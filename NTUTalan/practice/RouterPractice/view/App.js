export default {
    data() {
        return {
        }
    },
    template: `
    <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/">Contact</router-link></li>
        <li><a>About</a></li>
    </ul>
    <div id="userView">
        <router-view></router-view>
    </div>`
}