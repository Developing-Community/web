import Register from './components/sharifmarket/Register.vue';
import SubmitTeam from './components/sharifmarket/SubmitTeam.vue';
import SubmitProduct from './components/sharifmarket/SubmitProduct.vue';

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
    {
        path: '/sharifmarket/product/submit',
        component: SubmitProduct,
        name: 'submit-product'
    },
];