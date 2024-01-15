<template>
  <div>
    <div :class="{ 'opacity-25': !productList.availability }" class="card">
      <img
        :src="productList.img"
        class="card-img-top"
        alt="menuListImage"
        style="height: 12rem; object-fit: cover"
      />
      <div class="card-body">
        <div class="row mb-2">
          <div class="col">
            <h3 class="card-title lh-1 mb-0">{{ productList.name }}</h3>
            <p class="card-text text-secondary">
              {{ productList.description }}
            </p>
          </div>
        </div>
        <div class="row align-items-center">
          <div class="col-10">
            <span class="fs-3">{{ productList.price }}</span>
            <span>$</span>
          </div>
          <div class="col-2">
            <button class="btn btn-primary ml-auto">+</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

type Product = {
  id: number;
  img: string;
  name: string;
  description: string;
  price: number;
  availability: boolean;
};

export default defineComponent({
  props: {
    productList: {
      type: Object as () => Product,
      required: true,
    },
  },
});
</script>
