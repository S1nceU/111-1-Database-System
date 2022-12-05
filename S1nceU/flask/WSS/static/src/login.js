import { createApp } from 'vue'/*'vue/dist/vue.esm-bundler.js'*/

const app = createApp({
    data() {
        return {
            loginForm: {
                account: '',
                password: '',
                token: ''
            }          
        }
    },
    methods: {       
        async Login() {
            console.log("get in func")
            const token = 'abcdefghijklmnop'
            let usname = this.loginForm.account
            let uspw = this.loginForm.password
            console.log(this.loginForm)

            if(usname !== '' && uspw !== '') {
                this.loginForm.token = token
                console.log('get in if')
            }
            else {
                alert("Error")
            }
            
            try{
                console.log("to post")
                let res = await axios.post('http://127.0.0.1:5000/login/', 
                {  
                    account: this.loginForm.account,
                    password: this.loginForm.password
                })
                await res.then   
            }
            catch(err) {
                alert("Post Error or 帳號密碼錯誤")
            }

            Cookies.set('login', JSON.stringify(this.loginForm), {expires: 1})
        
        },
        removeCookie() {
            Cookies.remove('login')
        }
    },
    watch: {
        account() {
            console.log(`${this.account}`)
        },
        password() {
            console.log(`${this.password}`)
        }  
    }
})
app.mount('.box')