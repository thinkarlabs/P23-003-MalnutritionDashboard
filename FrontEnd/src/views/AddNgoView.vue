<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postNgo">
        <div class="row">
          <h3 class="float-start">Add NGO</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">NGO Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="NGO name"
              v-model="newNgo.ngoName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Name"
              v-model="newNgo.contactPersonName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Phone</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Phone"
              v-model="newNgo.contactPersonPhone"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Email</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Email"
              v-model="newNgo.contactPersonEmail"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Password"
              v-model="newNgo.contactPersonPassword"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Location</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Location"
              v-model="newNgo.location"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Pincode</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="pincode"
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
import { useNgoStore } from "../stores/ngo";
import router from "../router";
let newNgo = reactive({
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: "",
  contactPersonPassword: "",
  location: "",
  pincode: "",
});
const store = useNgoStore();

const postNgo = async () => {
  await store.postNgo(newNgo);
  return router.push("/ngos");
};
</script>
