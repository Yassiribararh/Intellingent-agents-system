import json
import os
import mimetypes

class MimeAgent:
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'searchagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'verifytypes':
                response = self.check_mime(message)
        
        return json.dumps({
            "sender": 'MimeAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })
        
    def check_mime(self, kqml_message):
        file_data = json.loads(kqml_message)["response"]

        files_with_mime = []

        for file_path in file_data["file_paths"]:
            mime_type, _ = mimetypes.guess_type(file_path)
            file_name = os.path.basename(file_path)
            files_with_mime.append({"file_path": file_path, "file_name": file_name, "mime_type": mime_type})

        return {
            "files": files_with_mime,
            "files_count": file_data['files_count']
            } 