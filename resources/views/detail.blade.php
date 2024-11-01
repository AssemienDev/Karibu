@include('header')

@extends('base')

@section('content')
    {{-- <section class="max-w-7xl mx-auto px-3 py-5">
        <h2 class="text-xl mb-5 underline text-center ">
            Confirmez votre reservation 
        </h2>
        <div class="container flex flex-col md:flex-row sm:justify-around">
            <div class="flex-shrink-0 w-full sm:w-auto">
                <img src="{{ asset('images/images.jpg')}}" class="w-full h-48 object-cover md:max-w-[500px] md:h-full mb-5">
            </div>
            <div class="mx-5">
                <h2 class="underline font-bold text-lg text-center">Détail de l'article</h2>
                <p class="mb-4">
                    <h2 class="font-bold text-lg">titre de l'hotel </h2>
                    <span>Lorem ipsum dolor sit amet
                        consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum 
                        similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
                </p> 
                <p>
                    <h2 class="font-bold text-lg">Le prix de l'hotel </h2>
                    <span>Lorem ipsum dolor sit amet
                        consectetur adipisicing elit. Minus excepturi, ducimus accusamus nisi repellat modi, blanditiis est fugiat, atque dolorum 
                        similique nulla eos cumque dolor expedita saepe porro ipsa facere!</span>
                </p>
                <div class="justify-center flex sm:mb-5">
                    <a class="mt-5 text-white bg-violet-500
                      items-center py-2 px-5 rounded-lg" 
                      href="{{ route('reservation') }}">
                        Reservez
                    </a>
                  </div>
            </div>  
        </div>
   
    </section> --}}

    @include('template')

    

    <section class="mx-auto bg-gradient-to-r from-violet-400 to-blue-500 pb-5 pt-2">
        <h2 class="text-center text-bold text-white pt-3"> Vos Avantages</h2>
            <ul class="flex flex-col md:flex-row justify-center ml-10 text-white list-disc flex-grap mt-5">
                <li class="sm:mx-5">odit asperiores ad, quia exercitationem mollitia.</li>
                <li class="sm:mx-5">Lorem ipsum dolor sit amet consectetur adipisicing  </li>
                <li class="sm:mx-5">elit. Facere possimus dolore saepe et exercitationem cum eveniet voluptate.  </li>
            </ul>   
    </section>
    <section class="max-w-7xl mx-auto px-4 py-10 mt-7">
    <div class="grid gap-5 grid-cols-2 sm:grid-cols-3 md:grid-cols-4 ">

        <a href="" class="flex items-center justify-center px-4 py-2
            font-semibold text-smrounded-lg text-white">
                <div> 
                    <img src="{{ asset('images/clime-rose.jpg')}}" class="w-full h-48 object-cover md:max-w-[500px] md:h-full">
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
                </div> 
        </a>

        <a href="" class="flex items-center justify-center px-4 py-2
            font-semibold text-smrounded-lg text-white">
                <div> 
                    <img src="{{ asset('images/ventile.jpg')}}" class="w-full h-48 object-cover md:max-w-[500px] md:h-full">
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
                </div> 
        </a>

        <a href="" class="flex items-center justify-center px-4 py-2
            font-semibold text-smrounded-lg text-white">
                <div> 
                    <img src="{{ asset('images/clime_violet.jpg')}}" class="w-full h-48 object-cover md:max-w-[500px] md:h-full">
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
                </div> 
        </a>

        <a href="" class="flex items-center justify-center px-4 py-2
            font-semibold text-smrounded-lg text-white">
                <div> 
                    <img src="{{ asset('images/clime-vert.jpg')}}" class="w-full h-48 object-cover md:max-w-[500px] md:h-full">
                    <p class=" mt-2 font-semibold text-center">Description de l'hotel Description de l'hotel text-center text-center</p>
                </div> 
            </a>
    </div>

    
{{-- <div class="main_content">
        <div class="section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-md-6 mb-4 mb-md-0">
                        <div class="product-image">
                            <div class="product_img_box"><img id="product_img" alt="product_img1"
                                    src="{{ asset('images/clime-violet - Copie.jpg') }}"
                                     > --}}
                                     {{--Peut-être mis dans le src data-zoom-image="/assets/files/culottes/culotte_8/10518988473111520886581236853833613928085898971684087225041.webp --}}
                                     {{-- <a 
                                     title="Zoom" class="product_img_zoom"><span class="linearicons-zoom-in"></span></a>  --}}
                            {{-- </div>
                            <div id="pr_item_gallery" data-slides-to-show="4" data-slides-to-scroll="1"
                                data-infinite="false"
                                class="product_gallery_item slick_slider slick-initialized slick-slider">
                                <div aria-live="polite" class="slick-list draggable">
                                    <div class="slick-track" role="listbox" style="opacity: 1; width: 556px; left: 0px;">
                                        <div class="item slick-slide slick-current slick-active" data-slick-index="0"
                                            aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide20"
                                            style="width: 129px;"><a href="#" class="product_gallery_item active" --}}
                                            {{-- Ce qui s'affiche en bas quand on clique sur l'image du bas--}}
                                                {{-- data-image="{{ asset('images/clime-vert.jpg') }}"
                                                data-zoom-image="{{ asset('images/clime-vert.jpg') }}"
                                                tabindex="0"><img alt="product_small_img1"
                                                    src="{{ asset('images/clime-vert.jpg') }}"></a> --}}
                                                    {{-- Ce qui s'affiche en bas --}}
                                        {{-- </div>
                                        
                                        <div class="item slick-slide slick-active" data-slick-index="1" aria-hidden="false"
                                            tabindex="-1" role="option" aria-describedby="slick-slide21"
                                            style="width: 129px;"><a href="#" class="product_gallery_item active"
                                                data-image="{{ asset('images/table-suite.jpg') }}"
                                                data-zoom-image="{{ asset('images/table-suite.jpg') }}"
                                                tabindex="0"><img alt="product_small_img1"
                                                    src="{{ asset('images/table-suite.jpg') }}"></a>
                                        </div>
                                        <div class="item slick-slide slick-active" data-slick-index="2" aria-hidden="false"
                                            tabindex="-1" role="option" aria-describedby="slick-slide22"
                                            style="width: 129px;"><a href="#" class="product_gallery_item active"
                                                data-image="{{ asset('images/douche.jpg') }}"
                                                data-zoom-image="{{ asset('images/douche.jpg') }}"
                                                tabindex="0"><img alt="product_small_img1"
                                                    src="{{ asset('images/douche.jpg') }}"></a>
                                        </div>
                                        <div class="item slick-slide slick-active" data-slick-index="3" aria-hidden="false"
                                            tabindex="-1" role="option" aria-describedby="slick-slide23"
                                            style="width: 129px;"><a href="#" class="product_gallery_item active"
                                                data-image="{{ asset('images/lavabo.jpg') }}"
                                                data-zoom-image="{{ asset('images/lavabo.jpg') }}"
                                                tabindex="0"><img alt="product_small_img1"
                                                    src="{{ asset('images/lavabo.jpg') }}"></a>
                                        </div>
                                    </div>
                                </div>
            </div>
        </div>
    </div> --}}
    

</section>

{{-- Faire un retour sur la page précedente --}}
<a href="{{ route('disponible') }}" class="mx-2 my-5">🔙</a>


    @include('footer')
@endsection

