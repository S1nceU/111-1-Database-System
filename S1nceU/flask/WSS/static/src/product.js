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

const product = createApp({
    data() {
        return {
        }
    },
    methods: {
        async addToCart(){
            console.log("test")
            let pathName = window.location.pathname
            let productID = pathName.split("/")[2]
            let res = await axios.post("http://127.0.0.1:5000/cart_add/", 
                {
                    "product_id": productID,
                    "amount": 1 // 之後要修
            })
            if(await res.data == 'Success') {
                alert("加入完成")
            }
        }
    }
}).mount('.content')