<template>
  <div>
    <h2>Attendance</h2>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Community</th>
          <th>First name</th>
          <th>Last name</th>
          <th>Attendance</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(attendance, index) in attendance" :key="index">
          <td>{{ attendance.workshop.date }}</td>
          <td>{{ attendance.workshop.community.name }}</td>
          <td>{{ attendance.child.first_name }}</td>
          <td>{{ attendance.child.last_name }}</td>
          <td>{{ attendance.attendance }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup lang="ts">
interface Attendance {
  attendance: string
  child: {
    first_name: string
    last_name: string
    id: number
  }
  workshop: {
    date: string
    cycle: number
    id: number
    community: {
      name: string
      id: number
    }
  }
}
defineProps({
  attendance: Array as () => Attendance[]
})
</script>
