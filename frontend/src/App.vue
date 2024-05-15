<script setup lang="ts">
import Navigation from '@/components/Navigation.vue'
</script>
<template>
  <header>
    <Navigation />
  </header>
  <main>
    <router-view />
  </main>
</template>
<script setup lang="ts">
import { onMounted } from 'vue'
import LoginView from './views/Login.vue'
onMounted(() => {
  console.log('App component mounted')
})
</script>
<style>
img {
  height: 200px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
