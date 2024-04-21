<script lang="ts">
import Navigation from '../components/Navigation.vue'
import CreateChild from '../components/CreateChild.vue'
export default {
  name: 'App',
  components: { Navigation, CreateChild }
}
</script>
<template>
  <CreateChild />
</template>
