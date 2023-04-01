<template><HeaderView></HeaderView> <RouterView /><FooterView></FooterView></template>

<script setup>
import { RouterView } from "vue-router";
import HeaderView from "../src/components/HeaderView.vue";
import FooterView from "../src/components/FooterView.vue";
</script>
