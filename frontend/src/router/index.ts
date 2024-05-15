import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Workshops from '../views/Workshops.vue'
import Home from '../views/Home.vue'
import Children from '../views/Children.vue'
import Communities from '../views/Communities.vue'
import Attendance from '../views/Attendance.vue'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      children: [
        {
          path: '/workshops',
          name: 'workshops',
          component: Workshops,
          auth: true
        },
        {
          path: '/children',
          name: 'children',
          component: Children
        },
        {
          path: '/communities',
          name: 'communities',
          component: Communities
        },
        {
          path: '/attendance',
          name: 'attendance',
          component: Attendance
        }
      ]
    },
    { 
      path: '/login', 
      name: 'Login', 
      component: Login 
    }
  ]
})

export default router
