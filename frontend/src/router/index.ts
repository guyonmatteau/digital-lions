import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Workshops from '../views/Workshops.vue'
import Home from '../views/Home.vue'
import Children from '../views/Children.vue'
import Communities from '../views/Communities.vue'

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
      component: Home
    },
    {
      path: '/workshops',
      name: 'workshops',
      component: Workshops
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
    }
  ]
})

export default router
