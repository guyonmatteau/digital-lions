import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Attendance from '../views/Attendance.vue'
import Children from '../views/Children.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        redirect: '/home'
    },
    {
      path: '/home',
      name: 'home',
      component: App
    },
    {
      path: '/attendance',
      name: 'attendance',
      component: Attendance
    },
    {
      path: '/children',
      name: 'children',
      component: Children
    }
  ]
})

export default router
