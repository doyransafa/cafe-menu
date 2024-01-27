<script lang="ts">
import CategoryTabs from "@/components/CategoryTabs.vue";
import HeaderMenu from "@/components/HeaderMenu.vue";
import MenuSearchBar from "@/components/MenuSearchBar.vue";
import ProductItem from "@/components/ProductItem.vue";
import axios from "axios";

export default {
  components: {
    HeaderMenu,
    CategoryTabs,
    MenuSearchBar,
    ProductItem,
  },
  data() {
    return {
      searchResults: [],
    };
  },
  methods: {
    async performSearch(searchTerm: any) {
      try {
        // Backend API'ye isteği gönder
        const response = await axios.get(
          `http://localhost:8000/products/?search=${searchTerm}`
        );
        this.searchResults = response.data;
      } catch (error) {
        console.error("Arama hatası:", error);
      }
    },
    clearSearchResults() {
      // Arama terimi boşaltıldığında mevcut sonuçları temizle
      this.searchResults = [];
    },
  },
};
</script>

<template>
  <HeaderMenu />
  <main>
    <div class="container margin-negative">
      <div class="row">
        <div class="col bg-white rounded-4 pt-3">
          <h1>BigCheff Menu</h1>
          <div>
            <div class="d-flex flex-wrap gap-2">
              <div>asdfsadf</div>
              <div>asdfasdf</div>
              <div>asdfasdfasd</div>
            </div>

            <div style="font-size: 14px">
              <p>
                Here you can add additional information for your guests, like
                taxes, service fees, restaurant working hours, contacts,
                delivery terms, general QR code menu information, and so on
              </p>
              <p>You can also add spacings</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <CategoryTabs />
        </div>
      </div>

      <div class="row">
        <div class="col">
          <MenuSearchBar
            @search="performSearch"
            @clearSearch="clearSearchResults"
          />
        </div>
      </div>

      <div class="row mt-3">
        <div
          class="mb-2"
          v-for="searchResult in searchResults"
          :key="searchResult.id"
        >
          <ProductItem :productList="searchResult" />
        </div>
      </div>

      <div class="row mt-4">
        <div class="col">
          <RouterView />
        </div>
      </div>
    </div>
  </main>
</template>

<style>
.margin-negative {
  margin-top: -30px;
}
</style>
