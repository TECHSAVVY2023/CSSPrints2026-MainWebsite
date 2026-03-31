<template>
    <div class="bg-white rounded-xl shadow-2xl 
                p-6 sm:p-8 lg:p-12 
                m-4 sm:m-10 lg:m-24 
                flex flex-col lg:flex-row gap-8 lg:gap-12 
                max-w-7xl mx-auto">

        <!-- Image -->
        <div class="flex-1 w-full relative group">
        <div class="rounded-lg overflow-hidden aspect-[4/3] bg-gray-100 relative">
            <img 
            src="/assets/imgs/about-hero.png" 
            class="w-full h-full object-cover transition-opacity duration-500" 
            alt="Product Showcase"
            />
        </div>
        </div>
        
        <!-- Content -->
        <div class="flex-1 flex flex-col justify-between">
        <div>
            <h2 class="text-xl sm:text-2xl font-bold mt-4 lg:mt-10 mb-4 lg:mb-6 tracking-wide uppercase">
            Lorem Ipsum Dolor Sit Amet
            </h2>

            <p class="text-sm sm:text-base text-gray-600 leading-relaxed mb-6 lg:mb-8">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, tincidunt a laoreet sit amet, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper turpis iaculis a.
            </p>
        </div>

        <button class="bg-[#B86B1F] text-white 
                        px-6 sm:px-8 py-2.5 sm:py-3 
                        mb-2 lg:mb-10 
                        rounded-md font-medium 
                        hover:bg-[#7E450C] transition w-fit">
            View Products
        </button>
        </div>

    </div>
</template>