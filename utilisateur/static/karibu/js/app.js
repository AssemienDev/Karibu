let deferredPrompt;
const installButton = document.getElementById('installButton'); // Assurez-vous d'avoir un bouton d'installation dans votre HTML

window.addEventListener('beforeinstallprompt', (event) => {
  // Empêche l'affichage automatique du prompt
  event.preventDefault();
  // Enregistre l'événement pour le déclencher plus tard
  deferredPrompt = event;

  // Affichez le bouton d'installation
  installButton.style.display = 'block';

  installButton.addEventListener('click', () => {
    // Affichez le prompt d'installation
    deferredPrompt.prompt();
    // Attendez la réponse de l'utilisateur
    deferredPrompt.userChoice.then((choiceResult) => {
      if (choiceResult.outcome === 'accepted') {
        console.log('Utilisateur a accepté l\'installation de PWA');
      } else {
        console.log('Utilisateur a refusé l\'installation de PWA');
      }
      deferredPrompt = null;
    });
  });
});

window.addEventListener('appinstalled', (event) => {
  // Le PWA a été installé
  console.log('PWA installée', event);
});
