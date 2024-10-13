import json
import sys
import logging
from Agents.RequirementsAgent import RequirementsAgent
from Agents.SearchAgent import SearchAgent
from Agents.MimeAgent import MimeAgent
from Agents.TypesAgent import TypesAgent
from Agents.TextAgent import TextAgent
from Agents.StatsAgent import StatsAgent
from Agents.SummaryAgent import SummaryAgent
from Agents.ReportAgent import ReportAgent
from Agents.ArchiveAgent import ArchiveAgent

# Suppress warnings from the transformers library
logging.getLogger("transformers").setLevel(logging.ERROR)

def run_system():
    # 1. Start the Requirements agent to get the user request.
    requirements_agent = RequirementsAgent()
    user_request = "I need a summary of all .txt files in the Desktop folder" 
    requirements_message = requirements_agent.send_message('SearchAgent', 'Search', user_request)

    # 2. Use SearchAgent to search files
    search_agent = SearchAgent()
    reply = search_agent.message_reply(requirements_message)
    print(reply)
    search_message = search_agent.send_message('MimeAgent', 'CheckMimeTypes', requirements_message)
    
    # If no files to summarize end execution
    if json.loads(search_message)['response'].get('files_count', 0) == 0:
        print("No text files to summarize")
        sys.exit()
        
    # 3. Use MIMEAgent to check MIME types
    mime_agent = MimeAgent()
    reply = mime_agent.message_reply(search_message)
    print(reply)
    mime_message = mime_agent.send_message('TypesAgent', 'VerifyTypes', search_message)
    
    # 4. Use TypesAgent to verify file extensions
    types_agent = TypesAgent()
    reply = types_agent.message_reply(mime_message)
    print(reply)
    types_message = types_agent.send_message('TextAgent', 'SummarizeFiles', mime_message)

    # 5. Use TextAgent to summarize text files
    text_agent = TextAgent()
    reply = text_agent.message_reply(types_message)
    print(reply)
    text_message = text_agent.send_message('StatsAgent', 'CollectStats', types_message)
    
    # 6. Use StatsAgent to collect statistics
    stats_agent = StatsAgent()
    reply = stats_agent.message_reply(text_message)
    print(reply)
    stats_message = stats_agent.send_message('ReportAgent', 'GenerateReport', text_message)
    
    # 7. Use SummaryAgent to combine summaries
    summary_agent = SummaryAgent()
    reply = summary_agent.message_reply(text_message)
    print(reply)
    summary_message = summary_agent.send_message('ReportAgent', 'GenerateReport', text_message)
    
    # 8. Use ReportAgent to generate a report
    report_agent = ReportAgent()
    reply = report_agent.message_reply(stats_message)
    print(reply)
    reply = report_agent.message_reply(summary_message)
    print(reply)
    report_message = report_agent.send_message('ArchiveAgent', 'ArchiveReport', user_request, stats_message, summary_message)

    # 9. Use ArchiveAgent to save results to a database
    archive_agent = ArchiveAgent()
    reply = archive_agent.message_reply(report_message)
    print(reply)
    archive_message = archive_agent.send_message('User', 'UserMessage', report_message)
    print(archive_message)

if __name__ == "__main__":
    run_system()