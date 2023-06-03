document.getElementById('startBot').addEventListener('click', function() {
    var mise = document.getElementById('mise').value;
    chrome.storage.sync.set({mise: mise}, function() {
      chrome.runtime.sendMessage({action: "startBot"});
    });
  });
  
  document.getElementById('stopBot').addEventListener('click', function() {
    // Logique pour arrêter le bot
  });
  