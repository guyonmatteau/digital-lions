<template>
  <h3>Workshop details</h3>
  <div>You are submitting attendance for the workshop on {{ todayFormatted }}</div>
  <div>
    <form @submit.prevent="$emit('createWorkshop', workshop)">
      <div>
        <label for="communitySelect">Community:</label>
        <select id="communitySelect" v-model="workshop.communityId" required>
          <option value="">Select</option>
          <option v-for="community in communities" :value="community.id" :key="community.id">
            {{ community.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Workshop cancelled?</label>
        <div>
          <label> <input type="radio" v-model="workshop.cancelled" :value="true" /> Yes </label>
          <label> <input type="radio" v-model="workshop.cancelled" :value="false" /> No </label>
        </div>
      </div>
      <button type="submit">Next</button>
    </form>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
interface Community {
  id: string
  name: string
}
defineProps({
  communities: {
    type: Array as () => Community[],
    required: true
  },
  todayFormatted: {
    type: String,
    required: true
  }
})

const workshop = ref({
  communityId: '',
  cancelled: ''
})
defineEmits(['createWorkshop'])
</script>
