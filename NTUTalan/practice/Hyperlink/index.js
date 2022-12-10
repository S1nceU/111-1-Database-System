import {createApp} from 'vue'

let resStr = ''
const app = createApp({
    data() {
        return {
            href: 'https://www.google.com.tw'
        }
    },
    methods: {
        test() {
            window.location.replace('./test.html')
        }
    },
    beforeMount() {
        axios.post("url here", {
            msg: ''
        }).then(res=>{
            resStr = res
        }).catch(err=>{
            console.log(err)
        })
    }
})
app.mount('#app')