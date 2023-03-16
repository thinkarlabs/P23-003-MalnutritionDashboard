<template>
    <div class="container-md mt-5 p-3">
      <div id="x-contest" class="container-float">
        <div class="row">
          <h3 class="float-start">Edit Aanganwadi</h3>
          <form @submit.prevent="updateAanganwadi">
            <div class="col-12 my-2">
              <label for="exampleFormControlInput1">Aanganwadi Contact Person</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Contact Person"
                v-model="currentAanganwadi.aanganwadiName"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Contact Phone</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Phone Number"
                v-model="currentAanganwadi.contactPersonPhone"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Password</label>
              <input
                type="password"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Password"
                v-model="currentAanganwadi.contactPersonPassword"
              />
            </div>
  
            <div class="col-6 my-2">
              <label for="exampleFormControlInput1">Location</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Aanganwadi Location"
                v-model="currentAanganwadi.location"
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
                v-model="currentAanganwadi.coordinates"
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
                  Update
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
    <div v-if="loading">Loading...</div>

    <div
      v-for="currency in info"
      class="currency"
    >
      {{ currency.description }}:
      <span class="lighten">
        <span v-html="currency.symbol"></span>{{ currency.rate_float | currencydecimal }}
      </span>
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
  let dummyAanganwadi = reactive({
    aanganwadiName: "",
    contactPersonName: "",
    contactPersonPhone: 123,
    contactPersonEmail:"",
    contactPersonPassword: "",
    location: "",
    coordinates: "",
    taluka:"",
    pincode:6162
  });

  const store = useAanganwadiStore();

  const currentAanganwadi = computed(() => {
    return store.getAanganwadi('640ebc4714851ef5da2d6741');
  });
  
  onMounted(() => {
    dummyAanganwadi = store.getAanganwadi('640ebc4714851ef5da2d6741');
    console.log(JSON.stringify(store.getAanganwadi('640ebda1a8a7361eebae63bd')));
  });
  
  const updateAanganwadi = () => {
    store.updateAanganwadi(aanganwadi);
    return router.push("/aanganwadiList");
  };
  
  </script>
  