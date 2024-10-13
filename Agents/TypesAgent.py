import json

class TypesAgent:
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'mimeagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'summarizefiles':
                response = self.check_types(message)
        
        return json.dumps({
            "sender": 'TypesAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })
        
    def check_types(self, kqml_message):
        file_data = json.loads(kqml_message)["response"]
        
        right_types_count = 0
        wrong_types_count = 0
        checked_files = []

        for file_obj in file_data["files"]:
            file_path = file_obj["file_path"]
            mime_type = file_obj["mime_type"]
            file_name = file_obj["file_name"]
            # Ensure file_type is a text
            if mime_type != "text/plain":
                print(f"Error: must be a text/plain file.")
                wrong_types_count += 1
            else:
                right_types_count += 1
            checked_files.append({"file_path": file_path, "file_name": file_name, "mime_type": mime_type})


        return {
            "files": checked_files,
            "files_count": file_data['files_count'],
            "right_types_count": right_types_count,
            "wrong_types_count": wrong_types_count
        }