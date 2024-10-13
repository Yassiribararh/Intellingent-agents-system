import json
from transformers import pipeline

class SummaryAgent:
    def __init__(self):
        # Initialize the summarization model pipeline gpt2
        self.summarizer = pipeline("text-generation", model="gpt2")
    
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'textagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'generatereport':
            response = self.combine_summaries(message)
        
        return json.dumps({
            "sender": 'StatsAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })

    def combine_summaries(self, kqml_message):
        
        file_data = json.loads(kqml_message)["response"]

        if "summaries" not in file_data or not file_data['summaries']:
            return json.dumps({"error": "No summaries found in KQML message"})

        combined_summary = " ".join([summary["summary"] for summary in file_data["summaries"]])

        # Use the summarizer to refine the combined summary
        refined_summary = self.summarizer(combined_summary, max_length=100, num_return_sequences=1)[0]["generated_text"]

        return {
            "combined_summary": refined_summary
        }