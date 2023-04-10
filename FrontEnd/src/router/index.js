import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue";
import PageNotFound from "../views/PageNotFoundView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "loginweb",
      component: () => import("../views/LoginWebView.vue"),
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashboardView,
    },
    {
      path: "/ngos",
      name: "ngoslist",
      component: () => import("../views/Admin/NgosView.vue"),
    },
    {
      path: "/addngo",
      name: "addngo",
      component: () => import("../views/Admin/AddNgoView.vue"),
    },
    {
      path: "/editngo/:id",
      name: "editngo",
      component: () => import("../views/Admin/EditNgoView.vue"),
    },

    {
      path: "/addaanganwadi",
      name: "addAanganwadi",
      component: () => import("../views/Admin/AddAanganwadi.vue"),
    },
    {
      path: "/aanganwadis",
      name: "aanganwadiList",
      component: () => import("../views/Admin/AanganwadiList.vue"),
    },
    {
      path: "/editaanganwadipage/:id",
      name: "aanganwadi-details",
      component: () => import("../views/Admin/EditAanganwadi.vue"),
    },
    {
      path: "/addsupplement",
      name: "addSupplement",
      component: () => import("../views/Ngo/AddSupplement.vue"),
    },
    {
      path: "/supplements",
      name: "supplementList",
      component: () => import("../views/Ngo/SupplementList.vue"),
    },
    {
      path: "/editsupplement/:id",
      name: "editSupplementPage",
      component: () => import("../views/Ngo/EditSupplement.vue"),
    },
    {
      path: "/adddonor",
      name: "addDonor",
      component: () => import("../views/Ngo/AddDonor.vue"),
    },
    {
      path: "/donors",
      name: "donorsList",
      component: () => import("../views/Ngo/DonorsList.vue"),
    },
    {
      path: "/editdonor/:id",
      name: "editDonor",
      component: () => import("../views/Ngo/EditDonor.vue"),
    },
    {
      path: "/addprogram",
      name: "Program",
      component: () => import("../views/Ngo/AddProgram.vue"),
    },
    {
      path: "/programs",
      name: "programlist",
      component: () => import("../views/Ngo/programlist.vue"),
    },
    {
      path: "/editprogram/:id",
      name: "program-edit",
      component: () => import("../views/Ngo/EditProgram.vue"),
    },
    {
      path: "/programssummary",
      name: "programssummaryview",
      component: () => import("../views/Aaganwadi/ProgramsSummaryView.vue"),
    },
    {
      path: "/supplementsupply/:program_joining_id",
      name: "SupplementSupplyView",
      component: () => import("../views/Aaganwadi/SupplementSupplyView.vue"),
    },
    {
      path: "/childsupplementarysummary",
      name: "ChildSupplementarySummaryView",
      component: () =>
        import("../views/Aaganwadi/ChildSupplementarySummaryView.vue"),
    },
    {
      path: "/addchild",
      name: "addchild",
      component: () => import("../views/Aaganwadi/AddChildView.vue"),
    },
    {
      path: "/editchild/:id",
      name: "editchild",
      component: () => import("../views/Aaganwadi/EditChildView.vue"),
    },
    {
      path: "/kidsCheckUp/:id",
      name: "kidsCheckUp",
      component: () => import("../views/Aaganwadi/kidsCheckUp.vue"),
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
