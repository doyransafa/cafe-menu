<script lang="ts">
import HeaderMenu from "@/components/HeaderMenu.vue";
import CategoryList from "@/components/List/CategoryList.vue";
import SearchBar from "@/components/SearchBar.vue";
import axios from "axios";

export default {
  components: {
    HeaderMenu,
    CategoryList,
    SearchBar,
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
        const response = await axios.get(`/products/?search=${searchTerm}`);
        this.searchResults = response.data;
      } catch (error) {
        console.error("Arama hatası:", error);
      }
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
          <h1>BigCheff Menuasasdfasdf</h1>
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
          <div class="form">
            <i class="fa fa-search"></i>
            <input
              type="text"
              class="form-control form-input"
              placeholder="Search Menu..."
            />
          </div>
          <SearchBar @search="performSearch" />
        </div>
      </div>

      <div class="row mt-4">
        <div class="col">
          {{ searchResults }}
          <CategoryList />
        </div>
      </div>
    </div>
  </main>
</template>

<style>
.margin-negative {
  margin-top: -30px;
}

.form {
  position: relative;
}

.form .fa-search {
  position: absolute;
  top: 20px;
  left: 20px;
  color: #9ca3af;
}

.form span {
  position: absolute;
  right: 17px;
  top: 13px;
  padding: 2px;
  border-left: 1px solid #d1d5db;
}

.left-pan {
  padding-left: 7px;
}

.left-pan i {
  padding-left: 10px;
}

.form-input {
  height: 55px;
  text-indent: 33px;
  border-radius: 10px;
}

.form-input:focus {
  box-shadow: none;
  border: none;
}
</style>
