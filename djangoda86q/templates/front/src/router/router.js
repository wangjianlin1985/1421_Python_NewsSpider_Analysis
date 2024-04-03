import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import xinwenzixunList from '../pages/xinwenzixun/list'
import xinwenzixunDetail from '../pages/xinwenzixun/detail'
import xinwenzixunAdd from '../pages/xinwenzixun/add'
import xinwenleixingList from '../pages/xinwenleixing/list'
import xinwenleixingDetail from '../pages/xinwenleixing/detail'
import xinwenleixingAdd from '../pages/xinwenleixing/add'
import wangyixinwenList from '../pages/wangyixinwen/list'
import wangyixinwenDetail from '../pages/wangyixinwen/detail'
import wangyixinwenAdd from '../pages/wangyixinwen/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'xinwenzixun',
					component: xinwenzixunList
				},
				{
					path: 'xinwenzixunDetail',
					component: xinwenzixunDetail
				},
				{
					path: 'xinwenzixunAdd',
					component: xinwenzixunAdd
				},
				{
					path: 'xinwenleixing',
					component: xinwenleixingList
				},
				{
					path: 'xinwenleixingDetail',
					component: xinwenleixingDetail
				},
				{
					path: 'xinwenleixingAdd',
					component: xinwenleixingAdd
				},
				{
					path: 'wangyixinwen',
					component: wangyixinwenList
				},
				{
					path: 'wangyixinwenDetail',
					component: wangyixinwenDetail
				},
				{
					path: 'wangyixinwenAdd',
					component: wangyixinwenAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
