<template>
  <h2>Submit attendance</h2>

  <WorkshopCancellation
    v-if="step === 1"
    :communities="communities"
    :todayFormatted="todayFormatted"
    @createWorkshop="createNewWorkshop"
  />

  <Attendance v-else-if="step === 2" :children="children" @submitAttendance="submitAttendance" />
  <Notification />
  <h2>Workshops</h2>
  <List :workshops="workshops" />
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import List from '../components/workshops/List.vue'
import WorkshopCancellation from '../components/workshops/Create.vue'
import Attendance from '../components/workshops/Attendance.vue'
import Notification from '../components/Notification.vue'
import axios from 'axios'
import { format } from 'date-fns'

import { useStore } from 'vuex'
interface Workshop {
  date: string
  cancelled?: boolean
  cancellation_reason?: string
  community_id?: number
  attendance?: { child_id: number; attendance: string }[]
}

interface Child {
  id: number
  first_name: string
  last_name: string
  community: string
  attendance?: string
}

const API_URL = process.env.API_URL

const COMMUNITIES_API_URL = API_URL + '/communities'
const WORKSHOPS_API_URL = API_URL + '/workshops'
const CHILDREN_API_URL = API_URL + '/children'

const currentDate = new Date()
const todayFormatted = format(currentDate, 'eeee MMM dd yyyy')
const databaseDate = format(currentDate, 'yyyy-MM-dd')
const step = ref(1)

const communities = ref([])
const workshops = ref([])
const workshop = ref<Workshop>({
  date: databaseDate
})

const children = ref([])
const store = useStore()

// Fetch communities from the backend API endpoint
const fetchCommunities = async () => {
  try {
    const response = await axios.get(COMMUNITIES_API_URL)
    communities.value = response.data
  } catch (error) {
    console.error('Error fetching communities:', error)
  }
}

// Fetch communities from the backend API endpoint
const fetchWorkshops = async () => {
  try {
    const response = await axios.get(WORKSHOPS_API_URL)
    workshops.value = response.data
  } catch (error) {
    console.error('Error fetching workshops:', error)
  }
}

const fetchChildren = async (communityId: number) => {
  try {
    const response = await axios.get(CHILDREN_API_URL, { params: { community_id: communityId } })
    children.value = response.data
  } catch (error) {
    console.error('Error fetching children:', error)
  }
}

function submitWorkshopInDB(workshopData: Workshop) {
  axios
    .post(WORKSHOPS_API_URL, workshopData)
    .then((response) => {
      store.dispatch('triggerNotification', {
        message: `Successfully created a workshop for ${todayFormatted} in ${communityId}!`,
        type: 'success'
      })
      fetchWorkshops()
    })
    .catch((error) => {
      store.dispatch('triggerNotification', {
        message: 'Failed to create workhop!',
        type: 'error'
      })
    })
}

function createNewWorkshop(workshopIn: any) {
  workshop.value.community_id = workshopIn.communityId
  if (workshopIn.cancelled) {
    workshop.value.cancelled = true
    submitWorkshopInDB(workshop.value)
  } else {
    workshop.value.cancelled = false
    fetchChildren(workshopIn.communityId)
    step.value = 2
  }
}

function submitAttendance(attendanceData: any) {
  const attendanceDataDB = attendanceData.map((child: any) => {
    return {
      child_id: child.id,
      attendance: child.attendance
    }
  })
  workshop.value.attendance = attendanceDataDB
  submitWorkshopInDB(workshop.value)
}

// Fetch communities when the component is mounted
onMounted(() => {
  fetchWorkshops()
  fetchCommunities()
})
</script>
