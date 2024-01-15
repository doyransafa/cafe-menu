<template>
  <div>
    <div class="row mb-3" v-for="category in categorys" :key="category.id">
      <CategoryItem :categoryItem="category" />
    </div>
  </div>
</template>
<script lang="ts">
import CategoryItem from "../CategoryItem.vue";
import categorys from "@/mock/categorys";

export default {
  components: {
    CategoryItem,
  },
  data() {
    return {
      categorys,
    };
  },
};
</script>
<style></style>
