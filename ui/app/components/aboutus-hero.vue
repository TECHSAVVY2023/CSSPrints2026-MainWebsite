<template>
  <header class="relative min-h-[350px] sm:min-h-[450px] 
                 flex items-center text-white overflow-hidden">
    
    <!-- Background image -->
    <img 
      src="/assets/imgs/about-hero.png" 
      alt="Mugs background" 
      class="absolute inset-0 w-full h-full object-cover object-[center_30%]"
    />

    <!-- Overlay -->
    <div class="absolute inset-0 bg-black/50"></div>

    <!-- Content -->
    <div class="relative z-10 w-full 
                px-6 sm:px-12 lg:px-20 text-left">
      
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold mb-3 sm:mb-4">
        ABOUT US
      </h1>

      <p class="text-sm sm:text-lg md:text-xl font-light 
                max-w-xl lg:max-w-2xl">
        From custom mugs to ID services, we handle your printing needs with precision and care. Quality work, delivered fast.
      </p>

    </div>
  </header>
</template>