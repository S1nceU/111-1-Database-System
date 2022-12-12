import {createApp} from 'vue'


const selectBar = createApp({
    data() {
        return {
            account:'',
            logged: false
        }
    },
    methods: {
        
    },
    computed: {
        text() {
            return '歡迎!' + this.account
        }
    },
    beforeMount() {
        axios.post("url here", {
            msg: ''
        }).then(response=>{
            this.account = response
        }).catch(error=>{
            console.log(error)
            this.account = error
            console.log(this.return)
        })

    }
})

selectBar.mount('.tt')