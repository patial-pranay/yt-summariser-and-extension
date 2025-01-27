document.getElementById("summarizeBtn").addEventListener("click", function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.executeScript(tabs[0].id, {
            file: 'content.js'
        }, function(results) {
            const transcript = results[0];  // Assuming content.js returns the transcript
            document.getElementById("transcript").value = transcript;
            
            // Call the summarizer API or function here
            const summary = summarizeTranscript(transcript);  // Call the summarization function (we'll implement this next)
            document.getElementById("summary").innerText = summary;
        });
    });
});

function summarizeTranscript(transcript) {
    // Use an API or function to summarize the transcript (e.g., call to server or use client-side summarizer)
    return "This is a placeholder summary based on the transcript.";
}
