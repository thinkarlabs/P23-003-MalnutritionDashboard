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
      path: "/editngo/:id",
      name: "editngo",
      component: () => import("../views/EditNgoView.vue"),
    },
    {
      path: "/kidsCheckUp/:id",
      name: "kidsCheckUp",
      component: () => import("../views/kidsCheckUp.vue"),
    },
    {
      path: "/addchild",
      name: "addchild",
      component: () => import("../views/AddChildView.vue"),
    },
    {
      path: "/editchild/:id",
      name: "editchild",
      component: () => import("../views/EditChildView.vue"),
    },
    {
      path: "/ChildSupplementarySummaryView",
      name: "ChildSupplementarySummaryView",
      component: () => import("../views/ChildSupplementarySummaryView.vue"),
    },
    {
      path: "/addAanganwadi",
      name: "addAanganwadi",
      component: () => import("../views/AddAanganwadi.vue"),
    },
    {
      path: "/aanganwadiList",
      name: "aanganwadiList",
      component: () => import("../views/AanganwadiList.vue"),
    },
    {
      path: "/editAanganwadiPage/:id",
      name: "aanganwadi-details",
      component: () => import("../views/EditAanganwadi.vue")
    },
    {
      path: "/addSupplement",
      name: "addSupplement",
      component: () => import("../views/AddSupplement.vue"),
    },
    {
      path: "/supplementList",
      name: "supplementList",
      component: () => import("../views/SupplementList.vue"),
    },
    {
      path: "/editSupplement/:id",
      name: "editSupplementPage",
      component: () => import("../views/EditSupplement.vue")
    },
    {
      path: "/addDonor",
      name: "addDonor",
      component: () => import("../views/AddDonor.vue")
    },
    {
      path: "/donorsList",
      name: "donorsList",
      component: () => import("../views/DonorsList.vue")
    },
    {
      path: "/editDonor/:id",
      name: "editDonor",
      component: () => import("../views/EditDonor.vue")
    },
    {
      path: "/program",
      name: "Program",
      component: () => import("../views/Program.vue"),
    },
    {
      path: "/programlist",
      name: "programlist",
      component: () => import("../views/programlist.vue"),
    },
    {
      path: "/editProgram/:id",
      name: "program-edit",
      component: () => import("../views/EditProgram.vue")
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
