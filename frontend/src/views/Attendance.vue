<template>
  <h2>Attendance Form</h2>
  <div>
      Today is {{ todayFormatted }}
  </div>
  <div>
    <AttendanceForm
      :communities="communities"
      v-if="showFirstForm"
      @form-submit="handleFirstFormSubmit"
    />
    <!-- Second form is only shown when showSecondForm is true -->
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

import Navigation from '@/components/Navigation.vue'
import AttendanceForm from '@/components/AttendanceForm.vue'
import AttendanceFormChildren from '@/components/AttendanceFormChildren.vue'

const API_URL = process.env.API_URL

const COMMUNITIES_API_URL = API_URL + '/communities'
const communities = ref([])
const currentDate = new Date()
const todayFormatted= format(currentDate, "eeee MMM dd yyyy")
const databaseDate = format(currentDate, "yyyy-MM-dd")

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
const currentDate = new Date()
const todayFormatted= format(currentDate, "eeee MMM dd yyyy")
const databaseDate = format(currentDate, "yyyy-MM-dd")


interface Child {
  id: number;
  first_name: string
  last_name: string
  community: string
  attendance?: string
}
const API_URL = process.env.API_URL
const children = ref([] as Child[])

export default {
  components: {
    Navigation,
    AttendanceForm,
    AttendanceFormChildren
  },
  data() {
    return {
      showFirstForm: true,
      showSecondForm: false
    }
  },
  methods: {
    handleFirstFormSubmit(formData: any) {

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
            // map the children data to include attendance field and skip irrelevant fields
            children.value = response.data.children.map((child: Child) => ({
              id: child.id,
              first_name: child.first_name,
              last_name: child.last_name,
              community: child.community,
              attendance: ''
            }))
            console.log('Children 1:', children.value)
          })
          .catch((error) => {
            console.error('Error fetching children:', error)
          })

        console.log('Children 2:', children.value)
        this.showFirstForm = false
        this.showSecondForm = true
      }
    },
    handleChildrenAttendance(submittedAttendance: any) {

      // First submit that the workshop took place

      // After that submit the attendance of each child
      for (const child of submittedAttendance) {
        axios.post(API_URL + '/attendance', {
          child: child.id,
          community: child.community,
          day: databaseDate,
          cycle: '1',
          attendance: child.attendance
        })
      }
    }
  }
}
</script>
