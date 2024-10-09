import unittest
from unittest.mock import patch, MagicMock
import json
from TaskExecutor import run_system

@patch('Agents.RequirementsAgent.RequirementsAgent')
@patch('Agents.SearchAgent.SearchAgent')
@patch('Agents.MimeAgent.MimeAgent')
@patch('Agents.TypesAgent.TypesAgent')
@patch('Agents.TextAgent.TextAgent')
@patch('Agents.StatsAgent.StatsAgent')
@patch('Agents.SummaryAgent.SummaryAgent')
@patch('Agents.ReportAgent.ReportAgent')
@patch('Agents.ArchiveAgent.ArchiveAgent')
@patch('builtins.print')
def test_run_system_with_files(self, MockPrint, MockArchiveAgent, 
                                 MockReportAgent, MockSummaryAgent, 
                                 MockStatsAgent, MockTextAgent, 
                                 MockTypesAgent, MockMimeAgent, 
                                 MockSearchAgent, MockRequirementsAgent):

    MockRequirementsAgent.return_value.process_requirements.return_value = json.dumps({
        "drive_letter": "/home/user/Documents",
        "file_mask": "*.txt",
        "files_count": 1
    })

    MockSearchAgent.return_value.search_files.return_value = json.dumps({
        "files": [{"file_path": "/home/user/Documents/sample.txt", 
                    "mime_type": "text/plain", "file_name": "sample.txt"}],
        "files_count": 1
    })

    MockMimeAgent.return_value.check_mime.return_value = json.dumps({
        "files": [{"file_path": "/home/user/Documents/sample.txt", 
                    "mime_type": "text/plain", "file_name": "sample.txt"}],
        "files_count": 1
    })

    MockTypesAgent.return_value.check_types.return_value = json.dumps({
        "files": [{"file_path": "/home/user/Documents/sample.txt", 
                    "mime_type": "text/plain", "file_name": "sample.txt"}],
        "files_count": 1
    })

    MockTextAgent.return_value.summarize_text.return_value = json.dumps({
        "summaries": [{"file_path": "/home/user/Documents/sample.txt", 
                       "summary": "This is a summary."}],
        "files_count": 1
    })

    MockStatsAgent.return_value.collect_stats.return_value = json.dumps({
        "total_files": 1,
        "summarized_files": 1
    })

    MockSummaryAgent.return_value.combine_summaries.return_value = json.dumps({
        "combined_summary": "This is a summary."
    })

    MockReportAgent.return_value.generate_report.return_value = "Report Content"
    MockArchiveAgent.return_value.save_report.return_value = None

    run_system()

    MockPrint.assert_any_call("Report Generated")
    MockArchiveAgent.return_value.save_report.assert_called_once_with("Report Content")

@patch('Agents.RequirementsAgent.RequirementsAgent')
@patch('builtins.print') 
def test_run_system_no_files(self, MockPrint, MockRequirementsAgent):

    MockRequirementsAgent.return_value.process_requirements.return_value = json.dumps({
        "drive_letter": "/home/user/Documents",
        "file_mask": "*.txt",
        "files_count": 0  
    })

    with self.assertRaises(SystemExit):
        run_system()

    MockPrint.assert_any_call("No text files to summarize")