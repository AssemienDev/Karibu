<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    @vite('resources/css/design.css')
    {{-- @vite('resources/css/style.css') --}}
    @vite('resources/js/slide.js')
    {{-- Swiper link to slide --}}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"/>

</head>
<body>
    
<div class="md:hidden">

    <div class="flex items-center justify-center min-h-20">
        <div class="container swiper">
            <div class="card-wrapper">
                <ul class="card-list swiper-wrapper">
                    <li class="card-item swiper-slide">
                        <a href="#" class="card-link">
                            <img src="{{ asset('images/suite-2.jpg')}}" alt="Card Image"
                            class="card-image object-cover">
                            <p class="bagde md:hidden">Suite</p>
                           {{--  <h2 class="card-title">Description de la chambre </h2>
                            <h2 class="card-title">Le prix  </h2> --}}                        
                        </a>
                    </li>
                    <li class="card-item swiper-slide">
                        <a href="#" class="card-link">
                            <img src="{{ asset('images/tv-2.jpg')}}" 
                            alt="Card Image" class="card-image object-cover">
                         <p class="bagde md:hidden">Television</p>
                         {{--   <h2 class="card-title">Description de la chambre </h2>
                            <h2 class="card-title">Le prix  </h2> --}}
                        </a>
                    </li>
                    <li class="card-item swiper-slide">
                        <a href="#" class="card-link">
                            <img src="{{ asset('images/table-suite.jpg')}}" 
                            alt="Card Image" class="card-image object-cover">
                        <p class="bagde md:hidden">Table suite </p>
                         {{-- <h2 class="card-title">Description de la chambre </h2>
                            <h2 class="card-title">Le prix  </h2> --}}
                        </a>
                    </li>
                </ul>

                {{-- Affiche la pagination en bas des bouttons  --}}
                <div class="swiper-pagination"></div>
                
                {{-- Affiche les bouttons next previous --}}
                {{-- <div class="swiper-button-prev"></div>
                <div class="swiper-button-next"></div> --}}
            </div>
        </div>
    </div>

    <div class="mx-5">
        <h2 class="underline font-bold text-lg text-center">Détail de l'article</h2>
        <p class="mb-4">
            <h2 class="font-bold text-lg">titre de l'hotel </h2>
            <span>Lorem ipsum dolor sit amet
                consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum 
                similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
        </p> 
        <p>
            <h2 class="font-bold text-lg">Le prix de l'hotel </h2>
            <span>Lorem ipsum dolor sit amet
                consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum 
                similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
        </p>
        <div class="justify-center flex sm:mb-5 mb-5">
            <a class="mt-5 text-white bg-violet-500
              items-center py-2 px-5 rounded-lg" 
              href="{{ route('reservation') }}">
                Reservez
            </a>
          </div>
    </div>
</div>

{{-- Grand ecran --}}
<section class="hidden max-w-7xl mx-auto px-3 py-5 md:block">
        <h2 class="hidden text-xl mb-8 underline text-center">
            Confirmez votre reservation 
        </h2>
        <div class="container flex flex-col md:flex-row sm:justify-around mx-7">
            <div class="flex-shrink-0 w-full sm:w-auto">
                <img src="{{ asset('images/suite-2.jpg')}}" class="object-cover md:max-w-[350px] md:h-full w-full">
            </div>
            <div class="mx-5 max-w-[350px]">
                <h2 class="underline font-bold text-lg text-center">Détail de l'article</h2>
                <p class="mb-4">
                    <h2 class="font-bold text-lg">titre de l'hotel </h2>
                    <span class="">Lorem ipsum dolor sit amet
                        {{-- consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum  --}}
                        similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
                </p> 
                <p>
                    <h2 class="font-bold text-lg">Le prix de l'hotel </h2>
                    <span>Lorem ipsum dolor sit amet
                        {{-- consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum  --}}
                        similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
                </p>
                <div class="justify-center flex">
                    <a class="mt-5 text-white bg-violet-500
                      items-center py-2 px-5 rounded-lg" 
                      href="{{ route('reservation') }}">
                        Reservez
                    </a>
                  </div>
            </div>  
        </div>
   
</section> 





<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

</body>
</html>