<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navigation from '@/components/Navigation.vue'
</script>
<template>
  <body>
    <div>
      <Navigation />
    </div>
    <div>
      <RouterView />
    </div>
  </body>
</template>
