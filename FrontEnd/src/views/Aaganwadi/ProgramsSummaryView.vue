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
        <table class="table table-hover">
          <tr>
            <td class="col-5">
              <input
                class="w-80"
                type="text"
                v-model="updatedJoiningCode.invite_code"
                aria-label="..."
                placeholder="Program Invite Code"
              />
            </td>
            <td style="padding-left: 5px" class="col-4">
              <button
                class="w-100 bg-primary text-light"
                data-nav=""
                @click="joinProgram()"
              >
                Join
              </button>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </main>
</template>
<style>
#x-main {
  width: auto;
}
</style>
<script setup>
import { onMounted, computed, reactive } from "vue";
import { useProgramSummaryStore } from "../../stores/programsummary";
import router from "../../router";

const store = useProgramSummaryStore();

let updatedJoiningCode = reactive({
  //Todo: Hardcoded value will be removed once login flow & base pages are implemented
  aanganwadi_id: "6423cc62f8b5a84041e29c27",
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
  router.push("supplementsupply/" + program_joining_id);
};
onMounted(async () => {
  await store.fetchProgramSummaries(updatedJoiningCode.aanganwadi_id);
});

const joinProgram = async () => {
  console.log("updatedJoiningCode" + JSON.stringify(updatedJoiningCode));
  await store.postProgramJoining(updatedJoiningCode);
  await store.fetchProgramSummaries(updatedJoiningCode.aanganwadi_id);
};
</script>
