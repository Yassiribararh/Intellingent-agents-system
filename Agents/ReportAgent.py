import os
import json

class ReportAgent:
    def generate_report(self, user_request, stats_message, summary_message):
        stats = json.loads(stats_message)
        summary = json.loads(summary_message)
        report = (f" - For user request: {user_request}.\n"
                  f" - A total of {stats['total_files']} text files were found.\n"
                  f" - {stats['right_types_count']} Files have the right types.\n"
                  f" - {stats['wrong_types_count']} Had wrong types.\n"
                  f" - Combined summary of all the text files: {summary['combined_summary']}\n")
        return report