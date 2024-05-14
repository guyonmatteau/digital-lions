<template>
    <form name="login-form" @submit.prevent="login(username, password)">
    <div class="mb-3">
      <label for="username">Username: </label>
      <input id="username" v-model="username" type="text" />
    </div>
    <div class="mb-3">
      <label for="password">Password: </label>
      <input id="password" v-model="password" type="password" />
    </div>
    <button class="btn btn-outline-dark" type="submit">
      Login
    </button>
  </form>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
const username = ref('')
const password = ref('')
function login(username: string, password: string) {
  console.log("Logged in with", username, password)  // Login logic here
}
</script>
