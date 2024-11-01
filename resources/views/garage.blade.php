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

    @extends('base')

    @include('header')
    
<section class="py-5 text-center">
        <h1>NOS ESPACES</h1>
        <h2 class="font-semibold">Le Garage</h2>
        <p class="px-5 pt-3">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo nostrum vero praesentium officia hic quidem eos
             cupiditate consequuntur cumque eaque et cum illum dolorem ea, doloremque at impedit ullam temporibus.
            Perferendis nihil a esse, corrupti, dicta magni voluptas facere adipisci voluptates explicabo nemo. Maxime
             iure molestias minus fugiat perspiciatis, nulla labore fuga praesentium asperiores itaque nostrum possimus 
             voluptatem officiis! Voluptatum? Rerum, voluptates quia illum quidem nihil accusantium dolor alias ducimus 
             eaque cupiditate ipsum commodi, nemo praesentium accusamus deserunt hic? Dolorem debitis nostrum, recusandae dolore
              quibusdam culpa obcaecati placeat minima officia?Atque voluptas libero architecto consequuntur soluta eos veritatis 
              aliquam quia voluptatum sapiente quod velit harum, enim, error, magnam laboriosam! Laboriosam placeat non minus culpa
               est accusantium quae, molestiae totam! Hic!
        </p>
</section>


<div class="flex items-center justify-center min-h-20">
    <div class="container swiper">
        <div class="card-wrapper">
            <ul class="card-list swiper-wrapper">
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-2.jpg')}}" alt="Card Image"
                         class="card-image object-cover">                
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-4.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-3.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                        
                    </a>
                </li>
                <li class="card-item swiper-slide">
                    <a href="#" class="card-link">
                        <img src="{{ asset('images/suite-1.jpg')}}" 
                        alt="Card Image" class="card-image object-cover">
                        
                    </a>
                </li>
            </ul>
            <div class="swiper-pagination"></div>

            <div class="swiper-button-prev"></div>
            <div class="swiper-button-next"></div>

            
        </div>
    </div>
</div>

<hr class="mt-5">
<section class="text-center pt-3 mt-5">
    <h1 class="text-xl font-semibold">Contactez-nous</h1>
    <p class="text-lg px-5 text-black">
        Anyama , en face de la Paroisse Notre dame de la paix , côte d'ivoire <br>
    </p>
    <p class="text-2xl pt-3 font-bold text-black"> 📞 +225 0142847666 <span class="text-red-500">(24h/7j)</span></p>  
    <p class="text-black text-2xl">
        eventmarie@gmail.com
    </p>
</section> 



@include('footer')

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

</body>
</html>