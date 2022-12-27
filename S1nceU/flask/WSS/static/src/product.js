import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: 'username',
            logged: false,
            accountLevel: '',
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
            addCount: '1'
        }
    },
    methods: {
        async addToCart(){
            let pathName = window.location.pathname
            let productID = pathName.split("/")[2]
            let res = await axios.post("http://127.0.0.1:5000/cart_add/", 
                {
                    "product_id": productID,
                    "amount": parseInt(this.addCount) // 之後要修
            })
            if(res.data == 'add success.') {
                alert("加入完成")
            }
            else if(res.data == 'There are the same product in your cart.') {
                alert("您的購物車已有相同的商品")
                window.location.replace("http://127.0.0.1:5000/login")
            }
            else if(res.data == 'not logged in') {
                alert("請先登入")
                window.location.replace("http://127.0.0.1:5000/login")
            }
        },
    }
}).mount('.content')