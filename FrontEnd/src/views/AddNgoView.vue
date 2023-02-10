<template>
  <div class="container-md mt-5 p-3">
    <div id="x-contest" class="container-float">
      <div class="row">
        <h3 class="float-start">Manage NGO</h3>
        <form @submit.prevent="postNgo">
          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">NGO Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.ngoName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.contactPersonName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Phone</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.contactPersonPhone"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Email</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.contactPersonEmail"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1"
              >Contact Person Password</label
            >
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.contactPersonPassword"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Location</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.location"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Pincode</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="newNgo.pincode"
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
              <router-link to="/ngos" custom v-slot="{ navigate }">
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
import { useNgoStore } from "../stores/ngo";
import router from "../router";
let newNgo = reactive({
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: 0,
  contactPersonPassword: "",
  location: "",
  pincode: 0,
});
const store = useNgoStore();

const postNgo = () => {
  store.postNgo(newNgo);
  return router.push("/ngos");
};
</script>
