import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            registObj: {
                username:'',
                password:''
            },
            confirm_pw:''
        }
    }, 
    methods: {
        async Register() {
            if(this.registObj.password != this.confirm_pw) {
                alert("密碼不一致")
                return
            }
            try {
                let res = await axios.post("http://127.0.0.1:5500/api/Login/RegisterC/", this.registObj)
            }
            catch(err) {
                alert("post error")
            }
        }
    }
})

app.mount('.box')