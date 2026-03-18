<template>
  <div class="min-h-screen bg-[#F6F8FA] font-sans text-gray-900">
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
          <a href="#" class="hover:text-orange-600">Home</a>
          <a href="#" class="hover:text-orange-600">Services</a>
          <a href="#" class="hover:text-orange-600">About Us</a>
        </div>
        <div class="flex gap-3">
          <button class="bg-[#c07128] text-white px-6 py-2 rounded-md font-medium hover:bg-orange-700 transition">Login</button>
          <button class="bg-[#3a4d5e] text-white px-6 py-2 rounded-md font-medium hover:bg-slate-800 transition">Register</button>
        </div>
      </div>
    </nav>

    <header class="relative h-[500px] flex items-center justify-center text-center text-white overflow-hidden">
      <img 
        src="https://images.unsplash.com/photo-1577937927133-66ef06ac9dfb?auto=format&fit=crop&q=80&w=2000" 
        alt="Mugs background" 
        class="absolute inset-0 w-full h-full object-cover"
      />
      <div class="absolute inset-0 bg-black/50"></div>

      <div class="relative z-10 max-w-4xl px-4">
        <h1 class="text-4xl md:text-6xl font-bold tracking-tight mb-4">
          ONE-STOP PRINTING AND DIGITAL
        </h1>
        <p class="text-lg md:text-xl font-light mb-8 max-w-2xl mx-auto">
          From custom mugs to ID services, we handle your printing needs with precision and care. Quality work, delivered fast.
        </p>
        <button class="bg-[#c07128] px-8 py-3 rounded-md font-semibold hover:bg-orange-700 transition uppercase text-sm tracking-widest">
          Enquire Now
        </button>
      </div>
    </header>

    <main class="max-w-6xl mx-auto -mt-16 mb-20 px-4 relative z-20">

      <div class="bg-white rounded-xl shadow-2xl p-8 md:p-12 flex flex-col md:flex-row gap-12 items-center">
        
        <div class="flex-1">
          <h2 class="text-2xl font-bold mb-6 tracking-wide uppercase">Lorem Ipsum Dolor Sit Amet</h2>
          <p class="text-gray-600 leading-relaxed mb-8">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, tincidunt a laoreet sit amet, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper turpis iaculis a.
          </p>
          <button class="bg-[#c07128] text-white px-8 py-3 rounded-md font-medium hover:bg-orange-700 transition">
            View Products
          </button>
        </div>

        <div class="flex-1 w-full relative group">
          <div class="rounded-lg overflow-hidden aspect-[4/3] bg-gray-100 relative">
            <img 
              :src="carouselImages[activeIdx]" 
              class="w-full h-full object-cover transition-opacity duration-500" 
              alt="Product Showcase"
            />
            
            <button @click="prevSlide" class="absolute left-4 top-1/2 -translate-y-1/2 bg-[#c07128]/80 p-2 rounded-full text-white hover:bg-orange-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
            </button>
            <button @click="nextSlide" class="absolute right-4 top-1/2 -translate-y-1/2 bg-[#c07128]/80 p-2 rounded-full text-white hover:bg-orange-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
              </svg>
            </button>

            <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
              <span 
                v-for="(_, i) in carouselImages" :key="i"
                @click="activeIdx = i"
                class="w-2 h-2 rounded-full cursor-pointer transition-colors"
                :class="activeIdx === i ? 'bg-white' : 'bg-white/40'"
              ></span>
            </div>
          </div>
        </div>
      </div>

      <div id="top-selling-services" class="max-w-6xl mx-auto mt-32 mb-40 px-4 relative">
        <h2 class="text-4xl font-bold text-[#222222] tracking-wide uppercase text-center">Top Selling Services</h2>
        <div class="w-[460px] h-[2px] bg-[#222222] mx-auto mb-20 rounded"></div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

          <div class="bg-white aspect-[3/4] rounded-lg shadow-xl p-6 flex flex-col items-left">
            <img src="#" alt="Custom Mugs" class="w-full h-48 object-cover rounded-md mb-4">
            <h3 class="text-2xl font-semibold mb-2">Service 1</h3>
            <p class="text-[#222222] text-lg text-left">Personalize your mugs with our high-quality printing services. Perfect for gifts and promotions.</p>
          </div>

          <div class="bg-white aspect-[3/4] rounded-lg shadow-xl p-6 flex flex-col items-left">
            <img src="#" alt="ID Services" class="w-full h-48 object-cover rounded-md mb-4">
            <h3 class="text-2xl font-semibold mb-2">Service 2</h3>
            <p class="text-[#222222] text-lg text-left">Fast and reliable ID card printing for schools, businesses, and events. Durable and professional results.</p>
          </div>

          <div class="bg-white aspect-[3/4] rounded-lg shadow-xl p-6 flex flex-col items-left">
            <img src="#" alt="Digital Printing" class="w-full h-48 object-cover rounded-md mb-4">
            <h3 class="text-2xl font-semibold mb-2">Service 3</h3>
            <p class="text-[#222222] text-lg text-left">High-quality digital printing for all your needs. From flyers to banners, we deliver vibrant results.</p>
          </div>

        </div>
      </div>

    </main>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeIdx = ref(0)
const carouselImages = [
  'https://images.unsplash.com/photo-1514228742587-6b1558fbed20?auto=format&fit=crop&q=80&w=800',
  'https://images.unsplash.com/photo-1572113173140-5e5e737bd31a?auto=format&fit=crop&q=80&w=800',
  'https://images.unsplash.com/photo-1539375665275-f9ad415ef9ac?auto=format&fit=crop&q=80&w=800'
]

const nextSlide = () => {
  activeIdx.value = (activeIdx.value + 1) % carouselImages.length
}

const prevSlide = () => {
  activeIdx.value = activeIdx.value === 0 ? carouselImages.length - 1 : activeIdx.value - 1
}
</script>

<style>
/* Optional: Smooth transitions for image switching */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>