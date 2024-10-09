import json

class TypesAgent:
    def check_types(self, kqml_message):
        file_data = json.loads(kqml_message)
        right_types_count = 0
        wrong_types_count = 0
        checked_files = []

        for file_obj in file_data["files"]:
            file_path = file_obj["file_path"]
            mime_type = file_obj["mime_type"]
            file_name = file_obj["file_name"]
            # Ensure file_type is a text
            if mime_type != "text/plain":
                print(f"Error: must be a text/plain file.")
                wrong_types_count += 1
            else:
                right_types_count += 1
            checked_files.append({"file_path": file_path, "file_name": file_name, "mime_type": mime_type})


        return json.dumps({"files": checked_files, "files_count": file_data['files_count'], "right_types_count": right_types_count, "wrong_types_count": wrong_types_count})