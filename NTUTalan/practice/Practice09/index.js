const { createApp } = Vue

const app = createApp({
    mounted() {
        this.$refs.p.textContent = 'test'
    }
})

app.mount('#app')