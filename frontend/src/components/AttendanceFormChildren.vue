<template>
  <form @submit.prevent="handleChildrenAttendance">
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

<script lang="ts">
interface Child {
  id: number
  first_name: string
  last_name: string
  community: string
  attendance: string
}
export default {
  props: {
    children: {
      type: Array as () => Child[],
      required: true
    }
  },
  methods: {
    handleChildrenAttendance() {
      // emit submitted data to parent component
      this.$emit('attendance-submit', this.children)
    }
  }
}
</script>
