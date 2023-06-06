<template>
  <div id="admin" v-if="logindetail.isAdmin">
    <div id="x-header">
      <nav class="navbar navbar-expand navbar-dark fixed-top bg-dark p-1">
        <div class="container-fluid">
          <img src="https://www.asthrasoft.com/site/img/logo.png" style="height: 25px" />
          <p class="navbar-brand my-0 ms-2">Think Nutrition</p>
          <a class="float-start ps-2" href="#" @click.prevent="changeLocale">{{ currentLocale }}</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav ms-auto">
              
              <li class="nav-item">
                <router-link
                  class="nav-link active"
                  aria-current="page"
                  data-nav="admin.dashboard"
                  to="/"
                  >Dashboard</router-link
                >
              </li>
              <li class="nav-item dropdown">
                <router-link
                  class="nav-link dropdown-toggle"
                  to="#"
                  id="dropdown03"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                  ><i class="bi bi-gear"></i
                ></router-link>
                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdown03">
                  <li>
                    <router-link class="dropdown-item" to="/ngos" data-nav="admin.ngos"
                      >NGOs</router-link
                    >
                  </li>
                  <li>
                    <router-link class="dropdown-item" to="/Aanganwadis"
                      >Aanganwadis</router-link
                    >
                  </li>
                  <li><hr class="dropdown-divider" /></li>
                  <li>
                    <a class="dropdown-item" data-nav="settings">Settings</a>
                  </li>
                  <li>
                    <a class="dropdown-item" data-nav="profile">Profile</a>
                  </li>
                  <li>
                    <router-link to="/" class="dropdown-item" data-nav="web.login" id = "logout"
                      >Logout</router-link
                    >
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
  <div id="ngo" v-if="logindetail.isNgo">
    <div id="x-header">
      <nav class="navbar navbar-expand navbar-dark fixed-top bg-dark p-1">
        <div class="container-fluid">
          <img src="https://www.asthrasoft.com/site/img/logo.png" style="height: 25px" />
          <p class="navbar-brand my-0 ms-2">Think Nutrition</p>

          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <router-link
                  class="nav-link active"
                  to="/"
                  aria-current="page"
                  data-nav="ngo.dashboard"
                  >Dashboard</router-link
                >
              </li>
              <li class="nav-item">
                <router-link
                  class="nav-link active"
                  to="/programs"
                  aria-current="page"
                  data-nav="ngo.programs"
                  >Programs</router-link
                >
              </li>
              <li class="nav-item dropdown">
                <router-link
                  class="nav-link dropdown-toggle"
                  to="#"
                  id="dropdown03"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                  ><i class="bi bi-gear"></i
                ></router-link>
                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdown03">
                  <li>
                    <router-link class="dropdown-item" to="/donors" data-nav="ngo.donors"
                      >Donors</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item"
                      to="/supplements"
                      data-nav="ngo.supplements"
                      >Supplements</router-link
                    >
                  </li>
                  <li><hr class="dropdown-divider" /></li>
                  <li>
                    <a class="dropdown-item" data-nav="settings">Settings</a>
                  </li>
                  <li>
                    <a class="dropdown-item" data-nav="profile">Profile</a>
                  </li>
                  <li>
                    <router-link to="/" class="dropdown-item" data-nav="web.login"
                      >Logout</router-link
                    >
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
  <div id="Aaganwadi" v-if="logindetail.isAaganwadi">
    <div id="x-header">
      <nav class="navbar navbar-expand navbar-dark fixed-top bg-dark p-1">
        <div class="container-fluid">
          <!--<img src="https://www.asthrasoft.com/site/img/logo.png" style="height:25px"/>-->
          <p class="navbar-brand my-0">Think Nutrition</p>

          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <router-link
                  class="nav-link active"
                  to="/programssummary"
                  aria-current="page"
                  data-nav="mob.home"
                  ><i class="bi bi-calendar-check"></i
                ></router-link>
              </li>
              <li class="nav-item">
                <router-link
                  to="/childsupplementarysummary"
                  class="nav-link active"
                  aria-current="page"
                  data-nav="mob.kids"
                  ><i class="bi bi-graph-up"></i
                ></router-link>
              </li>
              <li class="nav-item">
                <router-link to="/" class="dropdown-item" data-nav="web.login"
                  ><i class="bi bi-box-arrow-right"></i
                ></router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, reactive } from "vue";
import { useAuthStore } from "../stores/auth.js";

const store = useAuthStore();

const logindetail = computed(() => {
  console.log(store.authDetail);
  return store.authDetail;
});
</script>
