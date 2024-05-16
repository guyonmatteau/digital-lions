<template>
  <Create @createCommunity="createCommunity" />
  <List :communities="communities" />
  <Notification />
</template>

<script setup lang="ts">
import Create from '../components/communities/Create.vue'
import List from '../components/communities/List.vue'
import Notification from '../components/Notification.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

import { useStore } from 'vuex'
interface Community {
  id: number
  name: string
}

const communities = ref<Community[]>([])
const statusMessage = ref<string>('')
const store = useStore()
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
        store.dispatch('triggerNotification', {
          message: `Community ${communityName} created successfully`,
          type: 'success'
        })

        // Update list with communities
        fetchCommunities()
      } else {
        store.dispatch('triggerNotification', {
          message: 'Failed to create community!',
          type: 'error'
        })
      }
    })
    .catch((error) => {
      // Check if the error response indicates that the community already exists
      if (error.response && error.response.status === 409) {
        store.dispatch('triggerNotification', {
          message: `Community ${communityName} already exists!`,
          type: 'error'
        })
      } else {
        store.dispatch('triggerNotification', {
          message: 'Failed to create community!',
          type: 'error'
        })
      }
    })
}
onMounted(() => {
  fetchCommunities()
})
</script>
