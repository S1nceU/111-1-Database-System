import {createApp} from 'vue'
import App from '../view/App.js'
import router from './router.js'
const app = createApp({
    components: {
        App
    },
    data() {
        return {

        }
    }
})
console.log(app)
app.use(router)
app.mount('#app')