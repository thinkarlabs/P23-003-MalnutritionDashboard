<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="updateAanganwadi">
        <div class="row">
          <h3 class="float-start">Edit Aanganwadi</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">Aanganwadi Contact Person</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Aanganwadi Contact Person"
              v-model="updatedAanganwadi.contactPersonName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Phone</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Phone Number"
              v-model="updatedAanganwadi.contactPersonPhone"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Password"
              v-model="updatedAanganwadi.contactPersonPassword"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Location</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Location"
              v-model="updatedAanganwadi.location"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Latitude, Longitude Coordinates</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Latitude, Longitude Coordinates"
              v-model="updatedAanganwadi.coordinates"
            />
          </div>
          <div class="row">
            <div class="col-12 p-2">
              <button
                type="submit"
                class="btn btn-primary float-end mx-2"
                data-nav="admin.aanganwadis"
                @click="navigate"
                role="link"
              >
                Save
              </button>
              <router-link to="/aanganwadiList" custom v-slot="{ navigate }">
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.aanganwadis"
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
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  
  <script setup>
  import { ref, onMounted, computed, reactive } from "vue";
  import { useAanganwadiStore } from "../stores/aanganwadi";
  import router from "../router";
  import axios from "axios";
  import { useRoute } from "vue-router";

  const route = useRoute();

  let updatedAanganwadi = reactive({
    aanganwadiName: "",
    contactPersonName: "",
    contactPersonEmail: "",
    contactPersonPhone:"",
    contactPersonPassword: "",
    taluka: "",
    coordinates: "",
    taluka:"",
    pincode:0
  });

  const store = useAanganwadiStore();

  updatedAanganwadi = computed(() => {
    if(store.currentAanganwadi){
      return store.currentAanganwadi;
    }else{
      return{
        id: "",
        aanganwadiName: "",
        contactPersonName: "",
        contactPersonEmail: "",
        contactPersonPhone:"",
        contactPersonPassword: "",
        taluka: "",
        coordinates: "",
        taluka:"",
        pincode:0
      };
    }
  });
  
  onMounted(async () => {
    console.log("Aanganwadi ID :: "+route.params.id);
    await store.getAanganwadi(route.params.id);
    console.log(store.currentAanganwadi);
  });
  
  const updateAanganwadi = async () => {
    await store.updateAanganwadi(updatedAanganwadi);
    return router.push("/aanganwadiList");
  };
  </script>
