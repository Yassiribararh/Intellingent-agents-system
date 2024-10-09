import os
import glob
import json

class SearchAgent:
    def search_files(self, kqml_message):
        data = json.loads(kqml_message)
        drive_letter = os.path.expanduser(data["drive_letter"])
        file_mask = data["file_mask"]

        # Search for files
        file_paths = glob.glob(os.path.join(drive_letter, file_mask))
        file_count = len(file_paths)

        response = {"file_paths": file_paths, "files_count": file_count}
        return json.dumps(response)  # Return as JSON