import spacy
import json
import os

class RequirementsAgent:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_requirements(self, user_request):
        doc = self.nlp(user_request)

        # Initialize default values
        drive_letter = os.path.expanduser("~/Desktop")
        file_mask = "*.txt"

        # Limit folder map & types for prototype
        folder_map = {
            "desktop": "Desktop",
            "downloads": "Downloads",
            "documents": "Documents",
            "pictures": "Pictures",
            "videos": "Videos",
        }
        
        file_mask_map = {
            ".txt": ".txt",
        }

        # Check if the token matches any folder names and file types
        for token in doc:
            folder_name = token.text.lower()

            if folder_name in folder_map:
                drive_letter = os.path.join(os.path.expanduser("~"), folder_map[folder_name])

            if token.text.startswith(".") and len(token.text) > 1:
                if token.text in file_mask_map:
                    file_mask = "*" + token.text 

        return json.dumps({
            "drive_letter": drive_letter,
            "file_mask": file_mask
        })