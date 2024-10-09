# StatsAgent.py
import json

class StatsAgent:
    def collect_stats(self, kqml_message):
        file_data = json.loads(kqml_message)

        # Accessing the file paths directly from the message
        file_paths = []

        for file_path in file_data["summaries"]:
            file_paths.append({"file_path": file_path['file_path']})

        stats = {"total_files": file_data['files_count'], "file_paths": file_paths, "right_types_count": file_data['right_types_count'], "wrong_types_count": file_data['wrong_types_count']}

        return json.dumps(stats)