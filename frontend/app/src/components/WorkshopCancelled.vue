<template>
    <div>
      <h2 v-if="cancelled">Workshop Cancelled</h2>
      <p v-if="cancelled">The workshop has been successfully cancelled for today.</p>
      <p v-else>Error cancelling the workshop. Please try again later.</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import axios from 'axios';
  
  // Define the API endpoint URL
  const API_URL = 'https://api.example.com/cancelled-workshop';
  
  // Initialize the 'cancelled' variable to false
  let cancelled = false;
  
  // Perform the API call to notify the backend about the cancelled workshop
  axios.post(API_URL)
    .then(response => {
      if (response.status === 200) {
        console.log('Workshop cancelled successfully:', response.data);
        cancelled = true; // Set 'cancelled' to true if the API call is successful
      } else {
        console.error('Error cancelling workshop:', response.statusText);
      }
    })
    .catch(error => {
      console.error('Error cancelling workshop:', error);
    });
  </script>
  
  <style scoped>
  /* Component-specific styles */
  </style>
  