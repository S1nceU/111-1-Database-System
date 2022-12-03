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
            if(this.password != this.confirm_pw) {
                alert("密碼不一致")
            }
            try {
                let res = await axios.post("Api url here", this.registObj)
            }
            catch(err) {
                alert("post error")
            }
        }
    }
})

app.mount('.box')