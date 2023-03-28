import { defineStore } from "pinia";
// Import axios to make HTTP requests

import { HTTP } from "../../http-common";

export const useProgramStore = defineStore("program", {
  state: () => ({
    programs: [],
    currentprogram: "",
    supplement: [],
    donor: [],
  }),
  getters: {
    getProgram(state) {
      return state.programs;
    },
  },
  actions: {
    async fetchProgram() {
      try {
        const data = await HTTP.get("get_programs");
        this.programs = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createProgram(createProgram) {
      try {
        await HTTP.post("add_program", createProgram);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updatingProgram(updProgram) {
      try {
        await HTTP.put(
          "update_program/" + updProgram.value.id,
          updProgram.value
        );
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },

    async deleteProgram(id) {
      try {
        await HTTP.delete("delete_program/" + id).then(() => {
          this.fetchProgram();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchProgramById(id) {
      try {
        await HTTP.get("get_program/" + id).then((response) => {
          this.currentprogram = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchSupplement() {
      try {
        const response = await HTTP.get("get_supplements_details");
        this.supplement = response.data;
        console.log("333", this.supplement);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fecthDonor() {
      try {
        await HTTP.get("getdonors").then((response) => {
          this.donor = response.data;
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
