<template>
    <div class="full-div container" style="width: 1280px">
      <div id="x-contest" class="container-fluid p-3">
        <div class="row">
          <div class="col-12 p-2">
            <h3 class="float-start ps-2">Donors</h3>
            <router-link to="/addDonor" custom v-slot="{ navigate }">
              <button
                type="button"
                class="btn btn-primary float-end mx-2"
                data-nav="admin.donor.new"
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
                <th scope="col">Contact</th>
                <th scope="col">Email</th>
                <th scope="col">Phone No</th>
                <th scope="col" class="text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <div v-show="!isDonorsAvailable">
                <tr>
                  <td>No records available</td>
                </tr>
              </div>
              <tr v-for="item of donors" :key="item.id">
                <td>{{ item.name }}</td>
                <td>{{ item.contactperson }}</td>
                <td>{{ item.email }}</td>
                <td>{{ item.phone }}</td>
                <td class="col-2">
                  <button
                    type="button"
                    class="btn btn-primary float-end mx-2"
                    data-nav="admin.exercise.del"
                    @click="deleteDonor(item.id)"
                  >
                    <i class="bi bi-trash"></i>
                  </button>
                  <button
                    type="button"
                    class="btn btn-primary float-end mx-2"
                    data-nav="admin.exercise.edit"
                    @click="editDonor(item.id)"
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
  import { useDonorsStore } from "../stores/donors";
  import swal from "sweetalert";
  import router from "../router";
  
  const store = useDonorsStore();
  
  const donors = computed(() => {
    return store.donors.data;
  });
  const isDonorsAvailable = computed(() => {
    return store.donors?.data?.length > 0;
  });
  const deleteDonor = (id) => {
    swal({
      title: "Are you sure?",
      text: "Once deleted, you will not be able to recover this Donor!",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        store.deleteDonor(id);
        swal("Donor has been deleted!", {
          icon: "success",
        });
        donors.value = store.fetchDonors();
      }
    });
  };
  const editDonor = (id) => {
    console.log("DonorsList :: edit clicked " + id);
    router.push("editDonor/" + id);
  };
  onMounted(() => {
    store.fetchDonors();
  });
  </script>
  