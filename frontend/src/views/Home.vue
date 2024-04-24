<template>
    <h2>Home</h2>
  <div>
      Welcome to the Digital Lions app!
  </div>
</template>

<script lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { format } from 'date-fns'

import Navigation from '@/components/Navigation.vue'

export default {
  components: {
    Navigation,
  }
}
</script>
