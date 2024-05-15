<template>
  <Create @createCommunity="createCommunity" />
  <List :communities="communities" />
</template>

<script setup lang="ts">
import Create from '../components/communities/Create.vue'
import List from '../components/communities/List.vue'

import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Community {
  id: number
  name: string
}

const communities = ref<Community[]>([])
const statusMessage = ref<string>('')

const API_URL = process.env.API_URL
const COMMUNITIES_ENDPOINT = API_URL + '/communities'

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_ENDPOINT)
    communities.value = response.data
  } catch (error: any) {}
}

function createCommunity(communityName: string) {
  // Make API call to create the community
  axios
    .post(COMMUNITIES_ENDPOINT, {
      name: communityName
    })
    .then((response) => {
      // Check if the API call was successful
      if (response.status === 201) {
        statusMessage.value = 'Community created successfully!'
        // Update list with communities
        fetchCommunities()
      } else {
        statusMessage.value = 'Failed to create community. Please try again later.'
      }
    })
    .catch((error) => {
      // Check if the error response indicates that the community already exists
      if (error.response && error.response.status === 409) {
        statusMessage.value = 'Community already exists.'
      } else {
        console.error('Error creating community:', error)
        statusMessage.value = 'Failed to create community. Please try again later.'
      }
    })
}
onMounted(() => {
  fetchCommunities()
})
</script>
