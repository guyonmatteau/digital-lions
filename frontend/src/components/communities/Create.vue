<template>
  <div>
    <h2>Create Community</h2>

    <!-- Community creation form -->
    <form @submit.prevent="$emit('createCommunity', communityName)">
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

const communityName = ref('')
const successMessage = ref('')
const errorMessage = ref('')

</script>
