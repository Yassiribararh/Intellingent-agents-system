# TextAgent.py
from transformers import pipeline
import json

class TextAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization")
    
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'typesagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'collectstats' or message_type.lower() == 'summarizetext':
                response = self.summarize_text(message)
        
        return json.dumps({
            "sender": 'TextAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })

    def summarize_text(self, kqml_message):
        file_data = json.loads(kqml_message)["response"]
        summaries = []

        for file in file_data.get("files", []):
            file_path = file["file_path"]
            mime_type = file["mime_type"]
            file_name = file["file_name"]
            
            # Read the content of the file
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                    if content.strip():  # Ensure content is not empty
                        summary = self.summarizer(content, max_length=10, min_length=5, do_sample=False)
                        summaries.append({"file_path": file_path, "mime_type": file_name, "file_name": mime_type, "summary": summary[0]["summary_text"]})
                    else:
                        print(f"Warning: {file_path} is empty.")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        return {
            "summaries": summaries,
            "files_count": file_data['files_count'],
            "right_types_count": file_data['right_types_count'],
            "wrong_types_count": file_data['wrong_types_count']
        }