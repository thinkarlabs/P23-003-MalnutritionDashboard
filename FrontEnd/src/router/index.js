import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue";
import PageNotFound from "../views/PageNotFoundView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/login",
      name: "loginweb",
      component: () => import("../views/LoginWebView.vue"),
    },
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
      path: "/childsupplementarysummary",
      name: "ChildSupplementarySummaryView",
      component: () => import("../views/ChildSupplementarySummaryView.vue"),
    },
    {
      path: "/addaanganwadi",
      name: "addAanganwadi",
      component: () => import("../views/AddAanganwadi.vue"),
    },
    {
      path: "/aanganwadis",
      name: "aanganwadiList",
      component: () => import("../views/AanganwadiList.vue"),
    },
    {
      path: "/editaanganwadipage/:id",
      name: "aanganwadi-details",
      component: () => import("../views/EditAanganwadi.vue"),
    },
    {
      path: "/programssummary",
      name: "programssummaryview",
      component: () => import("../views/ProgramsSummaryView.vue"),
    },
    {
      path: "/supplementsupply/:program_joining_id",
      name: "SupplementSupplyView",
      component: () => import("../views/SupplementSupplyView.vue"),
    },
    {
      path: "/addsupplement",
      name: "addSupplement",
      component: () => import("../views/AddSupplement.vue"),
    },
    {
      path: "/supplements",
      name: "supplementList",
      component: () => import("../views/SupplementList.vue"),
    },
    {
      path: "/editsupplement/:id",
      name: "editSupplementPage",
      component: () => import("../views/EditSupplement.vue"),
    },
    {
      path: "/adddonor",
      name: "addDonor",
      component: () => import("../views/AddDonor.vue"),
    },
    {
      path: "/donors",
      name: "donorsList",
      component: () => import("../views/DonorsList.vue"),
    },
    {
      path: "/editdonor/:id",
      name: "editDonor",
      component: () => import("../views/EditDonor.vue"),
    },
    {
      path: "/addprogram",
      name: "Program",
      component: () => import("../views/AddProgram.vue"),
    },
    {
      path: "/programs",
      name: "programlist",
      component: () => import("../views/programlist.vue"),
    },
    {
      path: "/editprogram/:id",
      name: "program-edit",
      component: () => import("../views/EditProgram.vue"),
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
