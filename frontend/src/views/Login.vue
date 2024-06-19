<template>
  <Home />
  <form name="login-form" @submit.prevent="login(username, password)">
    <div class="mb-3">
      <label for="username">Email: </label>
      <input id="username" v-model="username" type="text" />
    </div>
    <div class="mb-3">
      <label for="password">Password: </label>
      <input id="password" v-model="password" type="password" />
    </div>
    <button class="btn btn-outline-dark" type="submit">Login</button>
  </form>
  <Notification />
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import Home from './Home.vue'
import Notification from '../components/Notification.vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const router = useRouter()
const store = useStore()

// Define the API endpoint URL for fetching communities
const API_URL = process.env.API_URL
const LOGIN_API_URL = API_URL + '/users/login'

function login(username: string, password: string) {
  console.log(LOGIN_API_URL)
  store.commit('login')
  router.push({ name: 'Home' })
  
  // comment out logging for Anni
  // axios
  //   .post(LOGIN_API_URL, { email_address: username, password: password })
  //   .then((response) => {
  //     // request with response in range 2xx
  //     store.commit('login')
  //     router.push({ name: 'Home' })
  //   })
  //   .catch((error) => {
  //     if (error.response) {
  //       const status = error.response.status
  //       let message: string
  //       switch (status) {
  //         case 400:
  //           message =
  //             'Bad Request: The server could not understand the request due to invalid syntax.'
  //           store.dispatch('triggerNotification', {
  //             message: 'Bad Request: Invalid syntax.',
  //             type: 'error'
  //           })
  //           break
  //         case 401:
  //         case 403:
  //           store.dispatch('triggerNotification', {
  //             message: 'Invalid credentials',
  //             type: 'error'
  //           })
  //           break
  //         case 404:
  //           store.dispatch('triggerNotification', {
  //             message: 'User email not found',
  //             type: 'error'
  //           })
  //           break
  //         case 422:
  //           store.dispatch('triggerNotification', {
  //             message: 'Email address not valid',
  //             type: 'error'
  //           })
  //           break
  //         case 500:
  //           message =
  //             "Internal Server Error: The server has encountered a situation it doesn't know how to handle."
  //           store.dispatch('triggerNotification', {
  //             message: 'Internal Server Error: Please try again later.',
  //             type: 'error'
  //           })
  //           break
  //         default:
  //           message = `Unexpected error: ${error.response.statusText}`
  //           store.dispatch('triggerNotification', {
  //             message: `Unexpected error: ${error.response.statusText}`,
  //             type: 'error'
  //           })
  //           break
  //       }
  //     }
  //   })
}
</script>
