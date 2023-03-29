<template>
  <main class="container-full">
    <div id="x-main" class="container-fluid mt-5 p-0" style="min-height: 500px">
      <div class="card rounded-3 shadow-sm" style="background-color: #afeeee">
        <div class="card-header">
          <h4 class="my-0 fw-normal">47 Children</h4>
        </div>
        <div class="card-body">
          <h3 class="card-title pricing-card-title">
            3
            <small class="text-muted fw-light"
              >[SAM] <i class="bi bi-arrow-up-circle text-danger"></i> 1
            </small>
          </h3>
          <h3 class="card-title pricing-card-title">
            12
            <small class="text-muted fw-light"
              >[MAM] <i class="bi bi-arrow-down-circle text-success"></i> 2
            </small>
          </h3>
        </div>
      </div>

      <h3 class="p-2">Supplement Programs</h3>

      <table class="table table-hover">
        <tbody>
          <tr
            v-for="item of programsummaries"
            :key="item.program_joining_id"
            style="cursor: pointer"
            data-nav="mob.supplement"
          >
            <td
              @click="editProgramJoiningSupplies(item.program_joining_id)"
              style="cursor: pointer"
            >
              {{ item.supplement_name }} supplement pack by {{ item.donor_name }} from
              {{ item.from_date }} to
              {{ item.to_date }}
            </td>
          </tr>
        </tbody>
      </table>
      <div class="table table-hover">
        <div class="col-8 p-0">
          <input
            class="w-100"
            type="text"
            v-model="updatedJoiningCode.invite_code"
            aria-label="..."
            placeholder="Program Invite Code"
          />
        </div>
        <div class="col-4 p-0">
          <button class="w-100 bg-primary text-light" data-nav="" @click="joinProgram()">
            Join
          </button>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { onMounted, computed, reactive } from "vue";
import { useProgramSummaryStore } from "../stores/programsummary";
import router from "../router";

const store = useProgramSummaryStore();

let updatedJoiningCode = reactive({
  aanganwadi_id: "64218dc533d73ceb3c76e454",
  invite_code: "",
  program_joining_id: "",
  isActive: "True",
});

const programsummaries = computed(() => {
  return store.programsummaries.data;
});
const isProgramSummaryAvailable = computed(() => {
  return store.programsummaries?.data?.length > 0;
});
const editProgramJoiningSupplies = (program_joining_id) => {
  console.log("edit clicked" + program_joining_id);
  router.push("SupplementSupply/" + program_joining_id);
};
onMounted(async () => {
  await store.fetchProgramSummaries(updatedJoiningCode.aanganwadi_id);
});

const joinProgram = () => {
  console.log("updatedJoiningCode" + JSON.stringify(updatedJoiningCode));
  store.postProgramJoining(updatedJoiningCode);
};
</script>
