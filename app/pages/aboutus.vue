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
            <NuxtLink to="/" class="hover:text-orange-600">Home</NuxtLink>
            <NuxtLink to="/service" class="hover:text-orange-600">Services</NuxtLink>
            <a href="#" class="hover:text-orange-600">About Us</a>
        </div>
        <div class="flex gap-3">
          <button class="bg-[#B86B1F] text-white px-6 py-2 rounded-md font-medium hover:bg-[#7E450C] transition">Login</button>
          <button class="bg-[#3a4d5e] text-white px-6 py-2 rounded-md font-medium hover:bg-[#1F2B37] transition">Register</button>
        </div>
      </div>
    </nav>

    <header class="relative h-[450px] flex items-center justify-start text-white overflow-hidden">
        <img 
            src="/Hero.png" 
            alt="Mugs background" 
            class="absolute inset-0 w-full h-full object-cover object-[center_30%]"
        />
        <div class="absolute inset-0 bg-black/50"></div>

        <div class="relative z-10 max-w-7xl px-60">
            <h1 class="text-6xl font-bold mb-4">
                ABOUT US
            </h1>
            <p class="text-lg md:text-xl font-light mb-8 max-w-2xl mx-auto">
                From custom mugs to ID services, we handle your printing needs with precision and care. Quality work, delivered fast.
            </p>
        </div>
    </header>

    <main class="max-w-6xl mx-auto mt-16 pb-56 px-4 relative z-20">
        <div class="bg-white rounded-xl shadow-2xl p-12 flex gap-12">
            <div class="flex-1 w-full relative group">
                <div class="rounded-lg overflow-hidden aspect-[4/3] bg-gray-100 relative">
                    <img 
                        src="/Hero.png" 
                        class="w-full h-full object-cover transition-opacity duration-500" 
                        alt="Product Showcase"
                    />
                </div>
            </div>
            
            <div class="flex-1 flex flex-col justify-between">
                <div>
                    <h2 class="text-2xl font-bold mt-10 mb-6 tracking-wide uppercase">
                        Lorem Ipsum Dolor Sit Amet
                    </h2>

                    <p class="text-gray-600 leading-relaxed mb-8">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, tincidunt a laoreet sit amet, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper turpis iaculis a.
                    </p>
                </div>

                <button class="bg-[#B86B1F] text-white px-8 py-3 mb-10 rounded-md font-medium hover:bg-[#7E450C] transition w-fit">
                    View Products
                </button>
            </div>
        </div>

        <div class="mt-40 mx-auto px-4">
            <h2 class="text-4xl font-bold text-[#222222] tracking-wide uppercase text-center">
                Founder
            </h2>

            <div class="w-48 md:w-[460px] h-[2px] bg-[#222222] mx-auto mb-20 rounded"></div>

            <div class="flex flex-col-reverse md:flex-row rounded-xl max-w-4xl mx-auto bg-white overflow-hidden items-stretch shadow-lg">
                
                <!-- TEXT -->
                <div class="p-6 md:p-20 flex-1">
                    <h1 class="text-2xl font-bold uppercase">
                        Name Here
                    </h1>

                    <p class="text-sm mt-4 leading-relaxed">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean mattis, augue a posuere blandit, massa arcu dictum nulla, 
                        feugiat interdum sapien lectus id nibh. Nulla facilisi. Pellentesque malesuada vitae mi sed porta. Aenean sed dolor lectus.
                        Sed quis purus vel eros finibus malesuada. Suspendisse placerat consequat tempus. Aliquam nec diam hendrerit, pharetra ligula nec, scelerisque ipsum.
                        Maecenas vel leo est. Fusce dignissim sodales tortor. In hac habitasse platea dictumst. Proin mattis dolor et dolor lobortis consectetur. Fusce nec nunc massa.
                    </p>
                </div>

                <!-- IMAGE -->
                <div class="w-full md:w-96 flex-shrink-0">
                    <img 
                        src="/founder.png" 
                        class="w-full h-64 md:h-full object-cover"
                        alt="Founder"
                    />
                </div>

            </div>
        </div>

        <!-- STAFFS SECTION -->
        <div class="mt-40 mx-auto px-4 max-w-6xl">
            <h2 class="text-4xl font-bold text-[#222222] tracking-wide uppercase text-center">
                Staffs
            </h2>

            <div class="w-48 md:w-[460px] h-[2px] bg-[#222222] mx-auto mb-20 rounded"></div>

            <!-- GRID WRAPPER (IMPORTANT FIX) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

                <div 
                    v-for="staff in staffs"
                    :key="staff.id"
                    class="bg-white rounded-xl shadow-lg overflow-hidden text-left p-8 h-[360px] flex flex-col"
                >
                    <img 
                        :src="staff.image"
                        class="w-32 h-32 mx-auto rounded-full object-cover mb-4"
                        :alt="staff.name"
                    />

                    <h3 class="text-xl font-bold uppercase">
                        {{ staff.name }}
                    </h3>

                    <!-- ROLE -->
                    <p class="text-sm text-[#B86B1F] font-medium mt-1 mb-4">
                        {{ staff.role }}
                    </p>

                    <!-- DESCRIPTION -->
                    <p class="text-sm text-gray-600 leading-relaxed flex-1">
                        {{ staff.description }}
                    </p>
                </div>

            </div>
        </div>
        
    </main>

    <div id="location" class="flex justify-center items-center bg-[#3B5065] w-full min-h-[600px] px-4 sm:px-8 lg:px-20 py-16">

      <div class="bg-[url('/map1.jpg')] flex flex-col lg:flex-row w-full max-w-7xl h-auto gap-10 lg:gap-20 px-5 sm:px-8 py-8 overflow-hidden rounded-3xl shadow-2xl">
        
        <!-- Map -->
        <div class="w-full lg:w-1/2 h-[300px] sm:h-[400px] lg:h-auto">
          <iframe 
            class="w-full h-full rounded-2xl"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30401.421116511025!2d123.83401664314265!3d8.171992009143041!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3255ac6e02a7dfd7%3A0x98968b6f04a82104!2sJAL%20PRINTING%20SERVICES!5e1!3m2!1sen!2sph!4v1773992852832!5m2!1sen!2sph"
            style="border:0;" 
            allowfullscreen="" 
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

