<template>
    <form>
        <label>Name:</label>
        <input type="text" v-model="name">
    </form>
</template>

<script>
    export default {
        data() {
            return {
                name: ''
            }
        }
    }
</script>

