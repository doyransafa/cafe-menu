<template>
  <div>
    <div class="row mb-3" v-for="category in subcategories" :key="category.id">
      <CategoryItem :categoryItem="category" />
    </div>
  </div>
</template>
<script lang="ts">
import SubCategoryDataService from "../../services/SubCategoryDataServices";
import CategoryItem, { type Category } from "../CategoryItem.vue";

export default {
  components: {
    CategoryItem,
  },
  data() {
    return {
      subcategories: [] as Category[],
    };
  },
  methods: {
    async retriveAllSubCategories() {
      SubCategoryDataService.getAll().then((response) => {
        this.subcategories = response.data;
      });
    },
  },
  mounted() {
    this.retriveAllSubCategories();
  },
};
</script>
<style></style>
