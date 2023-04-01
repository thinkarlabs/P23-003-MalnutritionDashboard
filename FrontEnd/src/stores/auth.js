import { defineStore } from "pinia";
import { HTTP } from "../../http-common";
//childStore
export const useAuthStore = defineStore("auth", {
  state: () => ({
    authDetail: {
      isAdmin: true,
      isNgo: false,
      isAaganwadi: false,
    },
  }),
  actions: {
    async getChild(id) {
      try {
        await HTTP.get(id + "/get_child").then((response) => {
          this.child = response.data.data[0];
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
