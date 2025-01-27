chrome.runtime.onInstalled.addListener(function() {
    console.log("YouTube Summarizer Extension Installed");
});

chrome.browserAction.onClicked.addListener(function(tab) {
    chrome.tabs.executeScript(tab.id, {
        file: 'content.js'
    });
});
