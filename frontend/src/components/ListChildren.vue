<template>
  <div>
    <h2>Children in Community</h2>
    <table>
      <thead>
        <tr>
          <th>First name</th>
          <th>Last name</th>
          <th>Community</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(child, index) in children" :key="index">
          <td>{{ child.first_name }}</td>
          <td>{{ child.last_name }}</td>
          <td>{{ child.community.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup(props) {
    const children = ref([]);

    const fetchChildren = async (communityId) => {
      try {
        const BASE_URL = 'http://localhost:8000';
        const response = await axios.get(`${BASE_URL}/children`);
        children.value = response.data;
      } catch (error) {
        console.error('Error fetching children:', error);
      }
    };

    onMounted(() => {
      fetchChildren(props.communityId);
    });

    return {
      children
    };
  },
  props: {
    communityId: {
      type: Number,
      required: true
    }
  }
};
</script>
