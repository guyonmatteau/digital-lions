import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      authenticated: false
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
    }
  }
})

export default store
