<template>
  <div>
    <h2>Form</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nameSelect">What is your name?</label>
        <select id="nameSelect" v-model="selectedName">
          <option value="">Select</option>
          <option value="Stijn">Stijn</option>
          <option value="Nomfundo">Nomfundo</option>
          <option value="Alice">Alice</option>
          <!-- Add more hardcoded options if necessary -->
        </select>
      </div>
      <div>
        <label for="communitySelect">Community:</label>
        <select id="communitySelect" v-model="selectedCommunity">
          <option value="">Select</option>
          <option v-for="community in communities" :value="community.id" :key="community.id">{{ community.name }}</option>
        </select>
      </div>
      <div>
        <label>Workshop cancelled?</label>
        <div>
          <label>
            <input type="radio" v-model="workshopCancelled" value="yes"> Yes
          </label>
          <label>
            <input type="radio" v-model="workshopCancelled" value="no"> No
          </label>
        </div>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>
<script>
const COMMUNITIES_API_URL = 'http://127.0.0.1:8000/communities';
export default {
  data() {
    return {
      selectedName: '',
      selectedCommunity: '',
      communities: [], // Array to store communities fetched from API
      workshopCancelled: '' // Variable to store workshop cancellation status
    };
  },
  mounted() {
    // Assuming you have a method to fetch communities from the API
    this.fetchCommunities();
  },
  methods: {
    fetchCommunities() {
      // Assuming you have a method to fetch communities from the API
      // Replace this with your actual API call
      // For example:
      fetch(COMMUNITIES_API_URL)
        .then(response => response.json())
        .then(data => {
          this.communities = data.communities;
        })
        .catch(error => {
          console.error('Error fetching communities:', error);
        });
    },
    submitForm() {
      // Handle form submission
      console.log('Form submitted!');
      console.log('Selected name:', this.selectedName);
      console.log('Selected community:', this.selectedCommunity);
      console.log('Workshop cancelled?', this.workshopCancelled);
      // You can perform further actions here, such as sending data to the server
    }
  }
};
</script>
