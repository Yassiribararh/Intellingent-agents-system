import json
from transformers import pipeline

class SummaryAgent:
    def __init__(self):
        # Initialize the summarization model pipeline gpt2
        self.summarizer = pipeline("text-generation", model="gpt2")

    def combine_summaries(self, kqml_message):
        
        file_data = json.loads(kqml_message)

        if "summaries" not in file_data or not file_data['summaries']:
            return json.dumps({"error": "No summaries found in KQML message"})

        combined_summary = " ".join([summary["summary"] for summary in file_data["summaries"]])

        # Use the summarizer to refine the combined summary
        refined_summary = self.summarizer(combined_summary, max_length=250, num_return_sequences=1)[0]["generated_text"]

        
        return json.dumps({"combined_summary": refined_summary})