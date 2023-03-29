<script setup>
import { onMounted, computed } from "vue";
import swal from "sweetalert";
import { useProgramStore } from "../stores/program.js";
import router from "../router";

const store = useProgramStore();

const programData = computed(() => {
  return store.programs.data;
});
const isProgramsAvailable = computed(() => {
  return store.programs?.data?.length > 0;
});

const editProgram = (id) => {
  router.replace({ path: "/editprogram/" + id });
};
const deleteProgram = (id) => {
  swal({
    title: "Are you sure?",
    text: "Once deleted, you will not be able to recover this Program!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      store.deleteProgram(id);
      swal("Program has been deleted!", {
        icon: "success",
      });
    }
  });
};
onMounted(() => {
  store.fetchProgram();
});
</script>

<template>
  <div id="x-main" class="container-full mt-5 p-3" style="min-height: 550px">
    <div class="container-md">
      <div class="row">
        <div class="col-12 p-2">
          <h3 class="float-start ps-2">Programs</h3>
          <router-link to="/addprogram" custom v-slot="{ navigate }">
            <button
              type="button"
              class="btn btn-primary float-end mx-2"
              data-nav="ngo.program.new"
              @click="navigate"
              role="link"
            >
              <i class="bi bi-plus-square"></i>
            </button>
          </router-link>
        </div>
        <div id="x-challenges">
          <table class="table table-striped" id="tbl_ch">
            <thead class="table-dark">
              <tr>
                <th scope="col">Code</th>
                <th scope="col">Donor</th>
                <th scope="col">Supplement</th>
                <th scope="col">From</th>
                <th scope="col">To</th>
                <th scope="col">Notes</th>
                <th scope="col" class="text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <div v-show="!isProgramsAvailable">
                <tr>
                  <td>No records available</td>
                </tr>
              </div>
              <tr v-for="program of programData" :key="programData.id">
                <td>{{ program.invite_code }}</td>
                <td>{{ program.donor_name }}</td>
                <td>{{ program.supplement_name }}</td>
                <td>{{ program.from_date }}</td>
                <td>{{ program.to_date }}</td>
                <td class="col-3">{{ program.notes }}</td>
                <td class="col-2">
                  <button
                    type="button"
                    class="btn btn-primary float-end mx-2"
                    data-nav="ngo.program.del"
                    @click="deleteProgram(program.id)"
                  >
                    <i class="bi bi-trash"></i>
                  </button>
                  <router-link to="/addprogram" custom v-slot="{ navigate }">
                    <button
                      type="button"
                      class="btn btn-primary float-end mx-2"
                      data-nav="ngo.program.edit"
                      @click="editProgram(program.id)"
                    >
                      <i class="bi bi-pencil-square"></i>
                    </button>
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
