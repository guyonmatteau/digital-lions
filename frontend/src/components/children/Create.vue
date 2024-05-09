<template>
  <div>
    <h2>Children</h2>
    <div>Here you can add new children to the system.</div>

    <h3>Information</h3>
    <!-- Child information form -->
    <form @submit.prevent="$emit('createChild', child)">
      <div>
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" v-model="child.firstName" required />
      </div>
      <div>
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" v-model="child.lastName" required />
      </div>
      <div>
        <label for="community">Community:</label>
        <select id="community" v-model="child.communityId" required>
          <option v-for="community in communities" :key="community.id" :value="community.id">
            {{ community.name }}
          </option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
interface Child {
  firstName: string
  lastName: string
  communityId: string
}
interface Community {
  id: string
  name: string
}
defineProps({
  communities: {
    type: Array as () => Community[],
    required: true
  }
})
const child = ref<Child>
</script>
