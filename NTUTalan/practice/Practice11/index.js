import { createApp } from "vue"
import ChildComp from './ChildComp.js'

const app = createApp({
    components: {
        ChildComp
    }
})
app.mount('#app')