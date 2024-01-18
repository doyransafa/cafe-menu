<template>
  <div>
    <ul class="nav nav-tabs nav-fill">
      <li v-for="category in categories" :key="category.id" class="nav-item">
        <router-link
          :to="{ name: 'categories', params: { categories: category.id } }"
          class="nav-link"
          aria-current="page"
          >{{ category.name }}</router-link
        >
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CategoryDataServices from "@/services/CategoryDataServices";

type Category = {
  id: number;
  name: string;
};

export default defineComponent({
  data() {
    return {
      categories: [] as Category[],
    };
  },
  methods: {
    async retriveCategories() {
      const response = await CategoryDataServices.getAll();
      this.categories = response.data;
    },
  },
  mounted() {
    this.retriveCategories();
  },
});
</script>
