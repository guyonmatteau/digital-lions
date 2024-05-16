<template>
  <Create :communities="communities" @createChild="createChild" />
  <List :children="children" />
  <Notification />
</template>
<script setup lang="ts">
import Create from '../components/children/Create.vue'
import List from '../components/children/List.vue'
import Notification from '../components/Notification.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useStore } from 'vuex'

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
const store = useStore()

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
  axios
    .post(CHILDREN_API_URL, apiChild)
    .then((response) => {
      // check if API call was successfull
      if (response.status == 201) {

        store.dispatch('triggerNotification', {
          message: 'Child created successfully!',
          type: 'success'
        })

        //Update list with children
        fetchChildren()
      } else {

        store.dispatch('triggerNotification', {
          message: 'Failed to create child!',
          type: 'error'
        })
      }
    })
      // Check if the error response indicates that the community already exists
      if (error.response && error.response.status === 409) {
        store.dispatch('triggerNotification', {
          message: 'There already exists a child with the same name!',
          type: 'error'
        })
      } else {
        store.dispatch('triggerNotification', {
          message: 'Failed to create child! Please try again later.''
          type: 'error'
        })
      }
    })
}

onMounted(() => {
  fetchCommunities()
  fetchChildren()
})
</script>
