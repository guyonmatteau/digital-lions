<template>
    <form @submit.prevent="handleSubmit">
        <label>Name</label>
        <input type="text" v-model="name">

        <label>Community</label>
        <select v-model="community">
            <option value="community1">Community 1</option>
            <option value="community2">Community 2</option>
            <option value="community3">Community 3</option>
        </select>

        <div class="form-check">
            <input type="checkbox" id="cancelled" v-model="cancelled">
            <label for="cancelled">
                Was this workshop cancelled due to the weather?
            </label>
        </div>

        <div class="submit">
            <button type="submit">Next</button>
        </div>

    </form>

    <p>Name: {{ name }}</p>
    <p>Community: {{ community }}</p>
    <p>Cancelled: {{ cancelled }}</p>
    
</template>

<script>
export default {
    data() {
        return {
            name: '',
            community: '',
            cancelled: false
        }
    },
    methods: {
        handleSubmit() {
            console.log('Form submitted')
        }
    }
}

</script>

<style>
form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
    }
label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}
input, select {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
}

input[type="checkbox"] {
    display: inline-block;
    width: 16px;
    margin: 0 10px 0 0;
    position: relative;
    top: 2px;
}
button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
}
.submit {
    text-align: center;
}
</style>

