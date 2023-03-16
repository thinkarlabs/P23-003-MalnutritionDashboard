import { defineStore } from "pinia";
// Import axios to make HTTP requests
import axios from "axios";

export const useAanganwadiStore = defineStore("aanganwadi", {
  state: () => ({
    aanganwadies: [],
  }),
  getters: {
    getAanganwadies(state) {
      return state.aanganwadies;
    },
  },
  actions: {
    async fetchAanganwadies() {
      try {
        const data = await axios.get("http://127.0.0.1:7000/api/getAanganwadis");
        this.aanganwadies = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postAanganwadi(newAanganwadi) {console.log("aanganwadi.js :: "+JSON.stringify(newAanganwadi));
      try {
        await axios.post("http://127.0.0.1:7000/api/addAanganwadi", newAanganwadi);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateAanganwadi(newAanganwadi) {
    console.log("EDITING Aanganwadi :: "+id);
      try {
        await axios
          .put("http://127.0.0.1:7000/api/updateAanganwadi/", newAanganwadi)
          .then(() => {
            this.fetchAanganwadies();
          });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    
    async deleteAanganwadi(id) {
      try {
        await axios
          .delete("http://127.0.0.1:7000/api/delete_aanganwadi/" + id)
          .then(() => {
            this.fetchAanganwadies();
          });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getAanganwadi(id) {
      try {
        const data = await axios.get("http://127.0.0.1:7000/api/"+id+"/get_aanganwadi/");
        console.log(JSON.stringify(data));
        this.aanganwadies = data.data;
        return this.aanganwadies;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  
});
