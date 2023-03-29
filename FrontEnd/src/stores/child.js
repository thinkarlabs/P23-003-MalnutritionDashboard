import { defineStore } from "pinia";
import { HTTP } from "../../http-common";
//childStore
export const useChildStore = defineStore("child", {
  state: () => ({
    childs: [],
    child: "",
  }),
  getters: {
    getchilds(state) {
      return state.childs;
    },
  },
  actions: {
    async fetchChilds() {
      try {
        const data = await HTTP.get("get_childs");
        this.kids = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
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
    async postchild(newChild) {
      try {
        await HTTP.post("add_child", newChild);
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async updateChild(Child) {
      try {
        await HTTP.put("updatechild/" + Child.value.id, Child.value);
      } catch (error) {
        alert(error.data);
        console.log(error);
      }
    },
    async deleteChild(id) {
      try {
        await HTTP.delete("deleteChild/" + id).then(() => {
          this.fetchNgos();
        });
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
