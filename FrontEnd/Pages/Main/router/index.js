import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../../../src/views/DashboardView.vue";
import PageNotFound from "../../../src/views/PageNotFoundView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/pages/main/"),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: DashboardView,
      children: [
        {
          path: "/ngos",
          name: "ngoslist",
          component: () => import("../../../src/views/NgosView.vue"),
        },
      ],
    },
    {
      path: "/ngosddd",
      name: "ngoslist",
      component: () => import("../../../src/views/NgosView.vue"),
    },
    {
      path: "/addngoo",
      name: "addngo",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../../../src/views/AddNgoView.vue"),
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

router.beforeEach((to, from) => {
  debugger;
  console.log(to);
  console.log(from);
});

export default router;
