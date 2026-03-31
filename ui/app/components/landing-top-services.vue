<script setup lang="ts">
    import services from '~/data/landing-top-services.json'
</script>

<template>
    <div id="top-selling-services" class="max-w-6xl mx-auto mt-32 pb-36 px-4 relative">
        <h2 class="text-4xl font-bold text-[#222222] tracking-wide uppercase text-center">Top Selling Services</h2>
        <div class="w-[460px] h-[2px] bg-[#222222] mx-auto mb-20 rounded"></div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

            <landing-top-services-card :services="services" />

        </div>

        <div class="mt-12 text-center">

            <button class="bg-[#B86B1F] text-white px-8 py-3 rounded-lg hover:bg-[#7E450C] transition inline-flex items-center justify-center gap-1">
            Services
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
            </button>

        </div>
    </div>
</template>