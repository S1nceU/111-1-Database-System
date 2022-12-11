// import module
// import * as Vue from 'vue'
//import { createRouter, createWebHistory } from 'vue-router'
//import { createRouter } from "vue-router"

// pages...
import Home from '../components/Home.js'
import Contact from '../components/Contact.js'

// setting
const routes = [
    {
        path: '/',
        name: Home,
        component: Home
    },
    {
        path: '/contact',
        name: Contact,
        component: Contact
    }
]
const router =  VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes: routes
})

export default router