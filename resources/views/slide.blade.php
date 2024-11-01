<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    @vite('resources/css/design.css')
    @vite('resources/js/slide.js')
    {{-- Swiper link to slide --}}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"/>
</head>
<body>
    

<div class="flex items-center justify-center min-h-20">
    <div class="container swiper">
        <div class="card-wrapper">
            <ul class="card-list swiper-wrapper">
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-2.jpg')}}" alt="Card Image"
                         class="card-image object-cover">
                        <p class="bagde">Suite</p>
                        <h2 class="card-title">Description de la chambre </h2>
                        <h2 class="card-title">Le prix  </h2>
                        
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-4.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                        <p class="bagde ">Suite</p>
                        <h2 class="card-title">Description de la chambre </h2>
                        <h2 class="card-title">Le prix  </h2>
                        
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-3.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                        <p class="bagde">Suite</p>
                        <h2 class="card-title">Description de la chambre </h2>
                        <h2 class="card-title">Le prix   </h2>
                        
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-1.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                        <p class="bagde">Suite</p>
                        <h2 class="card-title">Description de la chambre </h2>
                        <h2 class="card-title">Le prix  </h2>
                        
                    </a>
                </li>
            </ul>
            <div class="swiper-pagination"></div>

            <div class="swiper-button-prev"></div>
            <div class="swiper-button-next"></div>

            
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

</body>
</html>