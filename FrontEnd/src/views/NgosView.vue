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
                <th scope="col">Contact Phone No</th>
                <th scope="col" class="text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <li v-for="item of items" :key="item.id">
                  <td>{{ item.ngo_name }}</td>
                  <td>{{ item.ngo_contact }}</td>
                  <td>{{ item.ngo_email }}</td>
                  <td>{{ item.ngo_phone }}</td>
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
                      data-nav='admin.exercise.edit?memid="{{item.memid}}"'
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
<script>
import { ref } from "vue";

export default {
  name: "App",
  setup() {
    // make users variable reactive with the ref() function
    const items = ref([
      {
        ngo_id: "01",
        ngo_name: "Spirulina Foundation",
        ngo_contact: "Mahesh N",
        ngo_phone: "6754476326",
        ngo_email: "mahesh.spirulina@gmail.com",
        ngo_pwd: "pass",
      },
      {
        ngo_id: "02",
        ngo_name: "Antenna India",
        ngo_contact: "Ramesh Sinha",
        ngo_phone: "6754476326",
        ngo_email: "ramesh.s6344@gmail.com",
        ngo_pwd: "pass",
      },
      {
        ngo_id: "03",
        ngo_name: "Smile Foundation",
        ngo_contact: "Unnati Baranwal",
        ngo_phone: "6754476326",
        ngo_email: "unnati@smilefoundationindia.org",
        ngo_pwd: "pass",
      },
    ]);

    return {
      items,
    };
  },
};
</script>
