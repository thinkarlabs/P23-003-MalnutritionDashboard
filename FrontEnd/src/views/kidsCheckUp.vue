<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postMalnutritionDetail">
        <div class="row">
          <h3 class="form-label">Record Details for <b> Roshini K N (F, 3yr 4mo) </b></h3>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Select a date:</label
            >
            <input
              class="form-control"
              type="date"
              v-model="dateObj.selectedDate"
              :format="dateObj.dateFormat"
              id="datepicker"
            />
            <div>{{ formattedDate }}</div>
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Select Index</label>
            <select
              id="level"
              class="form-select"
              @change="nutritionIndexchangevalue($event)"
              v-bind:value="malnutritionDetail.malnutritionIndexCategory"
            >
              <option selected>Index</option>
              <option value="SAM">SAM</option>
              <option value="MAM">MAM</option>
              <option value="Normal">Normal</option>
            </select>
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Record Height (cms)</label
            >
            <input
              class="form-control"
              type="number"
              v-model="malnutritionDetail.height"
              aria-label="..."
            />
          </div>
          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Record Weight (kgs)</label
            >
            <input
              class="form-control"
              type="number"
              v-model="malnutritionDetail.weight"
              aria-label="..."
            />
          </div>
          <div class="col-12 mt-2">
            <button
              class="bg-primary text-light float-end"
              data-nav=""
              @click="navigate"
              type="submit"
              role="link"
            >
              Submit
            </button>

            <router-link to="/ChildSupplementarySummaryView" custom v-slot="{ navigate }">
              <button
                class="bg-primary text-light float-end me-2"
                data-nav="mob.kids"
                @click="navigate"
                role="link"
              >
                Cancel
              </button>
            </router-link>
          </div>
          <div class="my-2 col-12" v-if="isHistoryAvailable">
            <label for="exampleFormControlInput1" class="form-label"
              >Health Record History</label
            >
            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col" id="tableRow">Date</th>
                  <th scope="col" id="tableRow">Stats</th>
                </tr>
              </thead>
              <tbody v-for="item in malnutritionstats">
                <tr class="Row-styling">
                  <td class="col-2 align-self-start">{{ item.date }}</td>
                  <td>
                    {{ item.height }}cms, {{ item.weight }}kg [{{
                      item.malnutritionIndexCategory
                    }}]
                  </td>
                </tr>
              </tbody>
            </table>
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
import router from "../router";
import { useRoute } from "vue-router";
import { useMalnutritionDetailStore } from "../stores/malnutritiondetail";
import DatePicker from "vue3-datepicker";
import { format } from "date-fns";

const store = useMalnutritionDetailStore();
const route = useRoute();

let dateObj = reactive({
  selectedDate: null,
  dateFormat: "dd/MMM/yyyy",
});

let malnutritionDetail = reactive({
  malnutritionIndexCategory: "",
  date: dateObj.selectedDate,
  child_id: "",
  height: "",
  weight: "",
});

let malnutritionstats = computed(() => {
  if (store.currentChildMalnutrition.data) {
    return store.currentChildMalnutrition.data;
  } else {
    return {
      id: "",
      malnutritionIndexCategory: "",
      date: dateObj.selectedDate,
      child_id: "",
      height: "",
      weight: "",
    };
  }
});

const formattedDate = computed(() => {
  console.log("date", dateObj.selectedDate);
  malnutritionDetail.date = dateObj.selectedDate;
  //Todo: need to find whether we need this format later
  // malnutritionDetail.stat_date = dateObj.selectedDate
  //   ? format(dateObj.selectedDate, dateObj.dateFormat)
  //   : "";
});

const isHistoryAvailable = computed(() => {
  return store.currentChildMalnutrition?.data?.length > 0;
});

onMounted(async () => {
  console.log("Editing.... ");
  console.log(route.params.id);
  await store.getChildMalnutritionHistory(route.params.id);
  console.log("got result for child malnutrtion status");
  console.log(store.currentChildMalnutrition.data.data);
});

const nutritionIndexchangevalue = (event) => {
  const selectedvalue = event.target.options[event.target.options.selectedIndex].text;
  malnutritionDetail.malnutritionIndexCategory = selectedvalue;
  console.log(selectedvalue);
};

const postMalnutritionDetail = async () => {
  malnutritionDetail.child_id = route.params.id;
  console.log("vue", malnutritionDetail);
  await store.postNutritionStats(malnutritionDetail);
  location.reload();
  //Todo: need to find another better solution
  //return router.push("/kidscheckup/" + malnutritionDetail.child_id);
};
</script>
