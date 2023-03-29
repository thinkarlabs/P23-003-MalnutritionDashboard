<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postAanganwadi">
        <div class="row">
          <h3 class="float-start">Add Aanganwadi</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">Aanganwadi Contact Person</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Aanganwadi Contact Person"
              v-model="aanganwadi.contactPersonName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Phone</label>
            <input
              type="number"
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
              placeholder="Location"
              v-model="aanganwadi.location"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Latitude, Longitude Coordinates</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Latitude, Longitude Coordinates"
              v-model="aanganwadi.location_coordinates"
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
              <router-link to="/aanganwadis" custom v-slot="{ navigate }">
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
let aanganwadi = reactive({
  aanganwadiName: "",
  contactPersonName: "",
  contactPersonPhone: "",
  contactPersonEmail: "",
  contactPersonPassword: "",
  location: "",
  location_coordinates: "",
  pincode: 0,
});
const store = useAanganwadiStore();

const postAanganwadi = () => {
  store.postAanganwadi(aanganwadi);
  return router.push("/aanganwadis");
};
</script>
