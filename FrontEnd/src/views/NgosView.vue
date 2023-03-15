<template>
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

    <table class="col-12 table table-striped" id="tbl_ch">
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
        <div v-show="!isNgoAvailable">
          <tr>
            <td>No records available</td>
          </tr>
        </div>
        <tr v-for="item of ngos" :key="item.id">
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
              @click="deleteNgo(item.id)"
            >
              <i class="bi bi-trash"></i>
            </button>
            <button
              type="button"
              class="btn btn-primary float-end mx-2"
              data-nav="admin.exercise.edit"
              @click="editNgo(item.id)"
            >
              <i class="bi bi-pencil-square"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup>
import { onMounted, computed } from "vue";
import { useNgoStore } from "../stores/ngo";
import swal from "sweetalert";
import router from "../router";

const store = useNgoStore();

const ngos = computed(() => {
  return store.ngos.data;
});
const isNgoAvailable = computed(() => {
  return store.ngos?.data?.length > 0;
});
const deleteNgo = (id) => {
  swal({
    title: "Are you sure?",
    text: "Once deleted, you will not be able to recover this Ngo!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      store.deleteNgo(id);
      swal("Ngo has been deleted!", {
        icon: "success",
      });
      ngos.value = store.fetchNgos();
    }
  });
};
const editNgo = (id) => {
  console.log("edit clicked" + id);
  router.push("editngo/" + id);
};
onMounted(() => {
  store.fetchNgos();
});
</script>
