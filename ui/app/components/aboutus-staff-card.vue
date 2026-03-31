<script setup lang="ts">
    defineProps<{
        staffs: {
            id: number
            name: string
            role: string
            image: string
            description: string
        }[]
    }>()
</script>

<template>
    <div 
    v-for="staff in staffs"
    :key="staff.id"
    class="bg-white rounded-xl shadow-lg overflow-hidden text-left p-6 sm:p-8 
            w-full max-w-[300px] mx-auto flex flex-col"
    >
    <img 
        :src="staff.image"
        class="w-24 h-24 sm:w-32 sm:h-32 mx-auto rounded-full object-cover mb-4"
        :alt="staff.name"
    />

    <h3 class="text-lg sm:text-xl font-bold uppercase">
        {{ staff.name }}
    </h3>

    <!-- ROLE -->
    <p class="text-xs sm:text-sm text-[#B86B1F] font-medium mt-1 mb-3 sm:mb-4">
        {{ staff.role }}
    </p>

    <!-- DESCRIPTION -->
    <p class="text-xs sm:text-sm text-gray-600 leading-relaxed flex-1">
        {{ staff.description }}
    </p>
    </div>
</template>