@include('header')

@extends('base')

@section('content')


<section class="mx-auto relative px-10 w-76 py-5 shadow-lg mt-5 md:w-[500px]" >
    <h2 class="font-bold text-lg ">
        Passez au paiement
    </h2>
    <p>
        Choisissez un numéro pour le dépot et remplissez les champs d'informations !
    </p>

    <div class="text-red-700 flex flex-row justify-around items-center my-2">
        <span>0142847666</span>
        <img src="{{ asset('images/logo.png')}}" class="w-8 object-cover"> 
    </div>

    <div class="text-red-700 flex flex-row justify-around items-center my-2">
        <span>0142847666</span>
        <img src="{{ asset('images/logo.png')}}" class="w-8 object-cover">
    </div>

    <div class="text-red-700 flex flex-row justify-around items-center my-2">
        <span>0142847666</span>
        <img src="{{ asset('images/logo.png')}}" class="w-8 object-cover">
    </div>

    <h2 class="font-bold text-lg text-center mt-5 mb-2">
        Informations de paiement
    </h2>

    <h4 class="font-bold text-lg text-center">Total à payer :</h4>
    <h5 class="font-bold text-lg text-center mb-4">12000Frcfa</h5>



    <form action="" method="post" class="block" enctype="multipart/form-data">
        {{-- @csrf --}}
        {{-- <label for="name">*Numéro sur lequel vous avez effectué le dépot </label>
        <input type="text" class="w-full h-[50px] rounded-md mt-3 mb-5" name="name" id="name" required> --}}

        <label for="email">*Numéro ayant effectué le dépot </label>
        <input type="text" class="w-full h-[50px] rounded-md mt-3 mb-5" name="email" id="email" required>

    
        <input type="file" name="" id="" class="w-full h-[50px] rounded-md mt-3 mb-5">
        
        <button type="submit" class="bg-violet-600 text-white justify-center items-center mx-auto px-7 py-3 w-full rounded-md" required>
            valider
        </button>
        
    </form>
</section>



@include('footer')
@endsection


{{-- <div class="py-16 md:py-5">
    <h2 class="text-center font-bold text-xl  underline mb-7">
        Contactez-nous
    </h2>
    <div> 
        <img src="{{ asset('images/images.jpg')}}" class="w-96 mx-auto mt-10 sm:w-[400px] lg:w-[350px]">
        <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
    </div> 
    <img src="{{ asset('images/images.jpg') }}" alt="logo.png" class="w-96 mx-auto mt-10 sm:w-[400px] lg:w-[350px] md:hidden"> 
</div> --}}