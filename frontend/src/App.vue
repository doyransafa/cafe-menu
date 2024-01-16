<script lang="ts">
import { RouterView } from "vue-router";


export default {
  data() {
    return {
      categories: [],
    };
  },
  components: {
    RouterView,
  },
 
};
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
