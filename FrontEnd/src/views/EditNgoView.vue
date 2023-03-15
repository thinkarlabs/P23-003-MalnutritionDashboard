<template>
  <div class="container-md mt-5 p-3">
    <div id="x-contest" class="container-float">
      <div class="row">
        <h3 class="float-start">Manage NGO</h3>
        <form @submit.prevent="updateNgo">
          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">NGO Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="updatedNgo.ngoName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="updatedNgo.contactPersonName"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Phone</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="updatedNgo.contactPersonPhone"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Email</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="updatedNgo.contactPersonEmail"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Password</label>
            <input
              class="form-control"
              id="exampleFormControlInput1"
              placeholder=""
              v-model="updatedNgo.contactPersonPassword"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Location</label>
            <input
              class="form-control"
              id="exampleFormControlInput1"
              v-model="updatedNgo.location"
            />
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Pincode</label>
            <input
              class="form-control"
              id="exampleFormControlInput1"
              v-model="updatedNgo.pincode"
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
#main-Container {
  margin-top: -10rem;
}
@media (max-width: 400px) {
  #main-Container {
    margin-top: 3rem;
  }
}
</style>

<script setup>
import { ref, onMounted, computed, reactive } from "vue";
import { useNgoStore } from "../stores/ngo";
import { useRoute } from "vue-router";
import router from "../router";

let updatedNgo = reactive({
  id: "",
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: 0,
  contactPersonPassword: "",
  location: "",
  pincode: 0,
});

const route = useRoute();
const store = useNgoStore();

updatedNgo = computed(() => {
  if (store.ngo) {
    return store.ngo;
  } else {
    return {
      id: "",
      ngoName: "",
      contactPersonName: "",
      contactPersonEmail: "",
      contactPersonPhone: 0,
      contactPersonPassword: "",
      location: "",
      pincode: 0,
    };
  }
});
onMounted(async () => {
  console.log("Editing.... ");
  console.log(route.params.id);
  await store.getNgo(route.params.id);
  console.log(store.ngo);
});

const updateNgo = async () => {
  await store.updateNgo(updatedNgo);
  return router.push("/ngos");
};
</script>
