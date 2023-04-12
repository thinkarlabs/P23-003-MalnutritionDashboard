<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form v-on:submit.prevent="updateNgo">
        <div class="row">
          <h3 class="float-start">Manage NGO</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">NGO Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Ngo Name"
              v-model="updatedNgo.ngoName"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.ngoName">
              {{ helperSupport.ngoName }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Name"
              v-model="updatedNgo.contactPersonName"
            />
            <div
              className="text-danger mrgnbtn"
              v-if="helperSupport.contactPersonName"
            >
              {{ helperSupport.contactPersonName }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Phone</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Phone"
              v-model="updatedNgo.contactPersonPhone"
            />
            <div
              className="text-danger mrgnbtn"
              v-if="helperSupport.contactPersonPhone"
            >
              {{ helperSupport.contactPersonPhone }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person Email</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Contact Person Email"
              v-model="updatedNgo.contactPersonEmail"
            />
            <div
              className="text-danger mrgnbtn"
              v-if="helperSupport.contactPersonEmail"
            >
              {{ helperSupport.contactPersonEmail }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1"
              >Contact Person Password</label
            >
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Password"
              v-model="updatedNgo.contactPersonPassword"
            />
            <div
              className="text-danger mrgnbtn"
              v-if="helperSupport.contactPersonPassword"
            >
              {{ helperSupport.contactPersonPassword }}
            </div>
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Location</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Location"
              v-model="updatedNgo.location"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.location">
              {{ helperSupport.location }}
            </div>
          </div>
          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Pincode</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="pincode"
              v-model="updatedNgo.pincode"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.pincode">
              {{ helperSupport.pincode }}
            </div>
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
import { useRoute } from "vue-router";
import router from "../router";
import helper from "../helper/validation.helper.js";

let updatedNgo = reactive({
  id: "",
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: "",
  contactPersonPassword: "",
  location: "",
  pincode: "",
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
      contactPersonPhone: "",
      contactPersonPassword: "",
      location: "",
      pincode: "",
    };
  }
});

const helperSupport = reactive({
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: "",
  contactPersonPassword: "",
  location: "",
  pincode: "",
});

const isValidSubmission = (updatedNgo) => {
  helperSupport.pincode = helper.validatePincode(updatedNgo._value.pincode);
  helperSupport.contactPersonName = helper.validateName(
    updatedNgo._value.contactPersonName
  );
  helperSupport.contactPersonEmail = helper.validateEmail(
    updatedNgo._value.contactPersonEmail
  );
  helperSupport.ngoName = helper.validateName(updatedNgo._value.ngoName);
  helperSupport.contactPersonPhone = helper.validatePhoneNumber(
    updatedNgo._value.contactPersonPhone
  );
  helperSupport.location = helper.validateName(updatedNgo._value.location);
  helperSupport.contactPersonPassword =
    updatedNgo._value.contactPersonPassword !== ""
      ? ""
      : "Password is mandatory";
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

onMounted(async () => {
  console.log("Editing.... ");
  console.log(route.params.id);
  await store.getNgo(route.params.id);
  console.log(store.ngo);
});

const updateNgo = async () => {
  if (isValidSubmission(updatedNgo) == true) {
    await store.updateNgo(updatedNgo);
    return router.push("/ngos");
  }
};
</script>
