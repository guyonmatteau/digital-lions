<template>
  <div id="nav">
    <nav class="container navbar navbar-expand-lg navbar-light bg-light">
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="navbar-nav mr-auto">
          <router-link to="/home" class="nav-item nav-link">Home</router-link>
          <router-link to="/attendance" class="nav-item nav-link">Workshop Attendance</router-link>
          <router-link to="/children" class="nav-link">Children</router-link>
          <router-link to="/communities" class="nav-link">Communities</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script lang="ts">
export default {
  // Component logic
}
</script>
