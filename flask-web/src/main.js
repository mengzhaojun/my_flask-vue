import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/css/main.scss'

// 解决3.0.x版本菜单连续点击出现错误问题
// const originalPush = Router.prototype.push
// Router.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch(err => err)
// }


Vue.config.productionTip = false
Vue.use(ElementUI)

new Vue({
  el: '#app',
  store,
  router, // 挂载路由到实例中 
  render: h => h(App)
})