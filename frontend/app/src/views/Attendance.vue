<template>
  <div>
    <Navigation />
    <AttendanceForm :communities="communities" @form-submit="handleFirstFormSubmit" />
    <!-- Second form is only shown when showSecondForm is true -->
    <AttendanceFormChildren :children="children" v-if="showSecondForm" @form-submit="handleSecondFormSubmit" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

import Navigation from '@/components/Navigation.vue'
import AttendanceForm from '@/components/AttendanceForm.vue'
import AttendanceFormChildren from '@/components/AttendanceFormChildren.vue'

const API_URL = 'http://127.0.0.1:8000'

const COMMUNITIES_API_URL = API_URL + '/communities'
const communities = ref([])

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_API_URL)
    communities.value = response.data.communities
  } catch (error) {
    console.error('Error fetching communities:', error)
  }
}
// Fetch communities when the component is mounted
onMounted(() => {
  fetchCommunities()
})
</script>

<script lang="ts">
const API_URL = 'http://127.0.0.1:8000'
const children = ref([])

export default {
  components: {
    Navigation,
    AttendanceForm,
    AttendanceFormChildren
  },
  data() {
    return {
      showSecondForm: false
    }
  },
  methods: {
    handleFirstFormSubmit(formData) {
      // Handle data from the first form
      console.log('Selected name:', formData.selectedName)
      console.log('Selected community:', formData.selectedCommunity)
      console.log('Workshop cancelled?', formData.workshopCancelled)
      // Update showSecondForm based on the data from the first form

      if (formData.workshopCancelled) {
        // If workshop is cancelled, show successfull cancellation message
        this.showSecondForm = false
      } else {
        // If workshop is not cancelled, show the second form to submit attendance
        const CHILDREN_URL = API_URL + '/children'

        axios
          .get(CHILDREN_URL, {
            params: {
              community: formData.selectedCommunity
            }
          })
          .then((response) => {
            children.value = response.data.children
            console.log('Response:', response)
            console.log('Children:', children)
          })
          .catch((error) => {
            console.error('Error fetching children:', error)
          })

        this.showSecondForm = true
      }
    },

    handleSecondFormSubmit(children) {
      // Handle data from the second form
      console.log('Data from second form:', formData)
    }
  }
}
</script>
