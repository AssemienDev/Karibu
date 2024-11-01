@extends('base')


@include('header')

@section('content')
<section class="text-center">

    @include('sliderevent')

</section>
<section class="py-2 mt-5 text-center">
    <p class="font-bold text-3xl text-black">Pour la réussite de votre événement </p>
</section>

{{-- Partie des avantags --}}
<section class="max-w-7xl mx-auto px-4 ">
    <p class="text-xl font-bold text-black text-center">
        A votre dispositon 
    </p>
    <div class="grid gap-5 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        <a href="{{ route('espace.event') }}" class=" flex items-center justify-center px-4 py-2
                        font-semibold text-smrounded-lg text-white">
                <div class="border px-2 py-3 text-center"> 
                    <img src="{{ asset('images/menu.png')}}" class="mx-auto object-cover md:h-full">
                    <h4 class="py-2 text-sm font-semibold">SALLE DE RECEPTION</h4>
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center
                        ion de l'hotel Description de 
                    </p>
                </div> 
        </a>
        <a href="{{ route('espace.sallevip') }}" class=" flex items-center justify-center px-4 py-2
                        font-semibold text-smrounded-lg text-white">
                <div class="border px-2 py-3 text-center"> 
                    <img src="{{ asset('images/menu.png')}}" class="mx-auto object-cover md:h-full">
                    <h4 class="py-2 text-sm font-semibold">SALLE VIP</h4>
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center
                        ion de l'hotel Description de 
                    </p>
                </div> 
        </a>
        <a href="{{ route('espace.garage') }}" class=" flex items-center justify-center px-4 py-2
                font-semibold text-smrounded-lg text-white">
                <div class="border px-2 py-3 text-center"> 
                    <img src="{{ asset('images/menu.png')}}" class="mx-auto object-cover md:h-full">
                    <h4 class="py-2 text-sm font-semibold" > GARAGE</h4>
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center
                        ion de l'hotel Description de 
                    </p>
                </div> 
        </a>
    </div>
        
</section>



{{-- Partie Espace Karibu unique et spécial --}}
<section class="text-center py-8">
    <h1>Espace Karibu</h1>
    <h2 class="">Un espace unique et spécial</h2>
    <p class="max-w-[1000px] mx-auto text-black px-3 sm:text-lg">
        {{-- Justifier le texte  --}}
        L'esapce karibu est un espace événementiel approprié de luxe pour toutes vos  
        cérémonies , mariages , anniversaires etc ... 
        Notre espace a une capacité d'acceuil de plus de 300 personnes et 
        d'équipement techniques de très bonne qualité qui seront à votre  disposition.  
        {{-- flex text-black --}}
        <a href="{{route('espace.event')}}" class="flex items-center  text-decoration-none">En Savoir plus 
            <span class="material-symbols-outlined">
            arrow_right_alt
            </span>
        </a>
    </p>
</section>



{{-- Partie contact --}}
<hr>
<section class="text-center pt-3">
    <h1 class="uppercase font-semibold ">
        Besoin de visiter l'espace?
    </h1>
    <h1 class="text-xl font-semibold">Contactez-nous</h1>
    <p class="text-lg px-5 text-black">
        Anyama , en face de la Paroisse Notre dame de la paix , côte d'ivoire <br>
    </p>
    <p class="text-2xl pt-3 font-bold text-black"> 📞 +225 0142847666 <span class="text-red-500">(24h/7j)</span></p>  
    <p class="text-black text-2xl">
        eventmarie@gmail.com
    </p>


    {{-- <h2 class=" text-lg sm:font-bold sm:text-3xl font-extrabold ">
        Votre événement mérite un espace d'exception 
    </h2>
    <p class="">
        Nos différents tarifs , pour le moins abordable sont faits pour le bonheur de tous 
    </p> --}}
</section>



@include('footer')


@endsection
