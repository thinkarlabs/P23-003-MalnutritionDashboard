<template>
  <main class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <div class="row">
        <h3 class="">Add Child Details</h3>
        <form @submit.prevent="postchild">
          <div class="mb-1 col-12">
            <label for="exampleFormControlInput1" class="form-label">Child's Name</label>
            <input
              class="form-control"
              type="string"
              aria-label="..."
              placeholder="Child name"
              v-model="newchild.childName"
            />
          </div>

          <div class="mb-1 col-12">
            <label for="exampleFormControlInput1" class="form-label">Mother's Name</label>
            <input
              class="form-control"
              type="string"
              aria-label="..."
              placeholder="Mothers name"
              v-model="newchild.motherName"
            />
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Age</label>
            <input
              class="form-control"
              type="number"
              aria-label="..."
              placeholder="Child Age"
              v-model="newchild.child_age"
            />
          </div>

          <div class="mb-1 col-6">
            <label for="exampleFormControlInput1" class="form-label">Gender</label>
            <select id="level" class="form-select" @change="genderchangevalue($event)">
              <option value="">Gender</option>
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
                v-model="newchild.isActive"
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
import router from "../router";
let newchild = reactive({
  childName: "",
  motherName: "",
  child_age: "",
  gender: 0,
  isActive: false,
});
const store = usechildStore();

const genderchangevalue = (event) => {
  const selectedvalue = event.target.options[event.target.options.selectedIndex].text;
  newchild.gender = selectedvalue;
  console.log(selectedvalue);
};

const postchild = async () => {
  await store.postchild(newchild);
  return router.push("/ChildSupplementarySummaryView");
};
</script>
