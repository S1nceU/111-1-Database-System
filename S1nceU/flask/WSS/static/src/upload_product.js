import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: 'username',
            logged: false,
            accountLevel: ''
        }
    },
    methods: {
        async getData() {
            let res = await axios.post("http://127.0.0.1:5000/isLogined/", {})
            if(res.data == 'False') {
                this.logged = false
                return
            }
            this.username = res.data
            this.logged = true       
        },
        Logout() {
            Cookies.remove("WSS")
            this.logged = false
            alert("Log out ~")
            this.goHome()
        },
        goLogin() {
            window.location.replace("http://127.0.0.1:5000/login")
        },
        goHome() {
            window.location.replace("http://127.0.0.1:5000/home")
        },
        goSeller() {
            window.location.replace("http://127.0.0.1:5000/seller")
        },
        goOrder() {
            window.location.replace("http://127.0.0.1:5000/order")
        },
        goCart() {
            window.location.replace("http://127.0.0.1:5000/cart")
        },
        goMember() {
            if(!this.logged) {
                alert("請先登入")
                this.goLogin()
                return
            }
            else {
                window.location.replace("http://127.0.0.1:5000/member")
            }
        },
        goRegister() {
            window.location.replace("http://127.0.0.1:5000/register")
        }
    },
    computed:{
        welcome() {
            return "歡迎!" + this.username
        }
    },
    created() {
        this.getData()
    }
})
selectBar.mount('.tt')