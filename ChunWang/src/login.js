import { createApp } from 'vue'/*'vue/dist/vue.esm-bundler.js'*/

const app = createApp({
    data() {
        return {
            loginForm: {
                username: '',
                password: '',
                token: ''
            }          
        }
    },
    methods: {      

        async Login() {
            console.log("get in func")
            const token = 'abcdefghijklmnop'
            let usname = this.loginForm.username
            let uspw = this.loginForm.password
            console.log(this.loginForm)

            if(usname !== '' && uspw !== '') {
                this.loginForm.token = token
                console.log('get in if')
            }
            else {
                alert("Error")
            }

            // 帳號登入處理
            let res = await axios.post('http://127.0.0.1:5500/api/Login/loginC/', 
            {  
                username: this.loginForm.username,
                password: this.loginForm.password
            })
            console.log(res)
            console.log(JSON.stringify(res))

            Cookies.set('login', JSON.stringify(this.loginForm), {expires: 1})
                   
        },

        removeCookie() {
            Cookies.remove('login')
        }
    },
    watch: {
        username() {
            console.log(`${this.username}`)
        },
        password() {
            console.log(`${this.password}`)
        }  
    }
})
app.mount('.box')