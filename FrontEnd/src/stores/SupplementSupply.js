import { defineStore } from "pinia";
import { HTTP } from "../../http-common";

export const useSupplementSupplyStore = defineStore("supplementsupply", {
  state: () => ({
    supplySchedules: "",
  }),
  actions: {
    async getSupplyScheduleHistory(program_joining_id) {
      try {
        await HTTP.get("/get_all_supplemet_packs/" + program_joining_id).then(
          (response) => {
            this.supplySchedules = response.data;
          }
        );
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postSupplementSupplyDetail(newSupplementSupplyDetail) {
      try {
        await HTTP.post("add_supplement_pack", newSupplementSupplyDetail);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
