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
            <div className="text-danger mrgnbtn" v-if="msg.name">
              {{ msg.name }}
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
            <div className="text-danger mrgnbtn" v-if="msg.contactPersonName">
              {{ msg.contactPersonName }}
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
            <div className="text-danger mrgnbtn" v-if="msg.phoneNumber">
              {{ msg.phoneNumber }}
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
            <div className="text-danger mrgnbtn" v-if="msg.email">
              {{ msg.email }}
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
            <div className="text-danger mrgnbtn" v-if="msg.location">
              {{ msg.location }}
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
            <div className="text-danger mrgnbtn" v-if="msg.pincode">
              {{ msg.pincode }}
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
onMounted(async () => {
  console.log("Editing.... ");
  console.log(route.params.id);
  await store.getNgo(route.params.id);
  console.log(store.ngo);
});
let msg = reactive([]);

const updateNgo = async () => {
  let validationRegex = {
    name: /^[a-zA-Z]+(\s[a-zA-Z]+)?$/,
    pincode: /^[0-9]{6}$/,
    number: /^([+]\d{2})?\d{10}$/,
    email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  };

  if (updatedNgo._value.pincode.match(validationRegex.pincode)) {
    msg["pincode"] = "";
  } else {
    msg["pincode"] = "Please entered valid pincode";
  }
  if (updatedNgo._value.contactPersonName.match(validationRegex.name)) {
    msg["contactPersonName"] = "";
  } else {
    msg["contactPersonName"] = "Please entered a valid name";
  }
  if (updatedNgo._value.ngoName.match(validationRegex.name)) {
    msg["ngoName"] = "";
  } else {
    msg["ngoName"] = "Please entered a valid name";
  }
  if (updatedNgo._value.location.match(validationRegex.name)) {
    msg["location"] = "";
  } else {
    msg["location"] = "Please entered a valid name";
  }
  if (updatedNgo._value.contactPersonPhone.match(validationRegex.number)) {
    msg["phoneNumber"] = "";
  } else {
    msg["phoneNumber"] = "Please entered a valid phoneNumber";
  }

  if (updatedNgo._value.contactPersonEmail.match(validationRegex.email)) {
    msg["email"] = "";
  } else {
    msg["email"] = "Please entered a valid email";
  }
  if (
    updatedNgo._value.contactPersonEmail.match(validationRegex.email) &&
    updatedNgo._value.contactPersonPhone.match(validationRegex.number) &&
    updatedNgo._value.pincode.match(validationRegex.pincode) &&
    updatedNgo._value.contactPersonName.match(validationRegex.name) &&
    updatedNgo._value.ngoName.match(validationRegex.name) &&
    updatedNgo._value.location.match(validationRegex.name)
  ) {
    await store.updateNgo(updatedNgo);
    return router.push("/ngos");
  }
};
</script>
