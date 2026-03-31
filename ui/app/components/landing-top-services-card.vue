<script setup lang="ts">
    defineProps<{
        services: {
            id: number
            title: string
            img: string
            description: string
        }[]
    }>()
</script>

<template> 
    <div v-for="service in services" :key="service.id" class="bg-white rounded-lg shadow-xl flex flex-col h-full overflow-hidden">

        <div class="h-48 w-full">
            <img :src="service.img" :alt="service.title" class="w-full h-full object-cover" />
        </div>

        <div class="px-6 pt-6 pb-10 flex flex-col">
        <h3 class="text-xl font-semibold mb-2">{{ service.title }}</h3>
        <p class="text-[#222222] text-md">{{ service.description }}</p>
        </div>

    </div>
</template>

