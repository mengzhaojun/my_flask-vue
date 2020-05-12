import Vue from 'vue'
import VueRouter from 'vue-router'

const Login = () => import('../views/Login/Login')
const Layout = () => import('../views/Layout/Layout')
const Project = () => import('../views/Project/Project')
const Module = () => import('../views/Module/Module')
const Case = () => import('../views/Case/Case')
const Setting = () => import('../views/Setting/Setting')

Vue.use(VueRouter);

  const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      title: '登录页'
    }
  },
  {
    path: '/',
    component: Layout,
    name: Layout,
    meta: {
      title: '首页'
    },
    children: [
      {
        path: 'project',
        component: Project,
        name: 'Project'
      },
      {
        path: 'module',
        component: Module,
        name: 'Module'
      },
      {
        path: 'case',
        component: Case,
        name: 'Case'
      },
      {
        path: 'setting',
        component: Setting,
        name: 'Setting'
      },
    ]
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
