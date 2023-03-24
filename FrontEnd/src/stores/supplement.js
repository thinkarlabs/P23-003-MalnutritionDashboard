import { defineStore } from "pinia";
// Import axios helper to make HTTP requests
import { HTTP } from "../../http-common";


export const useSupplementStore = defineStore("ngo", {
  state: () => ({
    supplements: [],
    supplement: "",
  }),
  getters: {
    getNgos(state) {
      return state.supplements;
    },
  },
  actions: {
    async fetchSupplements() {
      try {
        const data = await HTTP.get("get_supplements_details");
        this.supplements = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getSupplement(id) {
      try {
        await HTTP.get(id + "/get_supplement_details").then((response) => {
          this.supplement = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postSupplement(newSupplement) {
      try {
        await HTTP.post("add_supplement_details", newSupplement);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateSupplement(updatedSupplement) {
      try {
        await HTTP.put("update_supplement_details/" + updatedSupplement.value.id, updatedSupplement.value);
      } catch (error) {
        debugger;
        alert(error.data);
        console.log(error);
      }
    },
    async deleteSupplement(id) {
      try {
        await HTTP.delete("delete_supplement_details/" + id).then(() => {
          this.fetchSupplements();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
