import {createApp} from 'vue'

const app = createApp({
    data() {
        return {
            rankItems: []
        }
    },
    methods: {
        getData() {
            this.rankItems = [
                {path: "../img/dog.PNG", rank: '1'},
                {path: "../img/pig.PNG", rank: '2'},
                {path: "../img/rabbit.PNG", rank: '3'}
            ]
        },
        getImg(imagePath) {
            return new URL(`${imagePath}`, import.meta.url).href
        }
    },
    mounted() {
        this.getData()
    }
})
app.mount('#app')