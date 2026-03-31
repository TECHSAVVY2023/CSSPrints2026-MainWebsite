<template>
   <div id="location" class="flex justify-center items-center bg-[#3B5065] w-full min-h-[600px] px-4 sm:px-8 lg:px-20 py-16">

        <div class="bg-[url('/assets/imgs/map1.jpg')] flex flex-col lg:flex-row w-full max-w-7xl h-auto gap-10 lg:gap-20 px-5 sm:px-8 py-8 overflow-hidden rounded-3xl shadow-2xl">
            
                <!-- Map -->
                <div class="w-full lg:w-1/2 h-[300px] sm:h-[400px] lg:h-auto">
                    <iframe 
                        class="w-full h-full rounded-2xl"
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30401.421116511025!2d123.83401664314265!3d8.171992009143041!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3255ac6e02a7dfd7%3A0x98968b6f04a82104!2sJAL%20PRINTING%20SERVICES!5e1!3m2!1sen!2sph!4v1773992852832!5m2!1sen!2sph"
                        style="border:0;" 
                        loading="lazy">
                    </iframe>
                </div>

                <!-- Content -->
                <div class="flex flex-col justify-between w-full lg:w-1/2 gap-10">
            
                <div>
                    <h2 class="text-white font-semibold text-2xl sm:text-3xl">
                    CSS Printing Shop Association
                    </h2>
                    <p class="text-white pt-4 text-sm sm:text-base leading-relaxed">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eget semper erat. 
                    Suspendisse ante sem, tempus non est ut, volutpat pharetra est. 
                    Nulla aliquet pulvinar orci, vitae aliquet nisi fermentum dictum.
                    </p>
                </div>

                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-end gap-3">
                    <h2 class="text-white font-semibold text-lg sm:text-xl">
                    Call us now:
                    </h2>
                    <p class="text-white text-lg sm:text-xl">
                    +63 000 000 0000
                    </p>
                    <button class="bg-[#B86B1F] text-white px-6 py-2 sm:px-8 sm:py-3 rounded-lg hover:bg-[#7E450C] transition">
                    Call now
                    </button>
                </div>
            </div>

        </div>

    </div>
</template>