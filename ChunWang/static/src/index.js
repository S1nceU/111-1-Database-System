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
}).mount('.tt')

const content = createApp({
    data() {
        return {
            searchText: ""
        }
    },
    methods: {
        Search() {
            window.location.replace(`http://127.0.0.1:5000/search/${this.searchText}`)
        },
        serchTag(text) {
            console.log("get in func")
            // this.searchText = text
            // this.Search()
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

const rank = createApp({
    data() {
        return {
            rankItems: []
        }
    },
    methods: {
        getDefaultData() {
            this.rankItems = [
                {path: "../img/dog.PNG", rank: '1'},
                {path: "../img/pig.PNG", rank: '2'},
                {path: "../img/rabbit.PNG", rank: '3'},
                {path: "../img/tiger.PNG", rank: '4'},
                {path: "../img/kangaroo.PNG", rank: '5'},
                {path: "../img/redpanda.PNG", rank: '6'}
            ]
        },     
        getImgPath(path) {
            return new URL(`${path}`, import.meta.url).href
        },
        isFirstRank(rank) {
            if(rank == '1') {
                return "margin-left: 30px;"
            }
            else {
                return ""
            }
        }
    },
    created() {
        this.getDefaultData()
    }
}).mount('.field')