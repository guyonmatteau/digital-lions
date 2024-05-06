<script lang="ts">
import Navigation from '../components/Navigation.vue'
import CreateChild from '../components/CreateChild.vue'
import ListChildren from '../components/ListChildren.vue'
export default {
  name: 'App',
  components: { Navigation, CreateChild, ListChildren }
}
</script>
<template>
  <CreateChild />
  <ListChildren />
</template>
