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
  <div
    class="bg-white"
    style="max-width: 475px; margin-left: auto; margin-right: auto"
  >
    <RouterView />
  </div>
</template>

<style scoped></style>
