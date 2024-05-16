<template>
  <div id="nav">
    <nav class="container navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="navbar-nav mr-auto">
          <router-link to="/" class="nav-item nav-link">Home</router-link>
        </div>
        <div class="navbar-nav mr-auto">
          <router-link v-if="store.state.authenticated" to="/children" class="nav-link">Children</router-link>
        </div>
        <div class="navbar-nav mr-auto">
          <router-link v-if="store.state.authenticated" to="/communities" class="nav-link">Communities</router-link>
        </div>
        <div class="navbar-nav mr-auto">
          <router-link v-if="store.state.authenticated" to="/workshops" class="nav-item nav-link">Workshops</router-link>
        </div>
        <div class="navbar-nav mr-auto">
          <router-link v-if="store.state.authenticated" to="/attendance" class="nav-link">Attendance</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script setup lang="ts">
import { useStore } from 'vuex'
const store = useStore()


</script>
