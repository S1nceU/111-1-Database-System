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
            let loginData = await res.data
            if(loginData == 'False') {
                alert("請先登入")
                this.logged = false
                this.goLogin()
                return
            }
            this.username = await loginData.username
            this.accountLevel = await loginData.user_level
            this.logged = true    
            if(accountLevel != '2') {
                alert("您沒有權限")
                this.goHome()
            }
        },
        Logout() {
            Cookies.remove("WSS", {path: ''})
            this.logged = false
            window.location.reload()
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
            window.location.replace("http://127.0.0.1:5000/member")
        },
        goRegister() {
            window.location.replace("http://127.0.0.1:5000/register")
        },
        goAdmin() {
            window.location.replace("http://127.0.0.1:5000/admin")
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