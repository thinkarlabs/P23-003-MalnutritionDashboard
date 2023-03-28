  import { defineStore } from "pinia";
// Import axios to make HTTP requests

import { HTTP } from "../../http-common";

export const useAanganwadiStore = defineStore("aanganwadi", {
  state: () => ({
    aanganwadies: [],
    currentAanganwadi: "",
  }),
  getters: {
    getAanganwadies(state) {
      return state.aanganwadies;
    },
  },
  actions: {
    async fetchAanganwadies() {
      try {
        const data = await HTTP.get("getAanganwadis");
        this.aanganwadies = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postAanganwadi(newAanganwadi) {
      console.log("saving aanganwadi :: "+JSON.stringify(newAanganwadi));
      try {
        await HTTP.post("addAanganwadi", newAanganwadi);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateAanganwadi(newAanganwadi) {
      console.log("Updating Aanganwadi with ID ::  "+newAanganwadi.value.id);
      try {
        await HTTP.put("updateAanganwadi/" + newAanganwadi.value.id,newAanganwadi.value);
      } catch (error) {
        debugger;
        alert(error);
        console.log(error);
      }

    },
    
    async deleteAanganwadi(id) {
      try {
        await HTTP.delete("delete_aanganwadi/" + id).then(() => {
          this.fetchAanganwadies();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getAanganwadi(id) {
      try {
        await HTTP.get(id + "/get_aanganwadi").then((response) => {
          this.currentAanganwadi = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  
});
