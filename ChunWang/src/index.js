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
            if(res.data == 'False') {
                this.logged = false
                return
            }
            this.username = res.data
            this.logged = true       
            console.log(this.output)
        },
        goLogin() {
            window.location.replace("http://127.0.0.1:5000/login.html")
        },
        Logout() {
            Cookies.remove("WSS")
            // axios.post("http://127.0.0.1:5000/logout/", {})
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
                {path: "../static/img/dog.PNG", rank: '1'},
                {path: "../static/img/pig.PNG", rank: '2'},
                {path: "../static/img/rabbit.PNG", rank: '3'},
                {path: "../static/img/tiger.PNG", rank: '4'},
                {path: "../static/img/kangaroo.PNG", rank: '5'},
                {path: "../static/img/redpanda.PNG", rank: '6'}
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