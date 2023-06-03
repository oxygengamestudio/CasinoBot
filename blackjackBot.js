// Votre logique de bot ici
var mise;
chrome.storage.sync.get(['mise'], function(result) {
  mise = result.mise;
});

// Utilisez la valeur de `mise` pour jouer
