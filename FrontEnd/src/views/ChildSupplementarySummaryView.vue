<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
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
              <tr
                v-for="kidsummary of childSummaries"
                :key="kidsummary.id"
                v-if="isSummaryDataAvailable"
                v-bind:class="[kidsummary.index]"
              >
                <td>
                  <span data-nav="mob.kid.new" style="cursor: pointer">
                    <u @click="editChild(kidsummary.id)"
                      >{{ kidsummary.childName }}
                    </u></span
                  >
                  <br />
                  {{ kidsummary.motherName }} <br />
                  {{ kidsummary.gender }}, {{ kidsummary.child_age }}
                </td>
                <td class="col-4 align-self-end" v-if="kidsummary.height !== ''">
                  {{ kidsummary.height }} <br />
                  {{ kidsummary.weight }} <br />
                  {{ kidsummary.statdate }}
                </td>
                <td class="col-1 align-self-start">
                  <router-link
                    :to="`/KidsCheckUp/${kidsummary.id}`"
                    custom
                    v-slot="{ navigate }"
                  >
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
import { useSupplmentarySummaryStore } from "../stores/SupplmentarySummary";
import router from "../router";

const store = useSupplmentarySummaryStore();

const childSummaries = computed(() => {
  if (store.childSummaries) {
    console.log("withing comp" + store.childSummaries);
    return store.childSummaries;
  } else {
    return {
      id: "",
      childName: "",
      statdate: "",
      child_age: "",
      height: "",
      weight: "",
      gender: "",
      isActive: "",
      motherName: "",
    };
  }
  //return store.childSummaries?.data;
});
const isSummaryDataAvailable = computed(() => {
  return store.childSummaries?.length > 0;
});

onMounted(async () => {
  await store.fetchChildSummaries();
});
const editChild = (id) => {
  console.log("edit clicked" + id);
  router.push("EditChild/" + id);
};
</script>
