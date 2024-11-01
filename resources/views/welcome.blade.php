{{-- <!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  @vite('resources/css/app.css')
</head>
<body> --}}
    {{-- <div class="flex justify-end mx-5">
        <a href="{{ route('register') }}" class="underline font-bold mx-5">Inscription</a>
        <a href="{{ route('login') }}" class="underline font-bold ">Connexion</a>
        <a href="{{ route('admin.category.index') }}" class="underline font-bold mx-5">Admin</a>
        <a href="{{ route('nave.connexion') }}" class="underline font-bold ">nav.conexion</a>
    </div> --}}

    @extends('base')

    @include('header')

    {{--Ajouter:  --}}

    @include("slider")

 
    {{-- <h1 class="hidden md:block text-xl md:text-4xl font-bold text-center text-violet-600 uppercase">
      Avantages
    </h1>  --}}
  {{-- Les images du wifi, service room etc ...  --}}
  <section class="sm:py-0"> 

    {{-- L'espace entre les avantages --}}
    <div class="flex mt-[50px] px-[50px] justify-around sm:justify-center sm:space-x-[150px]">
      
      <div class="text-center mt-1 flex-col flex "> 
        <a href="" class="bg-gray-300 border mx-5 p-10 rounded-full">
            <img src="{{ asset('images/logo.png') }}" alt="logo" class="w-10">
          </a>
        <p class="text-center font-bold">Wifi</p>
      </div> 

      <div class="text-center mt-1 flex-col flex "> 
        <a href="" class="bg-gray-300 border mx-5 p-10 rounded-full">
            <img src="{{ asset('images/logo.png') }}" alt="logo" class="w-10">
          </a>
        <p class="text-center font-bold">room serices</p>
      </div>

      
    </div> 



  </section>

    <h2 class="sm:mt-10 lg:text-3xl text-center text-violet-600 mt-5 font-bold ">
      Des logements avec tout le confort néccessaire
    </h2>
  
    <p class="text-lg text-center mt-3 px-10 ">
      Trouvez des logements entiers pour vos séjour et plus encore      
    </p> 

  
    @include('slide')
    
    {{-- Le boutton afficher plus --}}
     <div class="justify-end flex sm:mb-5 container mx-auto">
     <a class="mt-[50px] text-black ring ring-black
       items-center py-2 px-[24px] mx-5 
       rounded-lg" 
       href="{{ route('disponible') }}">
         Afficher plus
    </a>
    </div> 

    {{-- images et texte juste avant le bouton reservez --}}
    <section class="py-3 flex flex-col sm:flex-row max-w-4xl mx-auto">
      <div class="text-lg mx-10 flex-wrap">
        <img src="{{ asset('images/logo.png') }}" alt="logo securité" class="w-8 mx-10 mt-12 mb-2">
        <p>
          Trouvez des logements entiers pour vos séjour et plus encore Trouvez des logements entiers pour vos séjour et plus encore 
        </p>
      </div>

      <div class="text-lg mx-10 flex-wrap">
      <img src="{{ asset('images/logo.png') }}" alt="logo securité" class="w-8 mx-10 mt-12 mb-2">
      <p>
        Trouvez des logements entiers pour vos séjour et plus encore Trouvez des logements entiers pour vos séjour et plus encore 
      </p>
    </div>

    </section> 
    {{-- Le boutton reservez  --}}
    {{-- <button class="mt-[50px] text-white bg-violet-500
     items-center justify-start flex py-2 px-[45px] text-center
    mx-auto rounded-lg" 
    type="submit">
      Reservez 
    </button> --}}

   
      {{-- class="mt-[50px] text-white 
              flex items-center justify-center py-2 px-[45px] text-center
              mx-auto rounded-lg"> --}}


              {{-- <div class="mx-auto flex items-center justify-center">

                  <a href="{{ route('disponible') }}" 
                      class="bg-violet-500 ">
                            Reservez
                          
                </a>
              </div> --}}
            

              <div class="justify-center flex sm:mb-5">
                <a class="mt-5 text-white bg-violet-500
                  items-center py-2 px-5 rounded-lg" 
                  href="{{ route('disponible') }}">
                    Reservez
                </a>
              </div> 


    @include('footer')

   
  
{{--   
</body>
</html> --}}