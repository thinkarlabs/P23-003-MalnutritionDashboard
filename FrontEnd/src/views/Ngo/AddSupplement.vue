<template>
  <div class="full-div container" style="width: 1280px">
    <div id="x-contest" class="container-fluid p-3">
      <form @submit.prevent="postSupplement">
        <div class="row">
          <h3 class="float-start">Manage Supplement</h3>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">Title</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Supplement Title"
              v-model="newSupplement.title"
            />
            <div className="text-danger mrgnbtn" v-if="helperSupport.title">
              {{ helperSupport.title }}
            </div>
          </div>

          <div class="col-12 my-2">
            <label for="exampleFormControlInput1">Description</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Supplement Description"
              v-model="newSupplement.description"
            />
            <div
              className="text-danger mrgnbtn"
              v-if="helperSupport.description"
            >
              {{ helperSupport.description }}
            </div>
          </div>

          <div class="row">
            <div class="col-12 p-2">
              <button
                type="submit"
                class="btn btn-primary float-end mx-2"
                data-nav="admin.supplement"
                @click="navigate"
                role="link"
              >
                Save
              </button>
              <router-link to="/supplements" custom v-slot="{ navigate }">
                <button
                  type="button"
                  class="btn btn-primary float-end mx-2"
                  data-nav="admin.supplement"
                  @click="navigate"
                  role="link"
                >
                  Cancel
                </button>
              </router-link>
            </div>
          </div>
        </div>
      </form>
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
import { ref, onMounted, computed, reactive } from "vue";
import { useSupplementStore } from "../../stores/supplement";
import router from "../../router";
import helper from "../../helper/validation.helper.js";
let newSupplement = reactive({
  title: "",
  description: "",
});
const store = useSupplementStore();

const helperSupport = reactive({
  title: "",
  description: "",
});

const isValidSubmission = (newSupplement) => {
  helperSupport.title = helper.validateName(newSupplement.name);
  helperSupport.description =
    newSupplement.description !== "" ? "" : "Description is mandatory";
  return helper.isErrorMessagesAvailable(helperSupport) ? false : true;
};

const postSupplement = async () => {
  if (isValidSubmission(newSupplement) == true) {
    await store.postSupplement(newSupplement);
    return router.push("/supplements");
  }
};
</script>
