import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "../Main/App.vue";
import router from "../Main/router";

import "../../src/assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
