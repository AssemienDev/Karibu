@include('header')

@extends('base')

@section('content')

<section class="mx-auto relative w-76 py-3 mt-5 md:w-[500px] shadow-lg rounded-lg">
    <h2 class="font-bold text-lg text-center">
        Votre choix
    </h2>

    {{-- <div class=""> --}}
        <div> 
            <img src="{{ asset('images/suite-1.jpg')}}" class=" w-[250px] mx-auto mt-10 sm:w-[400px] lg:w-[350px]">
            <h3 class=" font-semi-bold text-lg text-center mt-10">Description de l'hotel Description de l'hotel text-center text-center</h3>
        </div> 
    {{-- </div> --}}

    <h2 class="font-bold text-lg text-center my-7">
        Réservation
    </h2>

<section class="relative px-10">
    <form action="" method="POST" class="block">
            <input type="text" name="name=" id="name"  class="w-full h-[70px] my-2 rounded" placeholder="Nom Complet" required> 

            <label for="">Date et heure d'arrivée </label><br>
            <input type="time" id="datetime" class=" my-3 rounded">
            <input type="date" id="datetime" class=" my-3 rounded" >
            {{-- <input type="text" class="w-full h-[70px] my-3 rounded" placeholder="Cel: 0111403877" required> --}}
            <label for="password">*Le Numéro à contacter (après la validation) </label>
            <input type="text" class="w-full h-[70px] rounded my-3 " name="password" id="password" placeholder="cel:1111112222" required>
    
            <select class="form-control my-3" name="" id="">
                <option disabled> Durée </option>
                <option value=""> Nuitée </option>
                <option value=""> Journée</option>
            </select>

            <select class="form-control my-3" name="" id="">
                <option disabled> Durée </option>
                <option value=""> 24heures (journée entière ) </option>
                <option value=""> 12heures (demie / journée)</option>
            </select>

            <button type="submit" class="bg-violet-600 justify-center text-white items-center mx-auto mt-3 py-3 w-full rounded-md">
                <a href="{{ route('valider') }}" class="text-white">envoyer</a>
            </button>
        
    </form>
</section>

</section>


@include('footer')

@endsection


 