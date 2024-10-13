# StatsAgent.py
import json

class StatsAgent:
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'textagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'generatereport':
                response = self.collect_stats(message)
        
        return json.dumps({
            "sender": 'StatsAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })
        
    def collect_stats(self, kqml_message):
        file_data = json.loads(kqml_message)["response"]

        # Accessing the file paths directly from the message
        file_paths = []

        for file_path in file_data["summaries"]:
            file_paths.append({"file_path": file_path['file_path']})

        return {
            "total_files": file_data['files_count'],
            "file_paths": file_paths,
            "right_types_count": file_data['right_types_count'],
            "wrong_types_count": file_data['wrong_types_count']
        }