<template>
  <div id="x-main" class="container-full mt-5 p-3">
    
    <div class="container-md">
      
      <div class="row">
        <div>
          <h1>{{ $t('dashboard.welcomeMsg') }}</h1>
        </div>
        <div class="col-12 p-2">
          <h3 class="float-start ps-2" id = "test">{{ $t('dashboard.malnutrition-dashboard')}} ({{ $t('dashboard.admin') }})</h3>
        </div>
        <div class="col-8 p-2">
          <l-map :zoom="leafletdata.zoom" :center="leafletdata.center">
            <l-tile-layer :url="leafletdata.url"></l-tile-layer>
            <l-marker :lat-lng="leafletdata.marker"></l-marker>
            <l-popup :lat-lng="leafletdata.marker">
              <p>Hello, I'm a popup</p>
            </l-popup>
          </l-map>
        </div>
        <div class="col-4" style="min-height: 420px">
          <div class="card mb-4 rounded-3 shadow-sm">
            <div class="card-header">
              <h4 class="my-0 fw-normal">472 Aanganwadis</h4>
            </div>
            <div class="card-body">
              <h3 class="card-title pricing-card-title">
                2,306
                <small class="text-muted fw-light"
                  >[SAM] <i class="bi bi-arrow-up-circle text-danger"></i> 37
                </small>
              </h3>
              <h3 class="card-title pricing-card-title">
                7,812
                <small class="text-muted fw-light"
                  >[MAM] <i class="bi bi-arrow-down-circle text-success"></i> 123
                </small>
              </h3>
            </div>
          </div>
          <div class="card rounded-3 shadow-sm" style="min-height: 220px">
            <div class="card-header">
              <h4 class="my-0 fw-normal">Detailed</h4>
            </div>
            <div class="card-body">
              <textarea class="m-0 p-0 w-100" style="height: 140px">
  [2022-Week 48] 1,283 SAM | 9,328 MAM
  [2022-Week 47] 1,247 SAM | 12,732 MAM
  [2022-Week 46] 1,252 SAM | 14,328 MAM
  [2022-Week 45] 1,291 SAM | 14,447 MAM
  			</textarea
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
#x-main {
  width: 1280px;
}
</style>
<script setup>
import { reactive } from "vue";
import { LMap, LTileLayer, LMarker, LTooltip } from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
let leafletdata = reactive({
  zoom: 13,
  center: [47.41322, -1.219482],
  url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  marker: [47.41322, -1.219482],
});


</script>