<div class="relative flex justify-center items-center w-full px-4 py-12 md:py-20">
    <div class="relative bg-[#B86B1F] flex flex-col md:flex-row w-full max-w-[1200px] p-6 md:p-10 rounded-xl">

    <!-- Left Image -->
    <div id="left-image" class="relative flex-shrink-0 w-full md:w-1/2 mb-6 md:mb-0 overflow-hidden rounded-lg">
    
    <!-- Image -->
    <img
        src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&q=80&w=800"
        alt="FAQ Banner"
        class="w-full h-56 sm:h-64 md:h-full object-cover"
    />

    <!-- Dark Overlay -->
    <div class="absolute inset-0 bg-black/70"></div>

    <!-- Text Content -->
    <div class="absolute inset-0 flex flex-col justify-start px-8 pt-8 sm:pt-14 md:pt-20 text-left">
        <h2 class="text-white text-xl sm:text-2xl md:text-3xl font-bold">
        Frequently Asked Questions
        </h2>
        <p class="text-white text-sm sm:text-md md:text-lg pt-5">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, tincidunt a laoreet sit amet, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper turpis iaculis a. 
        </p>
    </div>

    </div>

    <div id="faqs" class="relative flex flex-col justify-start md:pt-12 lg:pt-14  h-[300px] md:h-[340px] overflow-y-auto no-scrollbar w-full">

      <div class="relative">

        <div class="absolute left-6 md:left-20 top-0 bottom-0 w-[2px] bg-white"></div>

        <div
          v-for="(item,index) in faqs"
          :key="index"
          class="relative pl-12 md:pl-28 pt-2 pb-4"
        >
            <div class="absolute left-[18px] md:left-[75px] top-5 w-3 h-3 bg-white rounded-full"></div>

            <button             
                @click="toggle(index)"
                class="text-left text-white text-lg md:text-xl w-full font-semibold"
            >
                {{ item.question }}
            </button>

            <transition name="faq-fade">
                <div
                v-if="activeIndex === index"
                class="mt-2 mr-0 md:mr-20 text-white text-sm md:text-md"
                >
                {{ item.answer }}
                </div>
            </transition>
        </div>
      </div>
    </div>

  </div>
</div>

    </div>
</template>

<script setup>
import { ref } from 'vue'

const staffs = [
    {
        id: 1,
        name: "John Doe",
        role: "Lead Designer",
        image: "/staff1.png",
        description: "Lead designer responsible for branding and UI systems."
    },
    {
        id: 2,
        name: "Jane Smith",
        role: "Operations Manager",
        image: "/staff2.png",
        description: "Handles operations and customer relations."
    },
    {
        id: 3,
        name: "Mike Lee",
        role: "Print Technician",
        image: "/staff3.png",
        description: "Print technician ensuring high-quality outputs."
    },
    {
        id: 4,
        name: "Jane Smith",
        role: "Print Technician",
        image: "/staff4.png",
        description: "Handles operations and customer relations."
    },
    {
        id: 5,
        name: "Mike Lee",
        role: "Lead Designer",
        image: "/staff5.png",
        description: "Print technician ensuring high-quality outputs."
    },
    {
        id: 6,
        name: "Mike Lee",
        role: "Operations Manager",
        image: "/staff6.png",
        description: "Print technician ensuring high-quality outputs."
    }
]

const activeIndex = ref(null)

const faqs = ref([
    {
        question: "1 Lorem ipsum dolor sit amet? ",
        answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, Credits to Niel For this layout idea, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper  iaculis a."
    },
    {
        question: "2 Lorem ipsum dolor sit amet? ",
        answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, Credits to Niel For this layout idea, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper  iaculis a."
    },
    {
        question: "3 Lorem ipsum dolor sit amet? ",
        answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, Credits to Niel For this layout idea, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper  iaculis a."
    },
    {
        question: "4 Lorem ipsum dolor sit amet? ",
        answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, Credits to Niel For this layout idea, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper  iaculis a."
    },
    {
        question: "5 Lorem ipsum dolor sit amet? ",
        answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus massa, Credits to Niel For this layout idea, tincidunt sed nibh. Ut vehicula pretium enim, non ullamcorper  iaculis a."
    }
])

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index

  nextTick(() => {
    const el = document.getElementById(`faq-${index}`)
    const container = el?.closest('.overflow-y-auto')

    if (el && container) {
      const offset = 20

      container.scrollTo({
        top: el.offsetTop - offset,
        behavior: 'smooth'
      })
    }
  })
}
</script>