<template>
  <main class="container-full">
    <div id="x-main" class="container-fluid mt-5 p-0">
      <div class="row">
        <div class="col-12 m-0">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Details</th>
                <th scope="col">+</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="kidsummary of kidssummaries" :key="kidsummary.id">
                <td>
                  <span data-nav="mob.kid.new" style="cursor: pointer">
                    <u>{{ kidsummary.kid_name }} </u></span
                  >
                  <br />
                  {{ kidsummary.kid_pname }} <br />
                  {{ kidsummary.kid_gender }}, {{ kidsummary.kid_age }}
                </td>
                <td class="col-4 align-self-end">
                  {{ kidsummary.kid_height }} <br />
                  {{ kidsummary.kid_weight }} <br />
                  {{ kidsummary.kid_statdate }}
                </td>
                <td class="col-1 align-self-start">
                  <router-link to="/KidsCheckUp" custom v-slot="{ navigate }">
                    <i
                      class="bi bi-plus-circle-fill"
                      data-nav="mob.kid.stats"
                      @click="navigate"
                    ></i>
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="col-12 p-0">
        <router-link to="/AddChild" custom v-slot="{ navigate }">
          <button
            type="button"
            class="w-100 bg-primary text-light"
            data-nav="mob.kid.new"
            @click="navigate"
            role="link"
          >
            New
          </button>
        </router-link>
      </div>
    </div>
  </main>
</template>

<script setup>
const kidssummaries = [
  {
    id: 1,
    kid_name: "Sunil Karanth",
    kid_gender: "M",
    kid_age: "4y 3m",
    kid_pname: "S/O Rukmini Karanth",
    kid_height: "73 cms",
    kid_weight: "14.3 kgs",
    kid_index: "bg-light",
    kid_pic: "Spinal Cord Injury",
    kid_statdate: "02-Jan-2023",
  },
  {
    id: 2,
    kid_name: "Roshini K N",
    kid_gender: "F",
    kid_age: "3y 2m",
    kid_pname: "D/O Ramadevi K N",
    kid_height: "67 cms",
    kid_weight: "12.3 kgs",
    kid_index: "bg-warning",
    kid_pic: "Spinal Cord Injury",
    kid_statdate: "02-Jan-2023",
  },
  {
    id: 3,
    kid_name: "Kavitha Das",
    kid_gender: "F",
    kid_age: "3y 11m",
    kid_pname: "D/O Soumitra Das",
    kid_height: "76 cms",
    kid_weight: "18.3 kgs",
    kid_index: "bg-success",
    kid_pic: "Spinal Cord Injury",
    kid_statdate: "02-Jan-2023",
  },
];
</script>
