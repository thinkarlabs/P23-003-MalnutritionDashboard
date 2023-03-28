import { defineStore } from "pinia";
import { HTTP } from "../../http-common";

export const useSupplmentarySummaryStore = defineStore("SupplmentarySummary", {
  state: () => ({
    childSummaries: [],
  }),
  getters: {
    getchildSummaries(state) {
      return state.childSummaries;
    },
  },
  actions: {
    async fetchChildSummaries() {
      try {
        const childs = await HTTP.get("get_childs");
        const childMalnutritions = await HTTP.get("get_child_Malnutritions");
        console.log(childs.data.data);
        //let loadedChildren = JSON.parse(childs.data.data);
        let loadedChildren = childs.data.data;
        let modifedChildren = [];

        for (let i in loadedChildren) {
          let sex = "";
          let parentName = "";
          if (loadedChildren[i].gender == "Male") {
            sex = "M";
            parentName = "S/O " + loadedChildren[i].motherName;
          } else {
            sex = "F";
            parentName = "D/O " + loadedChildren[i].motherName;
          }
          loadedChildren[i].gender = sex;
          loadedChildren[i].motherName = parentName;

          let filteredChildMalnutritions = childMalnutritions.data.data.find(
            (element) => {
              // console.log("element" + JSON.stringify(element));
              // console.log("modifed element id" + loadedChildren[i].id);
              return element.child_id == loadedChildren[i].id;
            }
          );
          if (filteredChildMalnutritions) {
            console.log(
              "filteredChildMalnutritions.malnutritionIndexCategory " +
                filteredChildMalnutritions.malnutritionIndexCategory
            );
            if (
              filteredChildMalnutritions.malnutritionIndexCategory === "Normal"
            ) {
              loadedChildren[i].index = "bg-success";
              console.log("updatedindexsuccess " + loadedChildren[i].index);
            }
            if (
              filteredChildMalnutritions.malnutritionIndexCategory === "MAM"
            ) {
              loadedChildren[i].index = "bg-warning";
              console.log("updatedindexwarning " + loadedChildren[i].index);
            }
            if (
              filteredChildMalnutritions.malnutritionIndexCategory === "SAM"
            ) {
              loadedChildren[i].index = "bg-danger";
            }

            loadedChildren[i].height =
              filteredChildMalnutritions.height + " cms";
            loadedChildren[i].weight =
              filteredChildMalnutritions.weight + " kgs";
            loadedChildren[i].statdate = new Date(
              filteredChildMalnutritions.date
            )
              .toLocaleDateString("en-GB", {
                day: "numeric",
                month: "short",
                year: "numeric",
              })
              .replace(/ /g, "-");
          }
          modifedChildren.push(loadedChildren[i]);
        }
        this.childSummaries = modifedChildren;
        console.log(
          "Actual ChildMalnutrition data: " +
            JSON.stringify(childMalnutritions.data.data)
        );
        console.log(
          "this.childSummaries" + JSON.stringify(this.childSummaries)
        );
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
