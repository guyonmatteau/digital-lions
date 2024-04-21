<template>
  <div>
    <h2>Form</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nameSelect">What is your name?</label>
        <select id="nameSelect" v-model="selectedName" required>
          <option value="">Select</option>
          <option value="Stijn">Stijn</option>
          <option value="Nomfundo">Nomfundo</option>
          <option value="Alice">Alice</option>
          <!-- Add more hardcoded options if necessary -->
        </select>
      </div>
      <div>
        <label for="communitySelect">Community:</label>
        <select id="communitySelect" v-model="selectedCommunity" requird>
          <option value="">Select</option>
          <option v-for="community in communities" :value="community.name" :key="community.id">
            {{ community.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Workshop cancelled?</label>
        <div>
          <label> <input type="radio" v-model="workshopCancelled" :value="true" /> Yes </label>
          <label> <input type="radio" v-model="workshopCancelled" :value="false" /> No </label>
        </div>
      </div>
      <button type="submit">Next</button>
    </form>
  </div>
</template>
<script lang="ts">
interface Community {
  id: number,
  name: string
}
export default {
  data() {
    return {
      selectedName: '',
      selectedCommunity: '',
      workshopCancelled: '' // Variable to store workshop cancellation status
    }
  },
  props: {
    communities: {
      type: Array as () => Community[],
      default: () => []
    }
  },
  methods: {
    submitForm() {
      this.$emit('form-submit', this)
    }
  }
}
</script>
