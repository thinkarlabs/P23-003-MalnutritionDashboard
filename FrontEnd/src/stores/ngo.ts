import { defineStore } from "pinia";
// Import axios to make HTTP requests
import axios from "axios";

export const useNgoStore = defineStore("ngo", {
  state: () => ({
    ngos: [],
  }),
  getters: {
    getNgos(state) {
      return state.ngos;
    },
  },
  actions: {
    async fetchNgos() {
      try {
        const data = await axios.get("http://127.0.0.1:7000/getNgos");
        this.ngos = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postNgo(newNgo) {
      try {
        await axios.post("http://127.0.0.1:7000/addNgo", newNgo);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async deleteNgo(id) {
      try {
        await axios
          .delete("http://127.0.0.1:7000/delete_ngo/" + id)
          .then(() => {
            this.fetchNgos();
          });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
