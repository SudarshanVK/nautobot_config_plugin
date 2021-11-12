from nautobot.extras.jobs import Job, MultiObjectVar, BooleanVar

from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nautobot_plugin_nornir.constants import NORNIR_SETTINGS

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

        return result