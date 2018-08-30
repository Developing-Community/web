import Register from './components/sharifmarket/Register.vue';
import Login from './components/sharifmarket/Login.vue';
import Logout from './components/sharifmarket/Logout.vue';
import Home from './components/sharifmarket/Home.vue';
import SharifMarket from './components/sharifmarket/SharifMarket.vue';
import SubmitTeam from './components/sharifmarket/SubmitTeam.vue';
import Dashboard from './components/sharifmarket/Dashboard.vue';

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
            },
            {
                path: 'register',
                component: Register,
                name: 'sharif-register'
            },
            {
                path: 'team/submit',
                component: SubmitTeam,
                name: 'sharif-submit-team'
            },
            {
                path: 'login',
                component: Login,
                name: 'sharif-login'
            },
            {
                path: 'logout',
                component: Logout,
                name: 'sharif-logout'
            },
        ]
    },
    {
        path: '*',
        redirect: {name: 'sharif-home'}
    }
];