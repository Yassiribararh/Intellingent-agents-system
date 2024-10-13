import os
import glob
import json

class SearchAgent:
    
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'requirementsagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'checkmimetypes':
                response = self.search_files(message)
        
        return json.dumps({
            "sender": 'SearchAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })
        
    def search_files(self, kqml_message):
        data = json.loads(kqml_message)["response"]
        
        drive_letter = os.path.expanduser(data["drive_letter"])
        file_mask = data["file_mask"]

        # Search for files
        file_paths = glob.glob(os.path.join(drive_letter, file_mask))
        file_count = len(file_paths)

        return {
            "file_paths": file_paths,
            "files_count": file_count
        }