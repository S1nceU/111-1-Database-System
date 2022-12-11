// import module
import { createRouter, createWebHistory } from 'vue-router'

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
export const router = createRouter({
    routes: routes
})