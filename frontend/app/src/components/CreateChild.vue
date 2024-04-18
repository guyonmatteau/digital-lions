<template>
  <div>
    <h2>Child Information Form</h2>

    <!-- Child information form -->
    <form @submit.prevent="submitForm">
      <div>
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" v-model="child.firstName" required>
      </div>
      <div>
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" v-model="child.lastName" required>
      </div>
      <div>
        <label for="community">Community:</label>
        <select id="community" v-model="child.community" required>
          <option v-for="community in communities" :key="community.id" :value="community.name">{{ community.name }}</option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
const communities = ref([]);

// Define the API endpoint URL for fetching communities
const COMMUNITIES_API_URL = 'http://127.0.0.1:8000/communities';

// Define the child object with firstName, lastName, and community properties
const child = ref({
  firstName: '',
  lastName: '',
  community: ''
});

// Define a ref to store the fetched communities
/*const communities = ref([]);*/

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_API_URL);
    communities.value = response.data.communities;
    console.log('Fetched Communities:', communities.value);
  } catch (error) {
    console.error('Error fetching communities:', error);
  }
};

// Fetch communities when the component is mounted
onMounted(() => {
  fetchCommunities();
});

// Submit form function
const submitForm = () => {
  console.log('Submitted Child Information:', child.value);
  // Add logic to submit child information to backend API here
};
</script>

<style scoped>
/* Component-specific styles */
</style>
