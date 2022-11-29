const { createApp } = Vue
let id = 0
const list = createApp({
    data() {
        return {
            newItem: '',
            isHide: false, 
            items: [
                {id: id++, text: 'test01', done: false},
                {id: id++, text: 'test02', done: false}
            ]
        }
    },
    methods: {
        addItem() {
            this.items.push({
                text: this.newItem,
                id: id++,
                done: false
            })
            this.newItem=''
        },
        removeItem(item) {
            this.items = this.items.filter((e) => e.id != item.id) 
        },
    },
    computed: { 
        //計算屬性，它的值由其他屬性計算而來
        filterItems() {
            if(this.isHide) {
                return this.items.filter((e) => e.done == false)
            }
            return this.items
        }
    }
})
list.mount('#list')