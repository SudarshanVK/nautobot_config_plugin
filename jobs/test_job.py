# import logging
# # importing pynautobot
# import pynautobot

# from datetime import datetime
from nautobot.extras.jobs import Job, ChoiceVar, Stringvar


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
        
    