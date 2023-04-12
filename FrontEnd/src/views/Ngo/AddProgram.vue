<script setup>
import { ref, onMounted, computed, reactive, watch } from "vue";
import router from "../../router";
import { useProgramStore } from "../../stores/program.js";
import helper from "../helper/validation.helper.js";

const store = useProgramStore();

let donor = reactive({
  name: "",
  _id: null,
});

let supplement = reactive({
  name: "",
  _id: null,
});

let supplements = computed(() => {
  return store.supplement;
});

let donors = computed(() => {
  return store.donor.data;
});

let selectedDonorObject = computed(() => {
  return store.donor.data?.find((item) => item.name === donor.name);
});

watch(selectedDonorObject, (value) => {
  if (value) {
    donor._id = value.id;
  } else {
    donor._id = null;
  }
});

let selectedSupplementObj = computed(() => {
  return store.supplement.data?.find((item) => item.name === supplement.name);
});

watch(selectedSupplementObj, (value) => {
  if (value) {
    supplement._id = value.id;
  } else {
    supplement._id = null;
  }
});

let createProgram = {
  title: "",
  invite_code: "",
  donor,
  donor_name: "",
  supplement_name: "",
  supplement,
  from_date: "",
  to_date: "",
  notes: "",
};

const helperSupport = reactive({
  title: "",
  invite_code: "",
  date: "",
  notes: "",
});

onMounted(async () => {
  await store.fetchSupplement();
  await store.fecthDonor();
});

const isValidSubmission = (createProgram) => {
  helperSupport.title = helper.validateName(createProgram.title);
  helperSupport.invite_code = helper.validatePincode(createProgram.invite_code);
  helperSupport.date = helper.validateDateRange(
    createProgram.from_date,
    createProgram.to_date
  );
  helperSupport.notes =
    createProgram.notes !== "" ? "" : "Description is mandatory";
  console.log("date", helperSupport.date);
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

const addProgram = () => {
  if (isValidSubmission(createProgram) == true) {
    let idObject = {
      suppId: createProgram.supplement._id,
      donorId: createProgram.donor._id,
    };
    delete createProgram.donor;
    delete createProgram.supplement;
    createProgram["supplements_details_id"] = idObject.suppId;
    createProgram["donor_id"] = idObject.donorId;
    store.createProgram(createProgram);
    return router.push("/programs");
  }
};
</script>

<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="addProgram">
        <div class="row">
          <div class="col-12 p-2">
            <h3 class="float-start">Add Program</h3>
            <router-link to="/programs" custom v-slot="{ navigate }">
              <button
                type="button"
                class="btn btn-primary float-end mx-2"
                data-nav="ngo.program"
                @click="navigate"
                role="link"
              >
                Cancel
              </button>
            </router-link>
            <button
              type="submit"
              class="btn btn-primary float-end mx-2"
              data-nav="ngo.programs"
            >
              Save
            </button>
          </div>
        </div>
        <div id="x-challenge" class="container-float">
          <div class="row">
            <div class="col-6">
              <label for="exampleFormControlInput1">Title</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Title"
                v-model="createProgram.title"
              />
              <div className="text-danger mrgnbtn" v-if="helperSupport.title">
                {{ helperSupport.title }}
              </div>
            </div>
            <div class="col-3">
              <label for="exampleFormControlInput1">From</label>
              <input
                type="date"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="From Date"
                v-model="createProgram.from_date"
              />
              <div className="text-danger mrgnbtn" v-if="helperSupport.date">
                {{ helperSupport.date }}
              </div>
            </div>
            <div class="col-3">
              <label for="exampleFormControlInput1">To</label>
              <input
                type="date"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="To Date"
                v-model="createProgram.to_date"
              />
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-4">
              <label for="exampleFormControlInput1">Donor</label>
              <select id="level" class="form-select" v-model="donor.name">
                <option value="" selected>Donor</option>
                <option v-for="item in donors" v-bind:value="item.name">
                  {{ item.name }}
                </option>
              </select>
            </div>

            <div class="col-4">
              <label for="exampleFormControlInput1">Supplement</label>
              <select id="level" class="form-select" v-model="supplement.name">
                <option value="" selected>Supplement</option>
                <option
                  v-for="item in supplements.data"
                  v-bind:value="item.name"
                >
                  {{ item.name }}
                </option>
              </select>
            </div>

            <div class="col-4">
              <label for="exampleFormControlInput1">Invite Code</label>
              <input
                type="text"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="Invite Code"
                v-model="createProgram.invite_code"
              />
              <div
                className="text-danger mrgnbtn"
                v-if="helperSupport.invite_code"
              >
                {{ helperSupport.invite_code }}
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-12">
              <label for="exampleFormControlInput1">Notes</label>
              <textarea
                class="form-control"
                v-model="createProgram.notes"
              ></textarea>
              <div className="text-danger mrgnbtn" v-if="helperSupport.notes">
                {{ helperSupport.notes }}
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<style></style>
