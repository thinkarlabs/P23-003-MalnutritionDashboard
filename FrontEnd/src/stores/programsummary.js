import { defineStore } from "pinia";
// Import axios helper to make HTTP requests
import { HTTP } from "../../http-common";

export const useProgramSummaryStore = defineStore("programsummary", {
  state: () => ({
    programsummaries: [],
    programsummary: "",
  }),
  getters: {
    getProgramSummaries(state) {
      return state.programsummaries;
    },
  },
  actions: {
    async fetchProgramSummaries(aaganwadi_id) {
      try {
        await HTTP.get("get_program_joining_details/" + aaganwadi_id).then(
          (response) => {
            this.programsummaries = response.data;
          }
        );
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async getProgramSummary(id) {
      try {
        await HTTP.get(id + "/get_programsummary").then((response) => {
          this.programsummary = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async postProgramJoining(programJoining) {
      try {
        await HTTP.post("Add_program_joining", programJoining);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
