//import { createApp } from "vue" -待查詢
const { createApp } = Vue
let id = 0
const list = createApp({
    data() {
        return {
            newItem: '',
            items: [
                {id: id++, text: 'test01'},
                {id: id++, text: 'test02'}
            ]
        }
    },
    methods: {
        addItem() {
            this.items.push({
                text: this.newItem+"["+id.toString()+"]",
                id: id++
            })
            this.newItem=''
        },
        removeItem(item) {
            this.items = this.items.filter((e) => e.id != item.id) //!!!arrow fuction不能加大括號 !
        }
    }
})
list.mount('#list')