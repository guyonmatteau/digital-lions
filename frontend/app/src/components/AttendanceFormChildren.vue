<template>
  <div>
    <h2>Attendance Form for Children</h2>
    <!-- Attendance list -->
    <div v-for="(child, index) in children" :key="index">
      <label>{{ child }}</label>
      <input type="radio" v-model="selectedAttendance[child]" :value="'Present'" />
      <label>Present</label>
      <input type="radio" v-model="selectedAttendance[child]" :value="'Absent'" />
      <label>Absent</label>
      <input type="radio" v-model="selectedAttendance[child]" :value="'Cancelled'" />
      <label>Cancelled</label>
    </div>

    <!-- Submit button -->
    <button @click="submitForm">Submit</button>
  </div>
</template>

<script lang="ts">
export default {
  name: 'AttendanceFormChildren',
  props: {
    children: {
      type: Array,
      required: true
    }
  },
  data() {
    // Initialize selectedAttendance as an empty object
    return {
      selectedAttendance: {}
    }
  },
  methods: {
    submitForm() {
      // Log form data to the console
      console.log('Attendance:', this.selectedAttendance)

      // Add any additional form submission logic here
    }
  }
}
</script>

<style scoped>
/* Component-specific styles */
</style>
