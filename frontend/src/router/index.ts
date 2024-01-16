import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BlankLayout from "@/layout/BlankLayout.vue";
import MenuLayout from "@/layout/MenuLayout.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "blank",
      component: BlankLayout,
      children: [
        {
          path: "",
          name: "home",
          component: HomeView,
        },
        {
          path: "/about",
          name: "about",
          component: () => import("../views/AboutView.vue"),
        },
      ],
    },
    {
      path: "/menu",
      name: "",
      component: MenuLayout,
      children: [
        {
          path: "",
          name: "menu-list",
          component: () => import("@/components/List/CategoryList.vue"),
        },
        {
          path: ":categoryName",
          name: "menu-detail",
          component: () => import("@/components/List/ProductList.vue"),
        },
      ],
    },
  ],
});

export default router;
