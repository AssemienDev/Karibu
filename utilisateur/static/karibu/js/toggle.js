// Sélectionner tous les éléments qui ont la classe toggle-menu
const menuElementsToggle = document.querySelectorAll(".toggle-menu");

// Sélectionner le bouton qui déclenche le menu avec la classe icone-toggle
const iconeTogggle = document.querySelector(".icone-toggle");

// Fonction pour basculer la visibilité des éléments du menu
const ToggleMenu = ()=> {
    menuElementsToggle.forEach(el => el.classList.toggle("hidden"))
};

// Fonction pour activer au click la navbar
iconeTogggle.addEventListener("click",ToggleMenu) ;

