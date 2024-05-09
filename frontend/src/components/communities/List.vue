<template>
  <div>
    <h2>Communities</h2>
    <table>
      <thead>
        <tr>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(community, index) in communities" :key="index">
          <td>{{ community.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup lang="ts">
defineProps({
  communities: {
    type: Array,
    required: true
  }
})
</script>
