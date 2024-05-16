import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Workshops from '../views/Workshops.vue'
import Home from '../views/Home.vue'
import Children from '../views/Children.vue'
import Communities from '../views/Communities.vue'
import Attendance from '../views/Attendance.vue'
import Login from '../views/Login.vue'
import store from '../stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      children: [
        {
          path: 'workshops',
          name: 'Workshops',
          component: Workshops
        },
        {
          path: 'children',
          name: 'Children',
          component: Children
        },
        {
          path: 'communities',
          name: 'Communities',
          component: Communities
        },
        {
          path: 'attendance',
          name: 'Attendance',
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

router.beforeEach(function (to, from, next) {
  if (to.path !== '/login' && to.path !== 'login' && !store.state.authenticated) {
    next({ path: '/login' })
  } else if ((to.path === '/login' || to.path === 'login') && store.state.authenticated) {
    next({ path: '/' })
  } else {
    next()
  }
})

export default router
