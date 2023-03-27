<template>
    <div class="full-div container" style="width: 1280px">
      <div id="x-contest" class="container-fluid p-3">
        <form @submit.prevent="updateSupplement">
          <div class="row">
            <h3 class="float-start">Update Supplement</h3>
  
            <div class="col-12 my-2">
              <label for="exampleFormControlInput1">Title</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder=""
                v-model="updatedSupplement.name"
              />
            </div>
  
            <div class="col-12 my-2">
              <label for="exampleFormControlInput1">Contact Person Name</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder=""
                v-model="updatedSupplement.description"
              />
            </div>
  
            <div class="row">
              <div class="col-12 p-2">
                <button
                  type="submit"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.supplement"
                  @click="navigate"
                  role="link"
                >
                  Save
                </button>
                <router-link to="/supplementList" custom v-slot="{ navigate }">
                  <button
                    type="button"
                    class="btn btn-primary float-end mx-2"
                    data-nav="admin.supplement"
                    @click="navigate"
                    role="link"
                  >
                    Cancel
                  </button>
                </router-link>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <style>
  #x-contest {
    padding-left: 0px !important;
    padding-right: 0px !important;
  }
  #tableRow {
    font-weight: 700;
    font-size: 17px;
  }
  
  @media (max-width: 600px) {
    .full-div {
      max-width: fit-content;
    }
    .Row-styling {
      border: none;
    }
  }
  </style>
  
  <script setup>
  import { ref, onMounted, computed, reactive } from "vue";
  import { useSupplementStore } from "../stores/supplement";
  import { useRoute } from "vue-router";
  import router from "../router";
  
  let updatedSupplement = reactive({
    id: "",
    name: "",
    description: "",
  });
  
  const route = useRoute();
  const store = useSupplementStore();
  
  updatedSupplement = computed(() => {
    if (store.supplement) {
      return store.supplement;
    } else {
      return {
        id: "",
        name: "",
        description: "",
      };
    }
  });
  onMounted(async () => {
    console.log("Editing.... ");
    console.log(route.params.id);
    await store.getSupplement(route.params.id);
    console.log(store.supplement);
  });
  
  const updateSupplement = async () => {
    await store.updateSupplement(updatedSupplement);
    return router.push("/supplementList");
  };
  </script>
  