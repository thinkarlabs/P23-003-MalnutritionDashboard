import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue";
import PageNotFound from "../views/PageNotFoundView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: DashboardView,
    },
    {
      path: "/ngos",
      name: "ngoslist",
      component: () => import("../views/NgosView.vue"),
    },
    {
      path: "/addngo",
      name: "addngo",
      component: () => import("../views/AddNgoView.vue"),
    },
    {
      path: "/kidsCheckUp",
      name:"kidsCheckUp",
      component: () => import("../views/kidsCheckUp.vue"),
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
