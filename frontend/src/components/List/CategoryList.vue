<template>
  <div>
    <div
      class="row mb-3"
      v-for="category in subcategories.sub_categories"
      :key="category.id"
    >
      <CategoryItem :categoryItem="category" />
    </div>
  </div>
</template>
<script lang="ts">
import CategoryDataService from "../../services/CategoryDataServices";
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
      const id = this.$route.params.categories;
      CategoryDataService.get(id).then((response) => {
        this.subcategories = response.data;
      });
    },
  },

  watch: {
    "$route.params.categories": "retriveAllSubCategories",
  },

  mounted() {
    this.retriveAllSubCategories();
  },
};
</script>
<style></style>
