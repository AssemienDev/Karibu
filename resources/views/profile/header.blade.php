<section class="relative py-4">
    <nav class="fixed top-0 z-20 bg-gray-800 w-full grid grid-cols-none p-3 shadow-xl
    md:grid-cols-menu md:shadow-none mx-auto md:relative max-w-7xl">
        
    <div class="flex justify-between items-center md:justify-center">
        <a href="{{ route('home') }}">
            <img src="{{ asset('images/logo.png')}}" alt="logo app" class="w-12">
        </a>

        <button class="icone-toggle bg-white rounded p-2 inline-flex items-center 
        justify-center ring-1 ring-black ring-opacity-20 md:hidden">

        <img src="{{ asset('images/menu.png') }}" alt="menu toggle" class="w-6 h-6 ">
        </button>
    </div>

    <ul class="toggle-menu hidden px-1 md:pt-0 pt-6 bg-gray-800 flex flex-col md:flex md:bg-transparent
     md:flex-row md:space-x-10 md:w-auto md:items-center md:justify-center">
     
     {{-- Profile : ajout de md:hidden et de text-white text-white font-white--}}
     <li class="py-2 text-center border-t border-b border-gray-200 md:border-0 md:hidden ">
        <a href="{{ route('nave.profile') }}" class="font-medium text-lg text-white c
          hover:text-gray-900">Profile</a>
     </li>
     
     {{-- Mettre la route home ici --}}
     <li class="py-2 text-center border-t border-b border-gray-200 md:border-0 md:hidden">
        <a href="{{ route('nave.profile') }}" class="font-medium text-lg text-white font-white
          hover:text-gray-900">Logout</a>
     </li>
    </ul>

    {{-- Lien vers la page d'inscription --}}
    <div class="toggle-menu hidden flex justify-center items-center mt-6 md:mt-0 md-justify-end md:flex">
        <a href="{{ route('nave.inscription') }}"
        class="shadow-md py-2 px-3 border font-medium text-indigo-600 text-center w-40 bg-white hover:bg-gray-200 rounded-md"> Connexion </a>
    </div>
    </nav>

</section>