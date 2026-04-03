<template>
    <div class="relative flex justify-center items-center w-full px-4 py-12 md:py-40">
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

            <!-- FAQ Section -->
            <div id="faqs" class="relative flex flex-col justify-start md:pt-12 lg:pt-14  h-[300px] md:h-[340px] overflow-y-auto no-scrollbar w-full">

                <div class="relative">
                <!-- Vertical Line -->
                <div class="absolute left-6 md:left-20 top-0 bottom-0 w-[2px] bg-white"></div>

                <div
                    v-for="(item,index) in faqs"
                    :key="index"
                    class="relative pl-12 md:pl-28 pt-2 pb-4"
                >
                    <!-- Dot -->
                    <div class="absolute left-[18px] md:left-[75px] top-5 w-3 h-3 bg-white rounded-full"></div>

                    <!-- Question -->
                    <button             
                    @click="toggle(index)"
                    class="faqs-items text-left text-white text-lg md:text-xl w-full font-semibold"
                    >
                    {{ item.question }}
                    </button>

                    <!-- Answer -->
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
</template>

<script setup>
import { ref } from 'vue'

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

<style>
/* Optional: Smooth transitions for image switching */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.faq-fade-enter-active,
.faq-fade-leave-active {
  transition: all 0.3s ease;
}

.faq-fade-enter-from,
.faq-fade-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}

.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

</style>