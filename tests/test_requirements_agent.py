import unittest
import json
from pathlib import Path
from Agents.RequirementsAgent import RequirementsAgent

class TestRequirementsAgent(unittest.TestCase):
    def setUp(self):
        self.agent = RequirementsAgent()

    def test_process_txt_files(self):
        # Test for a request to summarize .txt files in Desktop
        user_request = "I need a summary of all .txt files in Desktop"
        result = self.agent.process_requirements(user_request)
        expected = {"drive_letter": str(Path.home()) + "/Desktop", "file_mask": "*.txt"}
        self.assertEqual(result, expected)

    def test_invalid_request(self):
        # Test for an invalid file_type defaults to .txt
        user_request = "Please summarize all .jpg files in Pictures"
        result = self.agent.process_requirements(user_request)
        expected = {"drive_letter": str(Path.home()) + "/Pictures", "file_mask": "*.txt"}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()