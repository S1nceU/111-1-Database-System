const {createApp} = Vue
const {VueResourse} = vue-resourse

const app = createApp({
    data(){
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        btn_login() {
            this.$http.get("http://localhostURL/user="+`${this.username}`+"&pw="+`${this.password}`)
            .then((res) => {
                alert("test success")
            })
            .catch((err) => {
                alert("test fail")
            })
        }
    }
})
app.use(VueResourse)
app.mount('#app')