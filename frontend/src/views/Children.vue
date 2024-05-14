<template>
  <Create :communities="communities" @createChild="createChild" />
  <List :children="children" />
</template>
<script setup lang="ts">
import Create from '../components/children/Create.vue'
import List from '../components/children/List.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Community {
  id: number
  name: string
}
interface Child {
  firstName: string
  lastName: string
  communityId: string
}

// Define the API endpoint URL for fetching communities
const API_URL = process.env.API_URL
const COMMUNITIES_API_URL = API_URL + '/communities'
const CHILDREN_API_URL = API_URL + '/children'

const children = ref([])
const communities = ref([])

const statusMessage = ref<string>('')

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_API_URL)
    communities.value = response.data
  } catch (error: any) {}
}

// Fetch children from the backend API endpoint
const fetchChildren = async () => {
  try {
    const response = await axios.get(CHILDREN_API_URL)
    children.value = response.data
  } catch (error: any) {}
}

function createChild(child: Child) {
   const apiChild = {
    first_name: child.firstName,
    last_name: child.lastName,
    community_id: child.communityId
  }
  axios.post(CHILDREN_API_URL, apiChild)
  .then((response) => {
    // check if API call was successfull
    if (response.status == 201) {
      console.log("Child created successfully")
      //Update list with children
      fetchChildren()
    } else {
      console.log("Failed to create child")
    }
  })
  .catch((error) => {
    // Check if the error response indicates that the community already exists
    if (error.response && error.response.status === 409) {
      statusMessage.value = 'Child already exists.'
    } else {
      console.error('Error creating child:', error)
      statusMessage.value = 'Failed to create child. Please try again later.'
    }
  })
}

onMounted(() => {
  fetchCommunities()
  fetchChildren()
})
</script>
