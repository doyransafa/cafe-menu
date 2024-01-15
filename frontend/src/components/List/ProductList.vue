<template>
  <div class="container">
    <div class="row mb-2" v-for="product in products" :key="product.id">
      <ProductItem :productList="product" />
    </div>
  </div>
</template>

<script lang="ts">
import ProductItem from "@/components/ProductItem.vue";
import products from "@/mock/products";

export default {
  components: {
    ProductItem,
  },
  data() {
    return {
      products,
    };
  },
};
</script>

<style></style>
