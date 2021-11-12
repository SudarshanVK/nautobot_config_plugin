import logging
# importing pynautobot
import pynautobot

from datetime import datetime

from nautobot.extras.jobs import Job, MultiObjectVar, BooleanVar, StringVar, IntegerVar, FloatVar, DateVar, TimeVar, \
from nautobot.extras.models import Tag
from nautobot.dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site, Platform, Region, Rack, RackGroup
from nautobot.tenancy.models import Tenant, TenantGroup

from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister

from nautobot.dcim.filters import DeviceFilterSet

from nautobot_plugin_nornir.plugins.inventory.nautobot_orm import NautobotORMInventory
from nautobot_plugin_nornir.constants import NORNIR_SETTINGS
# from nornir_netmiko.tasks import netmiko_send_command
from nornir_napalm.plugins.tasks import napalm_get

InventoryPluginRegister.register("nautobot-inventory", NautobotORMInventory)


class TestJob(Job):
    """
    Test job
    """

    user_email = StringVar(
        description="User email",
        label="User email",
        required=True,
    )
    
    class Meta:
        name = "Test Job"
        description = "Just a test job to get and print the email address"
        
    def __init__(self):
        super().__init__()
        self.data = None
        self.commit = None
        
    def run(self, data, commit):
        """
        Run the job
        """
        
        self.data = data
        self.commit = commit
        
        self.log_info(f"Email address: {self.data['user_email']}")
        
    