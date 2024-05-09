<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Community</th>
          <th>Cycle</th>
          <th>Cancelled</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(workshop, index) in workshops" :key="index">
          <td>{{ workshop.date }}</td>
          <td>{{ workshop.community_id }}</td>
          <td>{{ workshop.cycle }}</td>
          <td>{{ workshop.cancelled }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup lang="ts">
defineProps({
  workshops: {
    type: Array,
    required: true
  }
})
</script>
