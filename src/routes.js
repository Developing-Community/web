import Register from './components/sharifmarket/Register.vue';
import SubmitTeam from './components/sharifmarket/SubmitTeam.vue';

export const routes = [
    {
        path: '/sharifmarket/register',
        component: Register,
        name: 'register'
    },
    {
        path: '/sharifmarket/team/submit',
        component: SubmitTeam,
        name: 'submit-team'
    },
];