// Function to fetch the transcript using the YouTube Transcript API
function fetchTranscript() {
    const videoId = window.location.href.split("v=")[1].split("&")[0];  // Extract video ID from URL

    // Your YouTube Data API Key (replace with your actual API key)
    const apiKey = 'AIzaSyDXHvz5SgkVdhjGBP_aAxanuDMJfJhXCUM';

    // Make a request to the YouTube Data API (We’re going to use the YouTubeTranscriptApi here)
    fetch(`https://www.googleapis.com/youtube/v3/captions?videoId=${videoId}&key=${apiKey}`)
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data);  // Log the full API response for debugging

            // Check if the API response contains items and if each item has a text field
            if (data.items && data.items.length > 0) {
                const transcriptText = data.items
                    .filter(item => item.snippet && item.snippet.text) // Ensure 'text' exists
                    .map(item => item.snippet.text)
                    .join(' ');
                
                if (transcriptText) {
                    // Send the transcript text to the popup
                    chrome.runtime.sendMessage({ action: 'transcript', data: transcriptText });
                } else {
                    alert('No valid transcript text found.');
                }
            } else {
                alert('Transcript not found for this video.');
            }
        })
        .catch(error => {
            console.error('Error fetching transcript:', error);
            alert('Failed to fetch transcript.');
        });
}

// Trigger fetching the transcript when the content script is injected
fetchTranscript();
