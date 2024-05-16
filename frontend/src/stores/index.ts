import { createStore } from 'vuex'

interface NotificationState {
  message: string
  type: 'success' | 'error' | ''
}

const store = createStore({
  state() {
    return {
      authenticated: false,
      notification: {
        message: '',
        type: ''
      }
    }
  },
  mutations: {
    login(state) {
      state.authenticated = true
      console.log('Logging in')
    },
    logout(state) {
      state.authenticated = false
      console.log('Logging out')
    },
    setNotification(state, payload: NotificationState) {
      state.notification = payload
    },
    clearNotification(state) {
      state.notification = {
        message: '',
        type: ''
      }
    }
  },
  actions: {
    triggerNotification({ commit }, payload: NotificationState) {
      commit('setNotification', payload)
      setTimeout(() => {
        commit('clearNotification')
      }, 3000)
    }
  }
})

export default store
