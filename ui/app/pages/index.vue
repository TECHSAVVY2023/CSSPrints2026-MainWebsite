<script setup lang="ts">
    import { useCarouselImages } from '~/composables/carouselImages';

    const {
        images,
        activeIdx,
        nextSlide,
        prevSlide,
        } = useCarouselImages();
</script>

<template>
    <div class="min-h-screen bg-[#F6F8FA] font-sans text-gray-900">
        <navbar />

        <div class="relative">
            <landing-hero />

            <div class="relative z-20 -mt-8 sm:-mt-10 md:-mt-14 lg:-mt-16 px-10 max-w-[1200px] mx-auto">
                <landing-carousel-img
                    :images="images"
                    :active-idx="activeIdx"
                    :next-slide="nextSlide"
                    :prev-slide="prevSlide"
                />
            </div>
        </div>

        <main class="max-w-6xl mx-auto py-10 px-4 relative z-20">

            <landing-top-services />

        </main>

        <location />

        <faqs />

        <landing-footer />

    </div>
</template>