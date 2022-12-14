import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: "",
            logged: false,
            testdata: "testing"
        }
    },
    methods: {
        // async getData() {
        //     let res = await axios.post("http://127.0.0.1:5000/isLogined/", {})
        //     if(res.data == 'False') {
        //         this.logged = false
        //         return 'None'
        //     }
        //     this.logged = true
        //     console.log(typeof(JSON.stringify(res.data)))
        //     console.log(typeof(res.data))
        //     return JSON.stringify(res.data)
        // }
    },
    computed:{
        welcome() {
            return "歡迎!" + this.username
        }
    },
    created() {
        axios.post("http://127.0.0.1:5000/isLogined/", {})
            .then(res => {
                this.username = res.data
                this.logged = true
            })
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