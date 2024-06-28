<!-- Notification.vue -->
<template>
  <div v-if="message" :class="['notification', type]">
    {{ message }}
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      message: (state) => state.notification.message,
      type: (state) => state.notification.type
    })
  }
}
</script>
<style scoped>
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 5px;
  color: #fff;
  transition: opacity 0.3s ease;
}
.notification.success {
  background-color: #4caf50;
}
.notification.error {
  background-color: #f44336;
}
</style>
