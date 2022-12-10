import { createApp } from 'vue'/*'vue/dist/vue.esm-bundler.js'*/

const app = createApp({
    data() {
        return {
            loginForm: {
                account: '',
                password: ''
            },
            identity: ''   
        }
    },
    methods: {      
        async Login() {
            let url = ''
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

            // 執行登入後相關事宜
            console.log('Login success')

            Cookies.set('login', JSON.stringify(this.loginForm), {expires: 1})
                   
        },

        removeCookie() {
            Cookies.remove('login')
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
app.mount('.box')