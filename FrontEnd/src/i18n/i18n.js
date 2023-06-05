import en from "./en.json";
import fr from "./fr.json";
import hindi from "./hn.json";

import { createI18n } from "vue-i18n";

export default createI18n({
  locale: "fr", // current language
  fallbackLocale: "fr",
  messages: {
    en,
    fr,
    hindi,
  },
});
