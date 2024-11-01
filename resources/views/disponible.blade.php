@include('header')

@extends('base')


@section('content')
<section class="max-w-7xl mx-auto px-4 py-10">
    <p class="text-2xl mb-5 font-bold text-black">
        Disponible 
    </p>
     
    <div class="grid gap-5 grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
        {{-- <div class="shadow-lg">
            <img src="{{ asset('images/images.jpg')}}" class="w-full h-48 object-cover">
            <p class="text-center mt-2 font-semibold">Description de l'hotel</p>
            <div class="p-4">
                <div class="flex justify-between font-semibold">
                   <p>titre de l'hotel </p> 
                   <p>Le prix de l'hotel</p>
                </div>
                <a href="{{route("detail")}}" class="flex items-center justify-center px-4 py-2 mt-7
                font-semibold text-sm bg-gray-400 rounded-lg text-white">Voir detail</a>
            </div>
        </div> --}}

        <a href="{{route("detail")}}" class="flex items-center justify-center px-4 py-2
        font-semibold text-smrounded-lg text-white">
            <div> 
                <img src="{{ asset('images/suite-1.jpg')}}" class="w-full h-48 object-cover md:h-full">
                <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
            </div> 
        </a>

        <a href="{{route("detail")}}" class="flex items-center justify-center px-4 py-2
        font-semibold text-smrounded-lg text-white">
            <div> 
                <img src="{{ asset('images/suite-2.jpg')}}" class="w-full h-48 object-cover md:h-full">
                <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
            </div> 
        </a>

        <a href="{{route("detail")}}" class="flex items-center justify-center px-4 py-2
        font-semibold text-smrounded-lg text-white">
            <div> 
                <img src="{{ asset('images/ventile-3.jpg')}}" class="w-full h-48 object-cover md:h-full">
                <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
            </div> 
        </a>

        <a href="{{route("detail")}}" class="flex items-center justify-center px-4 py-2 
        font-semibold text-smrounded-lg text-white">
            <div> 
                {{--Peut-être mis dans images  md:max-w-[200px] --}}
                <img src="{{ asset('images/ventile-1.jpg')}}" class="w-full h-48 object-cover md:h-full">
                <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
            </div> 
        </a>
    </div>
    
</section>

@include('footer')
@endsection
