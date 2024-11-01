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
                <div class="py-10">
                    <img src="{{ asset('images/nature.jpg') }}" alt="logo.png" class="w-96 mx-auto mt-10 sm:w-[400px] lg:w-[350px] md:hidden">
                </div>
                    <h2 class="text-center font-bold text-xl  underline mb-7">
                        Contactez-nous
                    </h2>
                <section class="relative px-10 ">
                    <form action="" method="POST" class="block">
                        <label for="name">Nom Complet <span class="text-red-500">*</span> </label>
                        <input type="email" name="email" id="name" class="w-full h-[70px] mt-3 mb-5 rounded" placeholder="John Doe" required> 

                        <label for="email">Email <span class="text-red-500">*</span> </label>
                        <input type="email" name="email" id="email" class="w-full h-[70px] mt-3 mb-5 rounded" placeholder="example@gmail.com" required>

                        <label for="message">Message <span class="text-red-500">*</span> </label>
                        <textarea name="message" id="message" cols="30" rows="10" class="w-full h-[150px] mt-3 mb-5 rounded" placeholder="Ici votre message ..."  required></textarea>

                        <button type="submit" class="bg-violet-600 text-white justify-center items-center mx-auto  py-3 w-full rounded-md" required>
                            envoyer
                        </button>
                    
                    </form>
                </section>
           </div>
        </div>
            {{-- l'image apparait seulement quand on est sur grand ecran --}}
            <div class="hidden md:block flex-1">
                <img src="{{ asset('images/nature.jpg') }}" alt="logo.png" class="h-full w-full object-cover">
            </div>
    </div>


   @include('footer')
@endsection