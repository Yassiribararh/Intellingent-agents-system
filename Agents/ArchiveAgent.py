import datetime
import os
import json

class ArchiveAgent:
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'reportagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'usermessage':
            self.save_report(message)
            response = "Report Generated"
        
        return response
        
    def save_report(self, report):

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Use '-' instead of ':' for filename compatibility

        directory = 'SavedReports/'

        # Create the directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        report_path = os.path.join(directory, f'Report-Generated-{timestamp}.txt')

        report = json.loads(report)["response"]

        # Write the report to the file
        with open(report_path, 'w') as file:
            file.write(report)