const { createApp } = Vue

const login = createApp({
    data() {
        return {
            username: "",
            password: "",
            test: ""
        }
    }, 
    methods: {
        testFunc() {
            this.test = "username: " + this.username + "\n" + "password: " + this.password
        }
        // 待加入
    },
    watch: {
        username() {
            this.testFunc()
        },
        password() {
            this.testFunc()
        }
    }
}).mount('#login')