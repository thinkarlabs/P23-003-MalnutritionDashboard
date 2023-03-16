import { defineStore } from "pinia";
import { HTTP } from "../../http-common";

export const useMalnutritionDetailStore = defineStore("malnutritiondetail", {
  state: () => ({
    nutritionStats: [],
    currentChildMalnutrition: "",
  }),
  getters: {
    getnutritionStats(state) {
      return state.nutritionStats;
    },
  },
  actions: {
    async fetchNutritionStats() {
      try {
        const data = await HTTP.get("get_child_Malnutritions");
        this.nutritionStats = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getChildMalnutritionHistory(id) {
      try {
        await HTTP.get(id + "/get_child_malnutrition_stats").then(
          (response) => {
            this.currentChildMalnutrition = response.data;
          }
        );
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postNutritionStats(newNutritionStats) {
      try {
        await HTTP.post("childMalnutrion_Add", newNutritionStats);
        // this.fetchNutritionStats();
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
