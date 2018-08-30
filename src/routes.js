import Register from './components/sharifmarket/Register.vue';
import Login from './components/sharifmarket/Login.vue';
import Home from './components/sharifmarket/Home.vue';
import SharifMarket from './components/sharifmarket/SharifMarket.vue';
import SubmitTeam from './components/sharifmarket/dashboard/SubmitTeam.vue';
import SubmitProduct from './components/sharifmarket/dashboard/SubmitProduct.vue';
import Dashboard from './components/sharifmarket/dashboard/Dashboard.vue';

export const routes = [
    {
        path: '/sharifmarket',
        component: SharifMarket,
        name: 'sharifmarket',
        children: [
            {
                path: '',
                component: Home,
                name: 'sharif-home'
            },
            {
                path: 'dashboard',
                component: Dashboard,
                name: 'sharif-dashboard',
                children: [
                    {
                        path: 'team/submit',
                        component: SubmitTeam,
                        name: 'sharif-submit-team'
                    },
                    {
                        path: 'product/submit',
                        component: SubmitProduct,
                        name: 'sharif-submit-product'
                    }
                ]
            },
            {
                path: 'register',
                component: Register,
                name: 'sharif-register'
            },
            {
                path: 'login',
                component: Login,
                name: 'sharif-login'
            },
        ]
    }
];