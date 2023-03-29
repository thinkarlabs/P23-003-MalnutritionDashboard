import { defineStore } from "pinia";
// Import axios helper to make HTTP requests
import { HTTP } from "../../http-common";

export const useNgoStore = defineStore("ngo", {
  state: () => ({
    ngos: [],
    ngo: "",
  }),
  getters: {
    getNgos(state) {
      return state.ngos;
    },
  },
  actions: {
    async fetchNgos() {
      try {
        const data = await HTTP.get("getNgos");
        this.ngos = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getNgo(id) {
      try {
        await HTTP.get(id + "/get_ngo").then((response) => {
          this.ngo = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postNgo(newNgo) {
      try {
        await HTTP.post("create_ngo", newNgo);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateNgo(updatedNgo) {
      try {
        await HTTP.put("ngos/" + updatedNgo.value.id, updatedNgo.value);
      } catch (error) {
        alert(error.data);
        console.log(error);
      }
    },
    async deleteNgo(id) {
      try {
        await HTTP.delete("delete_ngo/" + id).then(() => {
          this.fetchNgos();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
