const { createApp } = Vue

const app = createApp({
    data() {
        return {
            todoID: 1,
            todoData: null
        }
    },
    methods: {
        async fetchData() {
            this.todoData = null
            const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${this.todoID}`)
            this.todoData = await response.json()
        }
    },
    mounted() {
        this.fetchData()
    },
    watch: {
        todoID() { // todoID++後(todoID改變)執行
            this.fetchData()
        }
    }
}).mount('#app')