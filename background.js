chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "startBot") {
      chrome.tabs.executeScript(null, {file: "blackjackBot.js"});
    }
  });
  