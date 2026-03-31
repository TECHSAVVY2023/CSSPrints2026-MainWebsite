<script setup lang="ts">
    import staffs from '~/data/aboutus-staffs.json'
</script>

<template>
    <div class="mt-40 mx-auto px-4 pb-60 max-w-6xl">
        <h2 class="text-4xl font-bold text-[#222222] tracking-wide uppercase text-center">
            Staffs
        </h2>

        <div class="w-48 md:w-[460px] h-[2px] bg-[#222222] mx-auto mb-20 rounded"></div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
            <aboutus-staff-card :staffs="staffs"/>
        </div>
    </div>
</template>