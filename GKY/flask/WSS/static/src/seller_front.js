import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: 'username',
            logged: false,
            accountLevel: '-1'
        }
    },
    methods: {
        async getData() {
            let res = await axios.post("http://127.0.0.1:5000/isLogined/", {})
            let loginData = res.data
            if(loginData == 'False') {
                this.logged = false

                return
            }
            this.username = loginData.username
            this.accountLevel = loginData.user_level
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
}).mount('.tt')

const searchList = createApp({
    data() {
        return {
            username: 'username',
            logged: false,
            accountLevel: '-1',
            addCount: 1
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
            this.username = loginData.username
            this.accountLevel = loginData.user_level
            this.logged = true       
        },
        async addToCart(product_id){
            let res = await axios.post("http://127.0.0.1:5000/cart_add/", 
                {
                    "product_id": product_id,
                    "amount": parseInt(this.addCount) // 之後要修
            })
            if(res.data == 'add success.') {
                alert("加入完成")
            }
            else if(res.data == 'There are the same product in your cart.') {
                alert("您的購物車已有相同的商品")
                window.location.reload()
            }
            else if(res.data == 'Not logged in') {
                alert("請先登入")
                window.location.replace("http://127.0.0.1:5000/login")
            }
        }
    },
    created() {
        this.getData()
    }
}).mount('.content')