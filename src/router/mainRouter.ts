import Vue from 'vue';
import Router from 'vue-router';
import adminRoutes from '@/router/adminRoutes'
// import clientRoutes from '@/router/clientRoutes'


var allRoutes: any[] = []
const routes = allRoutes.concat(adminRoutes)


Vue.use(Router);

export default new Router({
  routes:routes
});
