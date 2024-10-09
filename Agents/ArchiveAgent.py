import datetime
import os

class ArchiveAgent:
    def save_report(self, report):

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Use '-' instead of ':' for filename compatibility

        directory = 'SavedReports/'

        # Create the directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        report_path = os.path.join(directory, f'Report-Generated-{timestamp}.txt')

        # Write the report to the file
        with open(report_path, 'w') as file:
            file.write(report)