<!-- SearchBar.vue -->
<template>
  <div><input v-model="searchTerm" @input="search" />asdfasdf</div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      searchTerm: "",
    };
  },
  methods: {
    search() {
      // Arama terimini kullanarak backend API'yi çağırabilirsiniz
      this.$emit("search", this.searchTerm);
    },
  },
};
</script>
