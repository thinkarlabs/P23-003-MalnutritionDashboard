<template>
  <div id="x-main" class="container-full mt-5 p-3" style="min-height: 550px">
    <div class="container-md">
      <div class="row">
        <div class="col-12 p-2">
          <h3 class="float-start ps-2">NGOs</h3>
          <router-link to="/addngo" custom v-slot="{ navigate }">
            <button
              type="button"
              class="btn btn-primary float-end mx-2"
              data-nav="admin.ngo.new"
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
                <th scope="col">NGO Name</th>
                <th scope="col">Contact Person</th>
                <th scope="col">Contact EMail</th>
                <th scope="col">Contact Password</th>
                <th scope="col">Contact Phone</th>
                <th scope="col" class="text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <li v-for="item of ngos" :key="item.id">
                  <td>{{ item.ngoName }}</td>
                  <td>{{ item.contactPersonName }}</td>
                  <td>{{ item.contactPersonEmail }}</td>
                  <td>{{ item.contactPersonPassword }}</td>
                  <td>{{ item.contactPersonPhone }}</td>
                  <td class="col-2">
                    <button
                      type="button"
                      class="btn btn-primary float-end mx-2"
                      data-nav="admin.exercise.del"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                    <button
                      type="button"
                      class="btn btn-primary float-end mx-2"
                      data-nav='admin.exercise.edit?memid="{{item.id}}"'
                    >
                      <i class="bi bi-pencil-square"></i>
                    </button>
                  </td>
                </li>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, computed } from "vue";
import { useNgoStore } from "../stores/ngo";
const store = useNgoStore();

const ngos = computed(() => {
  return store.ngos.data;
});
onMounted(() => {
  store.fetchNgos();
});
</script>
