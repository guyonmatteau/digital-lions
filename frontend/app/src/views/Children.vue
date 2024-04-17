<script lang="ts">
import Navigation from '../components/Navigation.vue'
import AttendanceFormChildren from '../components/AttendanceFormChildren.vue'
export default {
    name: 'App',
    components: { Navigation, AttendanceFormChildren }
}
</script>
<template>
  <AttendanceFormChildren />
</template>


