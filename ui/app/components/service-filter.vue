<script setup>
import { ref } from "vue"

const showPurpose = ref(true)
const showPopularity = ref(true)

const togglePurpose = () => {
  showPurpose.value = !showPurpose.value
}

const togglePopularity = () => {
  showPopularity.value = !showPopularity.value
}
</script>

<template>
    <div class="flex flex-col w-[300px] h-auto rounded-lg pb-20 border border-gray-200 overflow-hidden">
        
        <!-- Header -->
        <div class="px-4 py-6 bg-[#3B5065] text-2xl text-white font-semibold">
        <h1>FILTER BY</h1>
        </div>

        <!-- Body (removed space-y-4) -->
        <div class="p-4 bg-white text-gray-800">

        <!-- PURPOSE -->
        <div class="mb-2">
            <button
            @click="togglePurpose"
            class="w-full flex justify-between items-center text-xl font-semibold uppercase text-gray-600 mb-2"
            >
            <span>Purpose</span>
            <span>{{ showPurpose ? "−" : "+" }}</span>
            </button>

            <div v-show="showPurpose" class="pl-1 space-y-2">
            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Personal</span>
            </label>

            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Business</span>
            </label>

            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Gift</span>
            </label>
            </div>
        </div>

        <!-- SEPARATOR (NOW FULLY CONTROLLABLE) -->
        <div class="border-t border-black mb-5 mt-5"></div>

        <!-- POPULARITY -->
        <div>
            <button
            @click="togglePopularity"
            class="w-full flex justify-between items-center text-xl font-semibold uppercase text-gray-600 mb-2"
            >
            <span>Popularity</span>
            <span>{{ showPopularity ? "−" : "+" }}</span>
            </button>

            <div v-show="showPopularity" class="pl-1 space-y-2">
            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Most Popular</span>
            </label>

            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Trending</span>
            </label>

            <label class="flex items-center gap-2 text-lg p-1">
                <input type="checkbox" class="accent-[#3B5065]" />
                <span>Newest</span>
            </label>
            </div>
        </div>

        </div>
    </div>
</template>