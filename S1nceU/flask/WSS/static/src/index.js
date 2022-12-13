import {createApp} from 'vue'

const selectBar = createApp({
    data() {
        return {
            username: '',
            logged: false,
            output: ''
        }
    },
    methods: {
        async getData() {
            let res = await axios.post("http://127.0.0.1:5000/isLogined/", {})
            if(res.data == 'False') {
                this.logged = false
                return
            }
            document.getElementById("username").innerHTML = "歡迎!" + res.data
            this.username = res.data
            this.logged = true
            this.output = '歡迎!' + this.username 
            
            console.log(this.output)
        }
    },
    beforeUpdated() {
        this.getData()
    }
})

selectBar.mount('.tt')