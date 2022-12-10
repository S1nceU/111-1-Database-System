import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            href: 'https://www.google.com.tw'
        }
    },
    methods: {
        test() {
            window.location.replace(this.href)
        }
    }
})
app.mount('#app')