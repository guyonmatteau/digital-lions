<template>
  <img alt="Little Lions logo" src="./assets/logo.png" />
  <LoginView/>
</template>
<script setup lang="ts">
import LoginView from './views/Login.vue'
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

