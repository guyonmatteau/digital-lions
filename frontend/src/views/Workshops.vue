<template>
 <h1> Workshops</h1>
  <div>
    <AttendanceForm
      :communities="communities"
      v-if="showFirstForm"
      @form-submit="handleFirstFormSubmit"
    />
    <AttendanceFormChildren
      :children="children"
      v-if="showSecondForm"
      @attendance-submit="handleChildrenAttendance"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { format } from 'date-fns'

import AttendanceForm from '@/components/AttendanceForm.vue'
import AttendanceFormChildren from '@/components/AttendanceFormChildren.vue'

const API_URL = process.env.API_URL

const COMMUNITIES_API_URL = API_URL + '/communities'
const communities = ref([])
const currentDate = new Date()
const todayFormatted = format(currentDate, 'eeee MMM dd yyyy')
const databaseDate = format(currentDate, 'yyyy-MM-dd')

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_API_URL)
    communities.value = response.data.communities
  } catch (error) {
    console.error('Error fetching communities:', error)
  }
}

interface Child {
  id: number
  first_name: string
  last_name: string
  community: string
  attendance?: string
}
const children = ref([] as Child[])
// Fetch communities when the component is mounted
onMounted(() => {
  fetchCommunities()
})


</script>

