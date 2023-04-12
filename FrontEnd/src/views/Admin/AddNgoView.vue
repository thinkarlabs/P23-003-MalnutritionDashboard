<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form v-on:submit.prevent="postNgo">
        <div class="row">
          <h3 class="float-start">Add NGO</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">NGO Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Ngo Name"
              v-model="newNgo.ngoName"
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
              v-model="newNgo.contactPersonName"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonName">
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
              v-model="newNgo.contactPersonPhone"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonPhone">
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
              v-model="newNgo.contactPersonEmail"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.contactPersonEmail">
              {{ helperSupport.contactPersonEmail }}
            </div>
          </div>

          <div class="col-6 my-2">
            <label for="exampleFormControlInput1"
              >Contact Person Password</label
            >
            <input
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Password"
              v-model="newNgo.contactPersonPassword"
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
              v-model="newNgo.location"
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
              v-model="newNgo.pincode"
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

<script setup>
import { reactive } from "vue";
import { useNgoStore } from "../../stores/ngo.js";
import router from "../../router";
import helper from "../../helper/validation.helper.js";
let newNgo = reactive({
  ngoName: "",
  contactPersonName: "",
  contactPersonEmail: "",
  contactPersonPhone: "",
  contactPersonPassword: "",
  location: "",
  pincode: "",
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
const store = useNgoStore();

const isValidSubmission = (newNgo) => {
  helperSupport.pincode = helper.validatePincode(newNgo.pincode);
  helperSupport.contactPersonName = helper.validateName(newNgo.contactPersonName);
  helperSupport.contactPersonEmail = helper.validateEmail(newNgo.contactPersonEmail);
  helperSupport.ngoName = helper.validateName(newNgo.ngoName);
  helperSupport.contactPersonPhone = helper.validatePhoneNumber(
    newNgo.contactPersonPhone
  );
  helperSupport.location = helper.validateName(newNgo.location);
  helperSupport.contactPersonPassword =
    newNgo.contactPersonPassword !== "" ? "" : "Password is mandatory";
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

const postNgo = async () => {
  if (isValidSubmission(newNgo) == true) {
    await store.postNgo(newNgo);
    return router.push("/ngos");
  }
};
</script>

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
<<<<<<< HEAD:FrontEnd/src/views/Admin/AddNgoView.vue
=======

<script setup>
import { ref, onMounted, computed, reactive, watch } from "vue";
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

let msg = reactive([]);

const postNgo = async () => {
  let validationRegex = {
    name: /^[a-zA-Z]+(\s[a-zA-Z]+)?$/,
    pincode: /^[0-9]{6}$/,
    number: /^([+]\d{2})?\d{10}$/,
    email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  };

  if (newNgo.pincode.match(validationRegex.pincode)) {
    msg["pincode"] = "";
  } else {
    msg["pincode"] = "Please entered valid pincode";
  }
  if (newNgo.contactPersonName.match(validationRegex.name)) {
    msg["contactPersonName"] = "";
  } else {
    msg["contactPersonName"] = "Please entered a valid name";
  }
  if (newNgo.ngoName.match(validationRegex.name)) {
    msg["ngoName"] = "";
  } else {
    msg["ngoName"] = "Please entered a valid name";
  }
  if (newNgo.location.match(validationRegex.name)) {
    msg["location"] = "";
  } else {
    msg["location"] = "Please entered a valid name";
  }
  if (newNgo.contactPersonPhone.match(validationRegex.number)) {
    msg["phoneNumber"] = "";
  } else {
    msg["phoneNumber"] = "Please entered a valid phoneNumber";
  }

  if (newNgo.contactPersonEmail.match(validationRegex.email)) {
    msg["email"] = "";
  } else {
    msg["email"] = "Please entered a valid email";
  }
  if (
    newNgo.contactPersonEmail.match(validationRegex.email) &&
    newNgo.contactPersonPhone.match(validationRegex.number) &&
    newNgo.pincode.match(validationRegex.pincode) &&
    newNgo.contactPersonName.match(validationRegex.name) &&
    newNgo.ngoName.match(validationRegex.name) &&
    newNgo.location.match(validationRegex.name)
  ) {
    await store.postNgo(newNgo);
    return router.push("/ngos");
  }
};
</script>
>>>>>>> 6670827 (Validation_for_Ngo):FrontEnd/src/views/AddNgoView.vue
