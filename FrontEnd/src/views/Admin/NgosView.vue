<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <div class="row">
        <div class="col-12 p-2">
          <h3 class="float-start ps-2">{{ $t('ngo.NGOs') }}</h3>
          <router-link to="/addngo" custom v-slot="{ navigate }">
            <button
              type="button"
              class="btn btn-primary float-end mx-2"
              id="addNGO"
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
              <th scope="col">{{ $t('ngo.name') }}</th>
              <th scope="col">{{ $t('ngo.contact_person') }}</th>
              <th scope="col">{{ $t('ngo.contact_email') }}</th>
              <th scope="col">{{ $t('ngo.contact_password') }}</th>
              <th scope="col">{{ $t('ngo.contact_phone') }}</th>
              <th scope="col" class="text-center">{{ $t('ngo.actions') }}</th>
            </tr>
          </thead>
          <tbody>
            <div v-show="!isNgoAvailable">
              <tr>
                <td>{{ $t('common.no_records') }}</td>
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
                  id="deleteNGO"
                  @click="deleteNgo(item.id)"
                >
                  <i class="bi bi-trash"></i>
                </button>
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  id="editNGO"
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
import { useNgoStore } from "../../stores/ngo";
import swal from "sweetalert";
import router from "../../router";

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
