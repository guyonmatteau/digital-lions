import './assets/main.css'

import { createApp } from 'vue'

import router from './router'
import App from './App.vue'
import store from './stores/index.ts'

const app = createApp(App)

// app.use(createPinia())
app.use(router)
app.use(store)

app.mount('#app')
export { app }
