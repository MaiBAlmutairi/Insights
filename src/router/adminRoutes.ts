import AdminHome from '@/views/adminRoutes/AdminHome.vue';
import SamaPage from '@/views/adminRoutes/SamaPage.vue';
import OperationPage from '@/views/adminRoutes/OperationPage.vue';
const routes = [
    {
      path: '/',
      name: 'home',
      component: AdminHome
    },
    {
      path: '/sama',
      name: 'sama',
      component: SamaPage
    },
    {
      path: '/operation',
      name: 'operation',
      component: OperationPage
    }
]

export default routes