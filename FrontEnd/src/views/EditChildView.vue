<template>
  <main class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <div class="row">
        <h3 class="">Manage Child Details</h3>
        <form @submit.prevent="updateChild">
          <div class="mb-1 col-12">
            <label for="exampleFormControlInput1" class="form-label">Child's Name</label>
            <input
              class="form-control"
              type="string"
              aria-label="..."
              placeholder="Child name"
              v-model="currentchild.childName"
            />
          </div>

          <div class="mb-1 col-12">
            <label for="exampleFormControlInput1" class="form-label">Mother's Name</label>
            <input
              class="form-control"
              type="string"
              aria-label="..."
              placeholder="Mothers name"
              v-model="currentchild.motherName"
            />
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Age</label>
            <input
              class="form-control"
              type="number"
              aria-label="..."
              placeholder="Child Age"
              v-model="currentchild.child_age"
            />
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Gender</label>
            <select
              id="level"
              class="form-select"
              @change="genderchangevalue($event)"
              v-bind:value="currentchild.gender"
            >
              <option value="" selected>Gender</option>
              <option value="Male" key="1">Male</option>
              <option value="Female" key="2">Female</option>
              <option value="Other" key="3">Other</option>
            </select>
          </div>

          <div class="mt-2 col-12">
            <div class="form-check float-end">
              <input
                class="form-check-input"
                type="checkbox"
                v-model="currentchild.isActive"
                id="flexCheckDefault"
              />
              <label class="form-check-label" for="flexCheckDefault"> In-Active </label>
            </div>
          </div>
          <div class="row">
            <div class="col-6 p-0">
              <router-link
                to="/ChildSupplementarySummaryView"
                custom
                v-slot="{ navigate }"
              >
                <button
                  class="w-100 bg-primary text-light"
                  data-nav="mob.childs"
                  @click="navigate"
                >
                  Cancel
                </button>
              </router-link>
            </div>
            <div class="col-6 p-0">
              <button
                type="submit"
                class="w-100 bg-primary text-light"
                data-nav="mob.childs"
                @click="navigate"
                role="link"
              >
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted, computed, reactive } from "vue";
import { usechildStore } from "../stores/child.js";
import { useRoute } from "vue-router";
import router from "../router";

const store = usechildStore();
const route = useRoute();

let currentchild = reactive({
  childName: "",
  motherName: "",
  child_age: "",
  gender: "",
  isActive: false,
});

currentchild = computed(() => {
  if (store.child) {
    return store.child;
  } else {
    return {
      id: "",
      childName: "",
      motherName: "",
      child_age: "",
      gender: "",
      isActive: false,
    };
  }
});

const genderchangevalue = (event) => {
  const selectedvalue = event.target.options[event.target.options.selectedIndex].text;
  currentchild.gender = selectedvalue;
  console.log(selectedvalue);
};

onMounted(async () => {
  console.log("Editing.... ");
  console.log(route.params.id);
  await store.getChild(route.params.id);
  console.log(store.child);
});

const updateChild = async () => {
  await store.updateChild(currentchild);
  return router.push("/ChildSupplementarySummaryView");
};
</script>
