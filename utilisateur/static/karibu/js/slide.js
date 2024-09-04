// Utilisation de Swiper pour le slider
alert('ok')
new Swiper('.card-wrapper', {
    loop: true,
    spaceBetween : 30,
  
    // Afficher les petits bouttons en bas
    pagination: {
      el: '.swiper-pagination',
      clickable : true ,
      dynamicBullets: true ,
    },
  
    // Faire marcher les bouttons sur le slider
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // pour le responsive des images
    breakpoints : {
        0: {
            slidesPerView: 1
        },
        768: {
            slidesPerView: 2
        },
        1024: {
            slidesPerView: 3
        },
    }
  });
  