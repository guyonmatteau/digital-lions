<template>
  <List :attendances="attendances" />
</template>
<script setup lang="ts">
import List from '../components/attendance/List.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Attendance {
  attendance: string
  child: {
    first_name: string
    last_name: string
    id: number
  }
  workshop: {
    date: string
    cycle: number
    id: number
    community: {
      name: string
      id: number
    }
  }
}
// Define the API endpoint URL for fetching communities
const API_URL = process.env.API_URL
const ATTENDANCE_URL = API_URL + '/attendance'

const attendances = ref([])

async function fetchAttendance() {
  try {
    const response = await axios.get(ATTENDANCE_URL)
    attendances.value = response.data
  } catch (error) {
    console.error('Error fetching attendance:', error)
  }
}

onMounted(() => {
  fetchAttendance()
  console.log(attendances.value)
})
</script>
