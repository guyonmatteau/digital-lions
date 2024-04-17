<template>
  <div>
    <h2>Attendance Form</h2>
    <!-- Name dropdown -->
    <div>
      <label for="nameDropdown">What is your name?</label>
      <select id="nameDropdown" v-model="selectedName">
        <option value="Anne">Anne</option>
        <option value="Stijn">Stijn</option>
        <option value="Nomfundo">Nomfundo</option>
      </select>
    </div>

    <!-- Community dropdown -->
    <div>
      <label for="communityDropdown">Which community are you from?</label>
      <select id="communityDropdown" v-model="selectedCommunity">
        <option value="Community A">Community A</option>
        <option value="Community B">Community B</option>
        <option value="Community C">Community C</option>
      </select>
    </div>

    <!-- Cancelled checkbox -->
    <div>
      <input type="checkbox" id="cancelledCheckbox" v-model="isCancelled">
      <label for="cancelledCheckbox">Is the workshop cancelled?</label>
    </div>

    <!-- Submit button -->
    <button @click="submitForm">Submit</button>
  </div>
</template>
<script lang="ts">
export default {
  name: 'AttendanceForm',
  data() {
    return {
      selectedName: '',
      selectedCommunity: '',
      isCancelled: false
    };
  },
  methods: {
    submitForm() {
      // Handle form submission logic here
      console.log('Form submitted');
      console.log('Name', this.selectedName);
      console.log('Community', this.selectedCommunity);
      console.log('Is cancelled', this.isCancelled);
    }
  }
}
</script>