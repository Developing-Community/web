import Register from './components/account/Register.vue';
import Login from './components/account/Login.vue';
import Logout from './components/account/Logout.vue';
import Account from './components/account/Account.vue';
import Home from './components/Home.vue';
import TelegramGroups from './components/TelegramGroups.vue';

export const routes = [
    {
        path: '',
        component: Home,
        name: 'home'
    },
    {
        path: '/account',
        component: Account,
        name: 'account',
        children: [
            {
                path: 'login',
                component: Login,
                name: 'login'
            },
            {
                path: 'register',
                component: Register,
                name: 'register'
            },
            {
                path: 'logout',
                component: Logout,
                name: 'logout'
            },
        ]
    },
    {
        path: '/groups',
        component: TelegramGroups,
        name: 'groups'
    },
    {
        path: '*',
        redirect: {name: 'home'}
    }
];
