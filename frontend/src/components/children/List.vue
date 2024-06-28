<template>
  <div>
    <h2>Children in Community</h2>
    <table>
      <thead>
        <tr>
          <th>First name</th>
          <th>Last name</th>
          <th>Community</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(child, index) in children" :key="index">
          <td>{{ child.first_name }}</td>
          <td>{{ child.last_name }}</td>
          <td>{{ child.community.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup lang="ts">
interface Child {
  first_name: string
  last_name: string
  community: {
    name: string
  }
}
defineProps({
  children: Array as () => Child[]
})
</script>
