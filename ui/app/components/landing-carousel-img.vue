<script setup lang="ts">
        import { useCarouselImages } from '~/composables/carouselImages';

    const { images, activeIdx, nextSlide, prevSlide } = useCarouselImages();

    defineProps<{
        images: string[]
        activeIdx: number
        nextSlide: () => void
        prevSlide: () => void
    }>()
</script>

<template>
    <div class="bg-white rounded-xl shadow-2xl p-8 md:p-12 flex flex-col md:flex-row gap-12 items-center">
        
        <div class="flex-1">
            <h2 class="text-2xl font-bold mb-6 tracking-wide uppercase">Lorem Ipsum Dolor Sit Amet</h2>
            <p class="text-gray-600 leading-relaxed mb-8">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, tincidunt a laoreet sit amet, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper turpis iaculis a.
            </p>
            <button class="bg-[#B86B1F] text-white px-8 py-3 rounded-md font-medium hover:bg-[#7E450C] transition">
                View Products
            </button>
        </div>

        <div class="flex-1 w-full relative group">
            <div class="rounded-lg overflow-hidden aspect-[4/3] bg-gray-100 relative">
                <img 
                :src="images[activeIdx]" 
                class="w-full h-full object-cover transition-opacity duration-500" 
                alt="Product Showcase"
                />
                
                <button @click="prevSlide" class="absolute left-4 top-1/2 -translate-y-1/2 bg-[#B86B1F] p-2 rounded-full text-white hover:bg-[#7E450C]">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                </button>
                <button @click="nextSlide" class="absolute right-4 top-1/2 -translate-y-1/2 bg-[#B86B1F] p-2 rounded-full text-white hover:bg-[#7E450C]">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                    </svg>
                </button>

                <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
                    <span 
                        v-for="(_, i) in images" :key="i"
                        @click="activeIdx = i"
                        class="w-2 h-2 rounded-full cursor-pointer transition-colors"
                        :class="activeIdx === i ? 'bg-white' : 'bg-white/40'"
                    ></span>
                </div>
            </div>
        </div>
    </div>
</template>