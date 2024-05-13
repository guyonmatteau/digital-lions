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
          <td>{{ workshop.community.name }}</td>
          <td>{{ workshop.cycle }}</td>
          <td>{{ workshop.cancelled }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup lang="ts">
interface Workshop {
  date: string
  community: {
    name: string
    id: number
  }
  cycle: number
  cancelled: boolean
}
defineProps({
  workshops: {
    type: Array as () => Workshop[],
    required: true
  }
})
</script>
