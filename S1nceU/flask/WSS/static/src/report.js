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
                this.logged = false
                return
            }
            this.username = await loginData.username
            this.accountLevel = await loginData.user_level
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
}).mount(".tt")

const report = createApp({
    data() {
        return {
            reportText: ""
        }
    },
    methods: {
        async Report() {
            let res = await axios.post("http://127.0.0.1:5000/add_event/", {content: this.reportText})
            if(res.data == "Report success.") {
                alert("回報成功!")
                window.location.reload()
            }
        }
    }
}).mount('.content')