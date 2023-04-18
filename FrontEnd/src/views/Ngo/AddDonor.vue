<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postDonor">
        <div class="row">
          <h3 class="float-start">Manage Donor</h3>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Entity Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Entity name"
              v-model="newDonor.name"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.name">
              {{ helperSupport.name }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Contact Person</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Name of Contact Person"
              v-model="newDonor.contactperson"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonName">
              {{ helperSupport.contactPersonName }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Email ID</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Email Address"
              v-model="newDonor.email"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonEmail">
              {{ helperSupport.contactPersonEmail }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1">Phone No</label>
            <input
              type="number"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Phone Number"
              v-model="newDonor.phone"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonPhone">
              {{ helperSupport.contactPersonPhone }}
            </div>
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
import router from "../../router";
import helper from "../../helper/validation.helper.js";

let newDonor = reactive({
  name: "",
  contactperson: "",
  email: "",
  phone: "",
});

const store = useDonorsStore();
const helperSupport = reactive({
  name: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: "",
});

const isValidSubmission = (newDonor) => {
  helperSupport.name = helper.validateName(newDonor.name);
  helperSupport.contactPersonName = helper.validateName(newDonor.contactperson);
  helperSupport.contactPersonEmail = helper.validateEmail(newDonor.email);
  helperSupport.contactPersonPhone = helper.validatePhoneNumber(newDonor.phone);
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

const postDonor = async () => {
  if (isValidSubmission(newDonor) == true) {
  await store.postDonor(newDonor);
  return router.push("/donors");
  }
};
</script>
