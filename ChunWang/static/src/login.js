import { createApp } from 'vue'/*'vue/dist/vue.esm-bundler.js'*/

const app = createApp({
    data() {
        return {
            loginForm: {
                account: '',
                password: ''
            },
            identity: 'buyer'   
        }
    },
    methods: {      
        async Login() {
            let url = ''
            if(this.loginForm.account == "") {
                alert("帳號不可為空")
                return
            }
            if(this.loginForm.password == "") {
                alert("密碼不可為空")
                return
            }
            console.log(this.loginForm)
            // 帳號登入處理
            if(this.isBuyer) {
                url = 'http://127.0.0.1:5000/login_c/'
            }
            else {
                url = 'http://127.0.0.1:5000/login_s/'
            }

            let res = await axios.post(url, this.loginForm)
            
            if(res.data == '0') {
                alert("查無帳號")
                return
            }
            
            if(res.data == '1') {
                alert("帳號或密碼錯誤")
                return
            }

            if(res.data == 'Account has been disabled!!') {
                alert("帳號已被停用")
                return
            }
            
            // 執行登入後相關事宜
            if(res.data == "seller") {
                this.goSeller()
                return
            }

            if(res.data == "customer") {
                this.goHome()
                return
            }

            if(res.data == "admin") {
                this.goAdmin()
                return
            }
        },
        goRegister() {
            window.location.replace("http://127.0.0.1:5000/register")
        },
        goHome() {
            window.location.replace("http://127.0.0.1:5000/home")
        },
        goSeller() {
            window.location.replace("http://127.0.0.1:5000/seller")
        },
        goAdmin() {
            window.location.replace("http://127.0.0.1:5000/admin")
        }
    },
    computed: {
        isBuyer() {
            if(this.identity == 'buyer') {
                return true
            }
            else {
                return false
            }
        }
    }
})
app.mount('.whole_page')