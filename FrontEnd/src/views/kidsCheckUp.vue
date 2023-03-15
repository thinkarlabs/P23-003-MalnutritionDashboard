<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postNgo">
        <div class="row">
          <h3 class="form-label">
            "Record Details for <b> Roshini K N (F, 3yr 4mo) </b>
          </h3>

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
            <select id="level" class="form-select" v-model="newNgo.index">
              <option selected>index</option>
              <option value="S">SAM</option>
              <option value="M">MAM</option>
              <option value="N">Normal</option>
            </select>
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Record Height (cms)</label
            >
            <input
              class="form-control"
              type="number"
              v-model="newNgo.height"
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
              v-model="newNgo.weight"
              aria-label="..."
            />
          </div>
          <div class="col-12 mt-2">
            <button class="bg-primary text-light float-end" data-nav="">Submit</button>
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
          <div class="my-2 col-12">
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
              <tbody v-for="item in stats">
                <tr class="Row-styling">
                  <td class="col-2 align-self-start">{{ item.stat_date }}</td>
                  <td>{{ item.height }}cms, {{ item.weight }}kg [{{ item.index }}]</td>
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
import DatePicker from "vue3-datepicker";
import { format } from "date-fns";

let dateObj = reactive({
  selectedDate: null,
  dateFormat: "dd/MMM/yyyy",
});

let stats = reactive([
  {
    stat_id: "001",
    stat_date: "12/Jan/2023",
    height: "132",
    weight: "34",
    index: "M",
  },
  {
    stat_id: "001",
    stat_date: "16/Jan/2023",
    height: "142",
    weight: "43",
    index: "N",
  },
  {
    stat_id: "001",
    stat_date: "27/Jan/2023",
    height: "137",
    weight: "23",
    index: "S",
  },
]);
let newNgo = reactive({
  stat_id: "001",
  stat_date: "",
  index: "index",
  height: "",
  weight: "",
});

const formattedDate = computed(() => {
  console.log("date", dateObj.selectedDate);
  newNgo.stat_date = dateObj.selectedDate
    ? format(dateObj.selectedDate, dateObj.dateFormat)
    : "";
});

const postNgo = () => {
  console.log("vue", newNgo);
  stats.push(newNgo);
};
</script>
