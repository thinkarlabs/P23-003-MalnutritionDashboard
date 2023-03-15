import { createRouter, createWebHistory } from "vue-router";
import AddKidView from "../views/AddKidView.vue";
import PageNotFound from "../views/PageNotFoundView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/pages/pwa/",
      name: "addkidview",
      component: AddKidView,
    },
    {
      path: "/addkid",
      name: "addkid",
      component: () => import("../views/AddKidView.vue"),
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
