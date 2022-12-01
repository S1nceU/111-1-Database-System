import { createApp } from 'vue/dist/vue.esm-bundler.js'
import Cookies from 'js-cookies'
import axios from 'axios'

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
            if(usname !== '' && uspw !== '') {
                this.loginForm.token = token
            }
            else {
                alert("Error")
            }
            try{
                let req = await axios.post('http://127.0.0.1:5173/login.html', 
                {  
                    username: this.loginForm.username,
                    password: this.loginForm.password
                })    
            }
            catch(err) {
                alert("Error")
            }
            //Cookies.set('login', JSON.stringify(this.loginForm), {expires: true})
            console.log(this.loginForm)
            // if(Cookies.get('login') && this.loginForm.token) {
            //     this.$router.push({name: 'Dashboard'})
            // }           
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