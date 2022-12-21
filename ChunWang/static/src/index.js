import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: 'username',
            logged: false
        }
    },
    methods: {
        async getData() {
            let res = await axios.post("http://127.0.0.1:5000/isLogined/", {})

            if(await res.data == 'False') {
                this.logged = false
                return
            }
            let data = await res.data
            this.username = await data.username
            let accountLevel = await data.user_level
            this.logged = true    
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
            console.log(this.rankItems)
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
})

rank.mount('.field')
selectBar.mount('.tt')