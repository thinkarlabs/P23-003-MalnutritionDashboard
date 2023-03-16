import { defineStore } from "pinia";
import { HTTP } from "../../http-common";

export const useSupplmentarySummaryStore = defineStore("SupplmentarySummary", {
  state: () => ({
    childSummaries: [],
  }),
  getters: {
    getchildSummaries(state) {
      return state.childSummaries;
    },
  },
  actions: {
    async fetchChildSummaries() {
      try {
        const childs = await HTTP.get("get_childs");
        const childMalnutritions = await HTTP.get("get_child_Malnutritions");
        console.log(childs.data.data);
        console.log(childMalnutritions.data.data);
        // let filtered = childMalnutritions.filter(malnutrition =>        // filter jsondata
        // childs.every( child =>                // so every member of filter array
        //     child.value.includes(malnutrition[child.id])) )

        // const filteredChildMalnutritions = childMalnutritions.filter(malnutru => )
        // this.childSummaries = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
