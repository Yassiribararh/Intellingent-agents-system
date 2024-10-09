import json
import os
import mimetypes

class MimeAgent:
    def check_mime(self, kqml_message):
        file_data = json.loads(kqml_message)

        # Assuming file_data["file_paths"] holds the paths
        files_with_mime = []

        for file_path in file_data["file_paths"]:
            mime_type, _ = mimetypes.guess_type(file_path)
            file_name = os.path.basename(file_path)
            files_with_mime.append({"file_path": file_path, "file_name": file_name, "mime_type": mime_type})

        # Wrap the output back into a dictionary
        return json.dumps({"files": files_with_mime, "files_count": file_data['files_count']})  # Return as a dictionary