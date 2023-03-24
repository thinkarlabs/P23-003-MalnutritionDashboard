import { defineStore } from "pinia";
// Import axios helper to make HTTP requests
import { HTTP } from "../../http-common";

export const useDonorsStore = defineStore("donors", {
  state: () => ({
    donors: [],
    donor: "",
  }),
  getters: {
    getDonors(state) {
      return state.donors;
    },
  },
  actions: {
    async fetchDonors() {
      try {
        const data = await HTTP.get("getdonors");
        this.donors = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getDonor(id) {
      try {
        await HTTP.get(id + "/get_donor").then((response) => {
          this.donor = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postDonor(newDonor) {
      try {
        await HTTP.post("donors", newDonor);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateDonor(updatedDonor) {
      try {
        await HTTP.put("donors/" + updatedDonor.value.id, updatedDonor.value);
      } catch (error) {
        debugger;
        alert(error.data);
        console.log(error);
      }
    },
    async deleteDonor(id) {
      try {
        await HTTP.delete("delete_donor/" + id).then(() => {
          this.fetchDonors();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
