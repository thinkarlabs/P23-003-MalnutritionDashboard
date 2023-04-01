<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <div class="row">
        <div class="col-12 p-2">
          <h3 class="float-start ps-2">Supplements</h3>
          <router-link to="/addsupplement" custom v-slot="{ navigate }">
            <button
              type="button"
              class="btn btn-primary float-end mx-2"
              data-nav="admin.supplements.new"
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
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col" class="text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            <div v-show="!isSupplementsAvailable">
              <tr>
                <td>No records available</td>
              </tr>
            </div>
            <tr v-for="item of supplements" :key="item.id">
              <td>{{ item.name }}</td>
              <td>{{ item.description }}</td>
              <td class="col-2">
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.exercise.del"
                  @click="deleteSupplement(item.id)"
                >
                  <i class="bi bi-trash"></i>
                </button>
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.exercise.edit"
                  @click="editSupplementPage(item.id)"
                >
                  <i class="bi bi-pencil-square"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
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
import { onMounted, computed } from "vue";
import { useSupplementStore } from "../../stores/supplement";
import swal from "sweetalert";
import router from "../../router";

const store = useSupplementStore();

const supplements = computed(() => {
  return store.supplements.data;
});
const isSupplementsAvailable = computed(() => {
  return store.supplements?.data?.length > 0;
});
const deleteSupplement = (id) => {
  swal({
    title: "Are you sure?",
    text: "Once deleted, you will not be able to recover this Supplement!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      store.deleteSupplement(id);
      swal("Supplement has been deleted!", {
        icon: "success",
      });
      supplements.value = store.fetchSupplements();
    }
  });
};
const editSupplementPage = (id) => {
  console.log("edit clicked" + id);
  router.push("editsupplement/" + id);
};
onMounted(() => {
  store.fetchSupplements();
});
</script>
