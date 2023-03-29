<template>
  <main class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postSupplementSupplyDetail">
        <div class="row">
          <h3 class="p-1">Spirulina Chiki Supplement Pack</h3>
          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Select Date</label>
            <input
              class="form-control"
              type="date"
              v-model="dateObj.selectedDate"
              :format="dateObj.dateFormat"
              id="datepicker"
            />
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Packs</label>
            <input
              class="form-control"
              type="number"
              aria-label="..."
              v-model="supplementSupplyDetail.no_of_packs_given"
            />
          </div>

          <div class="col-12 mt-2">
            <button class="bg-primary text-light float-end" data-nav="">Submit</button>
            <router-link to="/programssummary" custom v-slot="{ navigate }">
              <button
                class="bg-primary text-light float-end me-2"
                data-nav="mob.home"
                @click="navigate"
                role="link"
              >
                Cancel
              </button>
            </router-link>
          </div>
          <div class="my-2 col-12" v-if="isHistoryAvailable">
            <label for="exampleFormControlInput1" class="form-label"
              >Supplement Schedule</label
            >

            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col">Date</th>
                  <th scope="col">Packs</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="supplySchedule of supplySchedules"
                  :key="supplySchedule.program_joining_id"
                >
                  <td>{{ displayFormatDate(supplySchedule.given_date) }}</td>
                  <td class="col-4 align-self-end">
                    {{ supplySchedule.no_of_packs_given }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </form>
    </div>
  </main>
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
import router from "../router";
import { useRoute } from "vue-router";
import { useSupplementSupplyStore } from "../stores/SupplementSupply";
import DatePicker from "vue3-datepicker";
import { format } from "date-fns";

const store = useSupplementSupplyStore();
const route = useRoute();

let dateObj = reactive({
  selectedDate: null,
  dateFormat: "dd/MMM/yyyy",
});

let supplementSupplyDetail = reactive({
  no_of_packs_given: "",
  given_date: dateObj.selectedDate,
  program_joining_id: "",
});

let supplySchedules = computed(() => {
  if (store.supplySchedules.data) {
    return store.supplySchedules.data;
  } else {
    return {
      program_joining_id: "",
      given_date: dateObj.selectedDate,
      no_of_packs_given: "",
    };
  }
});

const isHistoryAvailable = computed(() => {
  return store.supplySchedules?.data?.length > 0;
});

onMounted(async () => {
  console.log("Editing Supply pack detail.... ");
  console.log(route.params.id);
  await store.getSupplyScheduleHistory(route.params.program_joining_id);
  console.log("got result for Supply pack details history");
  console.log(store.supplySchedules.data.data);
});

const postSupplementSupplyDetail = async () => {
  supplementSupplyDetail.given_date = dateObj.selectedDate;
  supplementSupplyDetail.program_joining_id = route.params.program_joining_id;
  console.log("supplementSupplyDetail", supplementSupplyDetail);
  await store.postSupplementSupplyDetail(supplementSupplyDetail);
  //Todo: need to find another better solution
  location.reload();
};

const displayFormatDate = (currentDate) => {
  return new Date(currentDate)
    .toLocaleDateString("en-GB", {
      day: "numeric",
      month: "short",
      year: "numeric",
    })
    .replace(/ /g, "-");
};
</script>
