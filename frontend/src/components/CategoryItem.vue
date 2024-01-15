<template>
  <router-link
    class="link-underline"
    :to="{ name: 'menu-item', params: { categoryName: categoryItem.id } }"
  >
    <div
      :style="{
        backgroundImage: 'url(' + categoryItem.img + ')',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundColor: 'black',
        height: '160px',
      }"
      class="rounded-4 position-relative overflow-hidden"
    >
      <div class="background-overlay"></div>

      <div class="h-100 text-center">
        <h1
          class="text-light d-flex h-100 text-center position-relative align-items-center justify-content-center"
        >
          {{ categoryItem.name }}
        </h1>
      </div>
    </div>
  </router-link>
</template>

<script lang="ts">
type Category = {
  id: number;
  name: string;
  img: string;
};

import { defineComponent } from "vue";

export default defineComponent({
  props: {
    categoryItem: {
      type: Object as () => Category,
      required: true,
    },
  },
});
</script>

<style>
a:link {
  text-decoration: none;
}

.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Ön plan rengi burada ayarlanabilir */
}
</style>
