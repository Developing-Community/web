import Register from './components/sharifmarket/Register.vue';
import GetLead from './components/sharifmarket/GetLead.vue';

export const routes = [
    {
        path: '/campaigns/sharifmarket/register',
        component: Register,
        name: 'register'
    },
    {
        path: '/campaigns/sharifmarket',
        component: GetLead,
        name: 'getLead'
    }
];