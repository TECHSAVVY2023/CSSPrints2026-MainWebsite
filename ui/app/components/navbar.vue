<template>
    <nav class="flex items-center justify-between px-8 py-4 bg-white shadow-sm">
        <div class="flex items-center gap-8 ml-40">
            <div class="w-10 h-10 flex items-center justify-center">
                <img src="/assets/imgs/Logo.png"
                    class="scale-[1.5]"
                />
            </div>

        </div>
        <div class="flex items-center gap-8 mr-10 ">
            <div class="hidden md:flex gap-6 font-medium">
                <NuxtLink to="/" class="nav-link hover:text-[#B86B1F]
                                        hover:underline underline-offset-4 decoration-2">Home</NuxtLink>
                <NuxtLink to="/service" class="nav-link hover:text-[#B86B1F] 
                                        hover:underline underline-offset-4 decoration-2">Services</NuxtLink>
                <NuxtLink to="/aboutus" class="nav-link hover:text-[#B86B1F] 
                                        hover:underline underline-offset-4 decoration-2">About Us</NuxtLink>
            </div>

            <div class="relative hidden md:block">
                <input 
                    type="text" 
                    placeholder="Search..." 
                    class="bg-gray-100 border-none rounded-md py-2 px-4 w-80
                            focus:ring-2 focus:ring-orange-500 outline-none"
                />
                <button class="absolute right-0 top-0 h-full px-3 bg-slate-700 rounded-r-md text-white">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
            </div>
        </div>
    </nav>
</template>