import re

def preprocess_transcript(transcript):
    """
    Preprocess the transcript by:
    - Removing filler words or noise
    - Removing special characters
    - Stripping extra spaces
    """
    # Define common filler words (customize as needed)
    filler_words = ["um", "uh", "like", "you know", "I mean", "so", "actually", "basically"]

    # Remove filler words
    for filler in filler_words:
        transcript = re.sub(rf"\b{filler}\b", "", transcript, flags=re.IGNORECASE)

    # Remove special characters (except periods, commas, question marks, and exclamation marks)
    transcript = re.sub(r"[^\w\s.,!?]", "", transcript)

    # Replace multiple spaces with a single space
    transcript = re.sub(r"\s+", " ", transcript)

    # Strip leading/trailing spaces
    return transcript.strip()

if __name__ == "__main__":
    # Example usage
    raw_transcript = input("Enter raw transcript text: ")
    cleaned_transcript = preprocess_transcript(raw_transcript)
    print("\n--- Cleaned Transcript ---\n")
    print(cleaned_transcript)
