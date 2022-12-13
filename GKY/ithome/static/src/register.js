import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            registObj: {
                username:'',
                password:'',
                ID: '',
                Name: '',
                email: '',
                address: '',
                phone: ''
            },
            confirm_pw:''
        }
    }, 
    methods: {
        async Register() {
            //format validattion
            let emailReg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$/
            let IDReg = /^[A-Z]\d{9}/

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

            try {
                let res = await axios.post("http://127.0.0.1:8000/register/", this.registObj)
            }
            catch(err) {
                alert("post error")
            }
        }
    }
})

app.mount('.box')