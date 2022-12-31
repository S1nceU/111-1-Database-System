import { createApp } from 'vue'

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

const search = createApp({
    data() {
        return {
            searchText: ""
        }
    },
    methods: {
        Search() {
            window.location.replace(`http://127.0.0.1:5000/search/${this.searchText}`)
        }
    }
}).mount('.search')

const suggestion = createApp({
    data() {return {}},
    methods: {
        searchTag(text) {
            console.log("get in func")
            console.log(text)
            window.location.replace(`http://127.0.0.1:5000/search/${text}`)
        }
    }
}).mount('.suggest_row')