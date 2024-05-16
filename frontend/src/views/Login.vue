<template>
  <Home />
  <form name="login-form" @submit.prevent="login(username, password)">
    <div class="mb-3">
      <label for="username">Username: </label>
      <input id="username" v-model="username" type="text" />
    </div>
    <div class="mb-3">
      <label for="password">Password: </label>
      <input id="password" v-model="password" type="password" />
    </div>
    <button class="btn btn-outline-dark" type="submit">Login</button>
  </form>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import Home from './Home.vue'

const username = ref('')
const password = ref('')

const router = useRouter()

const store = useStore()
function login(username: string, password: string) {
  store.commit('login')
  console.log(store.state.authenticated)

  router.push({ name: 'workshops' })
}
</script>
