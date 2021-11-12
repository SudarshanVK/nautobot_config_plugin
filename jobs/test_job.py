# import logging
# # importing pynautobot
# import pynautobot

# from datetime import datetime
from nautobot.extras.jobs import Job, ChoiceVar, Stringvar


class TestJob(Job):
    """
    Test job
    """

    test_string = StringVar(
        description="Just a test string",
        label="Just a test string",
        required=True,
    )
    
    class Meta:
        name = "Test Job"
        description = "Just a test job to get and print the test string"
        
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
        
        self.log_info(obj= None, message=f"Email address: {self.data['test_string']}")
        
    