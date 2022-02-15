import Vue from 'vue';
import App from './App.vue';
import router from './router/mainRouter';

import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


import Multiselect from 'vue-multiselect'
// register globally
Vue.component('multiselect', Multiselect)

import DataTable from "@andresouzaabreu/vue-data-table";
import "bootstrap/dist/css/bootstrap.min.css";
import "@andresouzaabreu/vue-data-table/dist/DataTable.css";







Vue.config.productionTip = false;
Vue.component("data-table", DataTable);

new Vue({
  router,
  // store,
  render: (h) => h(App),
}).$mount('#app');
