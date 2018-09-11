import jwt_decode from 'jwt-decode';
import { store } from './main';
export const protectedUrlMixin = {
    beforeRouteEnter(to, from, next){
        console.log(to);
        const token = localStorage.getItem('t');
        const loginRoute = { name: 'login' }
        if(!token){
            next(loginRoute);
        }
        else{
            const decoded = jwt_decode(token);
            const exp = decoded.exp
            const orig_iat = decoded.orig_iat
            if(exp - (Date.now()/1000) >= 3600){
                if((Date.now()/1000) - orig_iat < 604800){
                    store.dispatch('refreshToken')
                } else {
                    next(loginRoute);
                }
            }
        }
        next();
    }
}