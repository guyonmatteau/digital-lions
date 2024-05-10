<template>
  <Create :communities="communities" @createChild="createChildFromForm" />
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

function createChildFromForm(child: Child) {
  createChildInDB(child)
  fetchChildren()
}

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

function createChildInDB(child: Child) {
  const apiChild = {
    first_name: child.firstName,
    last_name: child.lastName,
    community_id: child.communityId
  }
  try {
    axios.post(CHILDREN_API_URL, apiChild)
  } catch (error) {
    console.error('Error submitting child information:', error)
  }
}

onMounted(() => {
  fetchCommunities()
  fetchChildren()
})
</script>
