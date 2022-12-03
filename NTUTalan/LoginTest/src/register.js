import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            username:'',
            password:'',
            confirm_pw:''
        }
    }, 
    methods: {
        async btn_register() {
            if(this.password != this.confirm_pw) {
                alert("密碼不一致")
            }
            
        }
    }
})

app.mount('#app')