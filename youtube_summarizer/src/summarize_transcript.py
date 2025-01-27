from transformers import pipeline

def summarize_transcript(transcript, num_sentences=5):
    """
    Summarizes the transcript using a modern transformer-based model (BART/T5).
    """
    if not transcript.strip():
        return "Error: The transcript is empty or contains only noise."
    
    # Initialize the summarizer pipeline (using BART or T5 model)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Generate the summary
    summary = summarizer(transcript, max_length=150, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']

if __name__ == "__main__":
    cleaned_transcript = input("Enter the cleaned transcript text: ")
    summary = summarize_transcript(cleaned_transcript, num_sentences=5)
    print("\n--- Summary ---\n")
    print(summary)
