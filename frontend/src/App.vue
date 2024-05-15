<template>
  <img alt="Little Lions logo" src="./assets/logo.png" />
    <p>
      <strong>Current route path:</strong> {{ $route.fullPath }}
    </p>
  <router-view></router-view>
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
