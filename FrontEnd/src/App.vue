<template>
  <HeaderView></HeaderView>
  <Language></Language>
  <RouterView /><FooterView></FooterView>
</template>

<script setup>
import { RouterView } from "vue-router";
import HeaderView from "../src/components/HeaderView.vue";
import FooterView from "../src/components/FooterView.vue";
import Language from "../src/components/Language.vue";
import { ref, onMounted, computed, reactive } from "vue";
import { useAuthStore } from "../src/stores/auth.js";

const store = useAuthStore();

const logindetail = computed(() => {
  console.log(store.authDetail);
  return store.authDetail;
});
</script>
