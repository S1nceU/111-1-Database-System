import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            registObj: {
                account:'',
                password:'',
                ID: '',
                username: '',
                email: '',
                address: '',
                phone: ''
            },
            confirm_pw:'',
            identity: 'buyer'
        }
    }, 
    methods: {
        async Register() {
            //format validattion
            let emailReg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$/
            let IDReg = /^[A-Z]\d{9}/
            let url = ''
            if(this.registObj.account == "") {
                alert("帳號不可為空")
                return
            }
            if(this.registObj.password == "") {
                alert("密碼不可為空")
                return
            }
            if(this.registObj.ID == "") {
                alert("身分證字號不可為空")
                return
            }
            if(this.registObj.username == "") {
                alert("暱稱不可為空")
                return
            }
            if(this.registObj.email == "") {
                alert("電子郵件不可為空")
                return
            }
            if(this.registObj.address == "") {
                alert("地址不可為空")
                return
            }
            if(this.registObj.phone == "") {
                alert("電話不可為空")
                return
            }
            
            if(this.registObj.password != this.confirm_pw) {
                alert("密碼不一致")
                this.registObj.password = ''
                this.confirm_pw = ''
                return
            }

            if(this.registObj.ID == '' || !IDReg.test(this.registObj.ID)) {
                alert("身分證格式有誤")
                this.registObj.ID = ''
                return
            }

            if(this.registObj.email == '' || !emailReg.test(this.registObj.email)){
                alert("電子郵件格式有誤")
                this.registObj.email = ''
                return
            }

            if(this.isBuyer) {
                url = 'http://127.0.0.1:5000/register_c/'
            }
            else {
                url = 'http://127.0.0.1:5000/register_s/'
            }

            let res = await axios.post(url, this.registObj)
            console.log(res.data)
            // 傳送註冊後續事項 (待新增)
            alert("註冊成功！！")
            window.location.replace("http://127.0.0.1:5000/login")
        },
        goLogin() {
            console.log("go Login")
            window.location.replace("http://127.0.0.1:5000/login")
        },
        goHome() {
            console.log("go Home")
            window.location.replace("http://127.0.0.1:5000/home")
        }
    },
    computed: {
        isBuyer() {
            if(this.identity == 'buyer') {
                return true
            }
            else {
                return false
            }
        }
    }
})

app.mount('.whole_page')