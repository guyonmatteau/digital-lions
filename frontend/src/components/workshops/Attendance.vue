<template>
  <form @submit.prevent="$emit('submitAttendance', children)">
    <div v-for="child in children" :key="child.id">
      <p>{{ child.first_name }} {{ child.last_name }}</p>
      <label>
        <input type="radio" v-model="child.attendance" value="present" required />Present
      </label>
      <label>
        <input type="radio" v-model="child.attendance" value="absent" required />Absent
      </label>
      <label>
        <input type="radio" v-model="child.attendance" value="cancelled" required />Cancelled
      </label>
    </div>
    <button type="submit">Submit attendance</button>
  </form>
</template>
<script setup lang="ts">
interface Child {
  id: number
  first_name: string
  last_name: string
  community: string
  attendance?: string
}
defineProps({
  children: {
    type: Array as () => Child[],
    required: true
  }
})

defineEmits(['submitAttendance'])
</script>
