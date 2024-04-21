<template>
  <div>
    <h2>Create Community</h2>

    <!-- Community creation form -->
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="communityName" required />
      </div>
      <button type="submit">Create Community</button>
    </form>

    <!-- Success message -->
    <p v-if="successMessage">{{ successMessage }}</p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const communityName = ref('')
const successMessage = ref('')
const errorMessage = ref('')

// Function to submit the form
const submitForm = async () => {
  try {
    // Make API call to create the community
    const response = await axios.post('http://127.0.0.1:8000/communities', {
      name: communityName.value
    })

    // Check if the API call was successful
    if (response.status === 201) {
      successMessage.value = 'Community created successfully!'
    } else {
      errorMessage.value = 'Failed to create community. Please try again later.'
    }
  } catch (error: any) {
    // Check if the error response indicates that the community already exists
    if (error.response && error.response.status === 409) {
      errorMessage.value = 'Community already exists.'
    } else {
      console.error('Error creating community:', error)
      errorMessage.value = 'Failed to create community. Please try again later.'
    }
  }
}
</script>

<style scoped>
/* Component-specific styles */
</style>
