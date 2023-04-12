<template>
  <main class="container-full">
    <div id="x-main" class="container-fluid mt-5 p-3" style="min-height: 550px">
      <div class="row">
        <div class="col-8">
          <h3 class="card-title">Beneficiaries</h3>
          <img style="width: 200px" src="../../public/img/spirulina-fnd.png" />
        </div>
        <div class="col-4">
          <div class="card login-card m-4 bg-secondary text-light">
            <div class="card-body">
              <h5 class="card-title">Login</h5>
              <form1>
                <div class="form-group">
                  <label for="usernameInput">Username</label>
                  <input
                    type="text"
                    class="form-control"
                    id="usernameInput"
                    placeholder="Enter username"
                    v-model="loginDetail.username"
                  />
                </div>
                <div class="form-group mt-2">
                  <label for="passwordInput">Password</label>
                  <input
                    type="password"
                    class="form-control"
                    id="passwordInput"
                    placeholder="Enter password"
                    v-model="loginDetail.password"
                  />
                </div>
                <button
                  type="submit"
                  class="mt-4 btn btn-primary"
                  data-nav="admin.dashboard"
                  @click="login()"
                >
                  Login
                </button>
              </form1>
            </div>
          </div>
          <div class="card login-card m-4 bg-secondary text-light">
            <div class="card-body">
              <h5 class="card-title">Supported by</h5>
              <a href="https://www.emids.com/" target="_blank">
                <img
                  style="width: 160px"
                  src="../../public/img/emids-logo.png"
                  class="me-3"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { onMounted, computed, reactive } from "vue";
import { useAuthStore } from "../stores/auth.js";
import router from "../router";

const store = useAuthStore();

let loginDetail = reactive({
  username: "",
  password: "",
});

const userDetails = computed(() => {
  console.log("ours login");
  console.log(JSON.stringify(store.authDetail.data));
  return store.authDetail;
});

onMounted(() => {
  store.authDetail.isAdmin = false;
  store.authDetail.isAaganwadi = false;
  store.authDetail.isNgo = false;
});

const login = async () => {
  console.log("loginDetail" + JSON.stringify(loginDetail));
  await store.getLoginUser(loginDetail);
  console.log("afterlogin");
  if (userDetails.value.isAdmin || userDetails.value.isNgo) {
    router.push("/dashboard");
  }

  if (userDetails.value.isAaganwadi) {
    router.push("/programssummary");
  }
};
</script>
