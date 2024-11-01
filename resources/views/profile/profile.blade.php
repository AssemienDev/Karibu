@extends('profile.base')
        @include('profile.header')

        <section class="max-w-7xl mx-auto px-4 py-10">
            <hr class="hidden md:block">
            <p class="text-2xl mb-5 font-bold text-white">
                Profil
            </p>
            <p class="text-2xl mb-1 font-bold text-white">
                Informations sur le profil
            </p>
            <p class="text-zinc-400 mb-5">
                Mettez à jour les informations de profil et l'adresse e-mail 
                de votre compte
            </p>
            <form action="" class="flex flex-col" method="POST">
                <label for="name" class="font-bold text-white">Nom</label> 
                <input type="text" name="name" id="name" class="max-w-[600px] h-[50px] rounded my-3 px-10 text-black"  >

                <label for="email" class="font-bold text-white">E-mail</label> 
                <input type="email" name="email" id="email" class="max-w-[600px] h-[50px] rounded my-3 px-10 text-black" >

                <button type="submit" class="bg-white rounded  max-w-[110px] py-2 text-black mt-2">
                    Sauvegarder
                </button>
            </form>

            <p class="text-2xl mt-16 font-bold text-white">
                Actualiser le mot de passe
            </p>
            <p class="text-zinc-400 mb-5">
                Assurez vous que votre compte utilise un mot de passe assez sécuriser 
              
            </p>
            <form action="" class="flex flex-col" method="POST">
                <label for="password" class="font-bold text-white">Mot de passe actuel</label> 
                <input type="password" name="password" id="password" class="max-w-[600px] h-[50px] rounded my-3 px-10 text-black"  >

                <label for="newpassword" class="font-bold text-white">Nouveau mot de passe</label> 
                <input type="password" name="newpassword" id="newpassword" class="max-w-[600px] h-[50px] rounded my-3 px-10 text-black" >

                <label for="newpassword" class="font-bold text-white">Confirmez le mot de passe</label> 
                <input type="password" name="newpassword" id="newpassword" class="max-w-[600px] h-[50px] rounded my-3 px-10 text-black" >


                <button type="submit" class="bg-white rounded  max-w-[110px] py-2 text-black mt-2">
                    Sauvegarder
                </button>
            </form>

            <p class="text-2xl mt-16 font-bold text-red-600">
                Supprimer votre compte
            </p>
            <p class="text-zinc-400 mb-5">
                Une fois votre compte supprimé , toutes ressources et données seront définitivement supprimées .
            </p>

            <button type="submit" class="bg-red-600 rounded max-w-[400px] px-4 py-3 text-white mt-2">
                SUPPRIMER LE COMPTE
            </button>

        </section>
    
    
    @include('profile.footer')





