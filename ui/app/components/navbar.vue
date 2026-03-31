<template>
    <nav class="flex items-center justify-between px-8 py-4 bg-white shadow-sm">
        <div class="flex items-center gap-8">
            <div class="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center">
            <span class="text-orange-700 font-bold">LP</span>
            </div>
            
            <div class="relative hidden md:block">
            <input 
                type="text" 
                placeholder="Search..." 
                class="bg-gray-100 border-none rounded-md py-2 px-4 w-64 focus:ring-2 focus:ring-orange-500 outline-none"
            />
            <button class="absolute right-0 top-0 h-full px-3 bg-slate-700 rounded-r-md text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
            </button>
            </div>

        </div>
        <div class="flex items-center gap-8">
            <div class="hidden md:flex gap-6 font-medium">
                <NuxtLink to="/" class="hover:text-orange-600">Home</NuxtLink>
                <NuxtLink to="/service" class="hover:text-orange-600">Services</NuxtLink>
                <NuxtLink to="/aboutus" class="hover:text-orange-600">About Us</NuxtLink>
            </div>
            <div class="flex gap-3">
                <button class="bg-[#B86B1F] text-white px-6 py-2 rounded-md font-medium hover:bg-[#7E450C] transition">Login</button>
                <button class="bg-[#3a4d5e] text-white px-6 py-2 rounded-md font-medium hover:bg-[#1F2B37] transition">Register</button>
            </div>
        </div>
    </nav>
</template>