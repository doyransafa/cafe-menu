<template>
  <div class="container">
    <div class="row mb-2" v-for="product in products" :key="product.id">
      <ProductItem :productList="product" />
    </div>
  </div>
</template>

<script lang="ts">
import ProductItem, { type Product } from "@/components/ProductItem.vue";
import ProductsDataServices from "@/services/ProductsDataServices";

export default {
  components: {
    ProductItem,
  },
  data() {
    return {
      products: [] as Product[],
    };
  },
  methods: {
    async retriveSubProduct() {
      const id = this.$route.params.categoryName as any;
      ProductsDataServices.getSubCategory(id)
        .then((response) => (this.products = response.data))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    this.retriveSubProduct();
  },
};
</script>

<style></style>
