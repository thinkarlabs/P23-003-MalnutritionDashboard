<script setup>
import { watch, onMounted, computed, reactive } from "vue";
import { useProgramStore } from "../../stores/program";
import { useRoute } from "vue-router";
import router from "../../router";
import helper from "../../helper/validation.helper.js";

const store = useProgramStore();
const route = useRoute();

let supplements = computed(() => {
  return store.supplement;
});

let donors = computed(() => {
  return store.donor.data;
});

let currentProgram = reactive({
  title: "",
  invite_code: "",
  supplement_name: "",
  donor_name: "",
  notes: "",
  from_date: "",
  to_date: "",
});

const helperSupport = reactive({
  title: "",
  invite_code: "",
  date: "",
  notes: "",
});

currentProgram = computed(() => {
  if (store.currentprogram) {
    return store.currentprogram;
  } else {
    return {
      title: "",
      invite_code: "",
      supplement_name: "",
      donor_name: "",
      notes: "",
      from_date: "",
      to_date: "",
    };
  }
});

onMounted(async () => {
  await store.fetchSupplement();
  await store.fecthDonor();
  await store.fetchProgramById(route.params.id);
});

const isValidSubmission = (currentProgram) => {
  helperSupport.title = helper.validateName(currentProgram._value.title);
  helperSupport.invite_code = helper.validatePincode(currentProgram._value.invite_code);
  helperSupport.date = helper.validateDateRange(
    currentProgram._value.from_date,
    currentProgram._value.to_date
  );
  helperSupport.notes =
    currentProgram._value.notes !== "" ? "" : "Description is mandatory";
  console.log("date", helperSupport.date);
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

const updatingProgram = async () => {
  if (isValidSubmission(currentProgram) == true) {
    await store.updatingProgram(currentProgram);
    return router.push("/programs");
  }
};
</script>

<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="updatingProgram">
        <div class="row">
          <div class="col-12 p-2">
            <h3 class="float-start">Updating Program</h3>
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
                v-model="currentProgram.title"
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
                v-model="currentProgram.from_date"
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
                v-model="currentProgram.to_date"
              />
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-4">
              <label for="exampleFormControlInput1">Donor</label>
              <select id="level" class="form-select" v-model="currentProgram.donor_name">
                <option value="" selected>Donor</option>
                <option v-for="item in donors" :value="item.name">
                  {{ item.name }}
                </option>
              </select>
            </div>

            <div class="col-4">
              <label for="exampleFormControlInput1">Supplement</label>
              <select
                id="level"
                class="form-select"
                v-model="currentProgram.supplement_name"
              >
                <option value="" selected>Supplement</option>
                <option v-for="item in supplements.data" v-bind:value="item.name">
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
                v-model="currentProgram.invite_code"
              />
              <div className="text-danger mrgnbtn" v-if="helperSupport.invite_code">
                {{ helperSupport.invite_code }}
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-12">
              <label for="exampleFormControlInput1">Notes</label>
              <textarea class="form-control" v-model="currentProgram.notes"></textarea>
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
