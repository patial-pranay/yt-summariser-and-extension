from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)
import re
from preprocess_transcript import preprocess_transcript
from summarize_transcript import summarize_transcript



def get_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def fetch_transcript(video_url):
    """
    Fetches the transcript for a given YouTube video URL.
    """
    try:
        video_id = get_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])
    except TranscriptsDisabled:
        return "Transcript is disabled for this video."
    except NoTranscriptFound:
        return "No transcript found for this video."
    except VideoUnavailable:
        return "Video is unavailable."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    url = input("Enter a YouTube video URL: ")
    transcript = fetch_transcript(url)
    print("\n--- Raw Transcript ---\n")
    print(transcript)
    
    print("\n--- Cleaned Transcript ---\n")
    cleaned_transcript = preprocess_transcript(transcript)
    print(cleaned_transcript)
    
    print("\n--- Summary ---\n")
    summary = summarize_transcript(cleaned_transcript, num_sentences=5)
    print(summary)

