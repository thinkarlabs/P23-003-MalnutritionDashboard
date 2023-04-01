<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="updateDonor">
        <div class="row">
          <h3 class="float-start">Edit Donor</h3>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Entity Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Entity Name"
              v-model="updatedDonor.name"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Name"
              v-model="updatedDonor.contactperson"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Email ID</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Email Address"
              v-model="updatedDonor.email"
            />
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Phone No</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Phone Number"
              v-model="updatedDonor.phone"
            />
          </div>

          <div class="row">
            <div class="col-12 p-2">
              <button
                type="submit"
                class="btn btn-primary float-end mx-2"
                data-nav="admin.donors"
                @click="navigate"
                role="link"
              >
                Save
              </button>
              <router-link to="/donors" custom v-slot="{ navigate }">
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.donors"
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
import { useDonorsStore } from "../../stores/donors";
import { useRoute } from "vue-router";
import router from "../../router";

let updatedDonor = reactive({
  id: "",
  name: "",
  contactperson: "",
  email: "",
  phone: 0,
});

const route = useRoute();
const store = useDonorsStore();

updatedDonor = computed(() => {
  if (store.donor) {
    return store.donor;
  } else {
    return {
      id: "",
      name: "",
      contactperson: "",
      email: "",
      phone: "",
    };
  }
});
onMounted(async () => {
  console.log("Editing Donor.... ");
  console.log(route.params.id);
  await store.getDonor(route.params.id);
  console.log(store.donor);
});

const updateDonor = async () => {
  await store.updateDonor(updatedDonor);
  return router.push("/donors");
};
</script>
