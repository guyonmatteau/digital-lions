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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Attendance.vue')
    },
    {
      path: '/children',
      name: 'children',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Children.vue')
    }
  ]
})

export default router
