import os
import json

class ReportAgent:
    def message_reply(self, message):
        message = json.loads(message)
        response = 'No reply for this sender'
        
        if message["sender"].lower() == 'statsagent' or message["sender"].lower() == 'summaryagent':
            response = 'Message Acknowledged By ' +  message["receiver"] + ' from ' + message["sender"]
        
        return response
        
    def send_message(self, receiver, message_type, user_request, stats_message, summary_message):
        response = 'No reply for this type of message'
        
        if message_type.lower() == 'archivereport':
            response = self.generate_report(user_request, stats_message, summary_message)
        
        return json.dumps({
            "sender": 'ReportAgent',
            "receiver": receiver,
            "response_code": 200,
            "response": response
        })
        
    def generate_report(self, user_request, stats_message, summary_message):
        stats = json.loads(stats_message)["response"]
        summary = json.loads(summary_message)["response"]
        report = (f" - For user request: {user_request}.\n"
                  f" - A total of {stats['total_files']} text files were found.\n"
                  f" - {stats['right_types_count']} Files have the right types.\n"
                  f" - {stats['wrong_types_count']} Had wrong types.\n"
                  f" - Combined summary of all the text files: {summary['combined_summary']}\n")
        return report