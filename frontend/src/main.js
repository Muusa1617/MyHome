// import Vue,{createApp} from 'vue'
// // import Vue,{createApp} from 'vue'

// import App from './App.vue'
// import router from './router'
// import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
// // import "./assets/main.css";
// // Import Bootstrap and BootstrapVue CSS files (order is important)
// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";

// // Make BootstrapVue available throughout your project
// Vue.use(BootstrapVue);
// Vue.use(IconsPlugin);

// URLSearchParams.prototype.appendIfExists = function (key, value) {
//     if (value !== null && value !== undefined) {
//         this.append(key, value)
//     }
// };

// createApp(App).use(router).mount('#app');


import {createApp} from 'vue'
// import Vue,{createApp} from 'vue'

import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
// import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
// import "./assets/main.css";
// Import Bootstrap and BootstrapVue CSS files (order is important)
// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";

// Make BootstrapVue available throughout your project
// Vue.use(BootstrapVue);
// Vue.use(IconsPlugin);

URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};

createApp(App).use(router).mount('#app');