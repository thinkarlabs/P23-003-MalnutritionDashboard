<template>
    <div class="container-md mt-5 p-3">
      <div id="x-contest" class="container-float">
        <div class="row">
          <h3 class="float-start">Manage Aanganwadi</h3>
          <form @submit.prevent="postAanganwadi">
            <div class="col-12 my-2">
              <label for="exampleFormControlInput1">Aanganwadi Contact Person</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Contact Person"
                v-model="aanganwadi.contactPersonName"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Contact Phone</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Phone Number"
                v-model="aanganwadi.contactPersonPhone"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Password</label>
              <input
                type="password"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Password"
                v-model="aanganwadi.contactPersonPassword"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Location</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Aanganwadi Location"
                v-model="aanganwadi.location"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1"
                >Latitude, Longitude Coordinates</label
              >
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Latitude, Longitude Coordinates"
                v-model="aanganwadi.coordinates"
              />
            </div>
            
            
            <div class="row">
              <div class="col-12 p-2">
                <button
                  type="submit"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.ngos"
                  @click="navigate"
                  role="link"
                >
                  Save
                </button>
                <router-link to="/aanganwadiList" custom v-slot="{ navigate }">
                  <button
                    type="button"
                    class="btn btn-primary float-end mx-2"
                    data-nav="admin.ngos"
                    @click="navigate"
                    role="link"
                  >
                    Cancel
                  </button>
                </router-link>
              </div>
            </div>
          </form>
        </div>
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
  let aanganwadi = reactive({
    aanganwadiName: "Test",
    contactPersonName: "",
    contactPersonPhone: 0,
    contactPersonEmail:"dummy@hotmail.com",
    contactPersonPassword: "",
    location: "",
    //coordinates: "",
    taluka:"Test Taluka",
    pincode:616263
  });
  const store = useAanganwadiStore();
  
  const postAanganwadi = () => {
    store.postAanganwadi(aanganwadi);
    return router.push("/aanganwadiList");
  };
  </script>
  