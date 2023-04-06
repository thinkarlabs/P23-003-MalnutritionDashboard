import { defineStore } from "pinia";
import { HTTP } from "../../http-common";
//childStore
export const useAuthStore = defineStore("auth", {
  state: () => ({
    authDetail: {
      isAdmin: false,
      isNgo: false,
      isAaganwadi: false,
      userName: "",
    },
  }),
  actions: {
    async getLoginUser(requestUserDetail) {
      try {
        await HTTP.post("isvaliduser", requestUserDetail).then((response) => {
          this.authDetail.userName = response.data.data.userName;
          switch (response.data.data.user_type) {
            case "admin":
              this.authDetail.isAdmin = true;
              break;
            case "ngo":
              this.authDetail.isNgo = true;
              break;
            case "aaganwadi":
              this.authDetail.isAaganwadi = true;
              break;
          }
          return this.authDetail;
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
