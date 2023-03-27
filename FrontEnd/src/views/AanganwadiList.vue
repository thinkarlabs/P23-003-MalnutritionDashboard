<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
    <div class="row">
      <div class="col-12 p-2">
        <h3 class="float-start ps-2">All Aanganwadies</h3>
        <router-link to="/addAanganwadi" custom v-slot="{ navigate }">
          <button
            type="button"
            class="btn btn-primary float-end mx-2"
            data-nav="admin.aanganwadi.new"
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
            <th scope="col">Contact Person</th>
            <th scope="col">Contact Phone</th>
            <th scope="col">Location</th>
            <th scope="col">GeoCoordinates</th>
            <th scope="col" class="text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <div v-show="!isAanganwadiAvailable">
            <tr>
              <td>No records available</td>
            </tr>
          </div>
          <tr v-for="item of aanganwadies" :key="item.id">
            <td>{{ item.contactPersonName }}</td>
            <td>{{ item.contactPersonPhone }}</td>
            <td>{{ item.location }}</td>
            <td>{{ item.location_coordinates }}</td>
            <td class="col-2">
              <button
                type="button"
                class="btn btn-primary float-end mx-2"
                data-nav="admin.exercise.del"
                @click="deleteAanganwadi(item.id)"
              >
                <i class="bi bi-trash"></i>
              </button>
              <button
                type="button"
                class="btn btn-primary float-end mx-2"
                data-nav='admin.exercise.edit?memid="{{item.id}}"'
                @click="editAanganwadiPage(item.id)"
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
  import { useAanganwadiStore } from "../stores/aanganwadi";
  import swal from "sweetalert";
  import router from "../router";
  
  const store = useAanganwadiStore();
  
  const aanganwadies = computed(() => {
    return store.aanganwadies.data;
  });
  const isAanganwadiAvailable = computed(() => {
    console.log("aanganwadies -> "+JSON.stringify(store.aanganwadies));
    return store.aanganwadies != null;
  });
  const deleteAanganwadi = (id) => {
    swal({
      title: "Are you sure?",
      text: "Once deleted, you will not be able to recover this Aanganwadi!",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        store.deleteAanganwadi(id);
        swal("Aanganwadi has been deleted!", {
          icon: "success",
        });
        store.fetchAanganwadies();
      }
    });
  };  

  const editAanganwadiPage = (id) => {
    router.replace({ path: '/editAanganwadiPage/'+id })
  };

  const editAanganwadi = (id) => {
      store.editAanganwadi(id);
      swal("Aanganwadi has been updated!", {
        icon: "success",
      });
      store.fetchAanganwadies();
  };

  onMounted(() => {
    store.fetchAanganwadies();
  });

  </script>
