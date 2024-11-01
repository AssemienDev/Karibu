@extends('base')

@section('title')
    Jeanine | Inscription
@endsection

@include('header')


@section('content')
    <div class="flex">
        {{-- Faire que l'image s'affiche sur grand ecran seulement --}}
        <div class="flex-1 flex flex-col justify-center items-center md:flex-none">
            {{-- Pour que la taille des inputs ne change pas --}}
            <div class="w-full max-w-xl">
                <div class="py-16">
                    <img src="{{ asset('images/nature.jpg') }}" alt="logo.png" class="md:hidden w-96 mx-auto mt-10 p-4 sm:w-[400px] lg:w-[350px]">
                </div>
                    <h2 class="text-center font-bold text-xl mb-10">
                        Inscrivez-vous et  commencez à <br> reservez
                    </h2>
                
    <section class="relative px-10 ">
        <form action="" method="POST" class="block space-y-10">
            <input type="text" class="w-full h-[70px]" placeholder="Nom Complet" name="name" id="name" required>
            <input type="email" class="w-full h-[70px]" placeholder="E-mail" name="email" id="email" required>
            <input type="password" class="w-full h-[70px]" placeholder="Mot de passe" name="password" id="password" required>
            <button type="submit" class="bg-violet-600 text-white justify-center items-center mx-auto px-7 py-3 w-full rounded-md" required>
                S'inscrire ✍️
            </button>
            <p class="text-center">
                vous avez un compte? 
                <a href="{{ route('nave.connexion') }}" class="text-violet-600 underline">Se connecter</a>
            </p>
        </form>
    </section>
{{-- Les icones : gmail et ... --}}
    <div class="justify-center flex ">
        <a href="" class="border border-gray-500 mx-3 p-3 my-4 text-white rounded-sm">
            <img src="{{ asset('images/logo.png') }}" alt="logo" class="w-2 ">
        </a>
        <a href="" class="border border-gray-500 mx-3 p-3 my-4  text-white rounded-sm">
            <img src="{{ asset('images/menu.png') }}" alt="logo" class="w-2 ">
        </a>
    </div>

</div>
</div>
{{-- l'image apparait seulement quand on est sur grand ecran --}}
<div class="hidden md:block flex-1">
    <img src="{{ asset('images/nature.jpg') }}" alt="logo.png" class="h-full w-full object-cover">
</div>
</div>


   @include('footer')
@endsection