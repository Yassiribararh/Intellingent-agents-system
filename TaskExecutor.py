# TaskExecutor.py
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
    kqml_message = requirements_agent.process_requirements(user_request)
    print(kqml_message)

    # 2. Use SearchAgent to search files
    search_agent = SearchAgent()
    kqml_message = search_agent.search_files(kqml_message)

    # 3. Use MIMEAgent to check MIME types
    mime_agent = MimeAgent()
    kqml_message = mime_agent.check_mime(kqml_message)

    # 4. Use TypesAgent to verify file extensions
    types_agent = TypesAgent()
    kqml_message = types_agent.check_types(kqml_message)

    # 5. Use TextAgent to summarize text files
    text_agent = TextAgent()
    kqml_message = text_agent.summarize_text(kqml_message)
    
    # If no files to summarize end execution
    if json.loads(kqml_message).get('files_count', 0) == 0:
        print("No text files to summarize")
        sys.exit()

    # 6. Use StatsAgent to collect statistics
    stats_agent = StatsAgent()
    stats_message = stats_agent.collect_stats(kqml_message)

    # 7. Use SummaryAgent to combine summaries
    summary_agent = SummaryAgent()
    summary_message = summary_agent.combine_summaries(kqml_message)
        
    # 8. Use ReportAgent to generate a report
    report_agent = ReportAgent()
    report = report_agent.generate_report(user_request, stats_message, summary_message)

    # 9. Use ArchiveAgent to save results to a database
    archive_agent = ArchiveAgent()
    archive_agent.save_report(report)
    print("Report Generated")

if __name__ == "__main__":
    run_system()