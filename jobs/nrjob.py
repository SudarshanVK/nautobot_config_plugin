from nautobot.extras.jobs import Job, MultiObjectVar, BooleanVar


from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nautobot_plugin_nornir.plugins.inventory.nautobot_orm import NautobotORMInventory
from nautobot_plugin_nornir.constants import NORNIR_SETTINGS


InventoryPluginRegister.register("nautobot-inventory", NautobotORMInventory)


FIELDS = {
    "platform",
    "tenant_group",
    "tenant",
    "region",
    "site",
    "platform",
    "role",
    "rack",
    "rack_group",
    "manufacturer",
    "device_type",
}


def get_job_filter(data=None):
    """Helper function to return a the filterable list of OS's based on platform.slug and a specific custom value."""
    if not data:
        data = {}
    query = {}
    for field in FIELDS:
        if data.get(field):
            query[f"{field}_id"] = data[field].values_list("pk", flat=True)
    if data.get("device"):
        query.update({"id": data["device"].values_list("pk", flat=True)})
    return DeviceFilterSet(data=query, queryset=Device.objects.all()).qs

def init_nornir():
    """
    Initialize Nautobot Inventory
    """
    
    nr = InitNornir(
        runner=NORNIR_SETTINGS.get("runner"),
        logging={"enabled": False},
        inventory={
            "plugin": "nautobot-inventory",
            "options": {
                "credentials_class": NORNIR_SETTINGS.get("credentials"),
                "params": NORNIR_SETTINGS.get("inventory_params"),
                "queryset": get_job_filter(data),
                # "defaults": {"now": now},
            },
        },
    )

    return nr

class NrJob(Job):
    """
    Nautobot Job
    """
    
    device = MultiObjectVar(model=Device, required=True)
    
    def __init__(self):
        super().__init__()
        self.data = None
        self.commit = None

    def run(self, data, commit):
        """
        Run Nautobot Job
        """
        nr = init_nornir()
        self.log_info(obj= None, message=f"{nr}")