<template><div class="ui container" style="text-align: center; margin-bottom: 20px;">
    <div class="top_container ">
        <div class="col-sm-10" style="display:block; margin: auto;">
<h1 style="text-align: center; margin:30px;">ورود</h1>
            <div v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div v-else>
                <div class="form-group">
                    <label>نام کاربری</label>
                    <input class="form-control" type="text" v-model="user.username">
                </div>
                <div class="form-group">
                    <label>کلمه عبور</label>
                    <input class="form-control" @keyup.enter="submit" type="password" v-model="user.password">
                </div>
                <button class="btn btn-primary" style="margin: 10px;" @click="submit">ورود</button>
                <button class="btn btn-primary" style="margin: 10px;" @click="$router.push({name: 'register'})">ثبت نام</button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import jwt_decode from 'jwt-decode';
    export default {
        data() {
            return {
                user: {
                    username: '',
                    password: ''
                },
                loading: false
            };
        },
        methods: {
            submit() {
                this.loading = true;
                var vinst = this;
                axios.post(this.$store.state.endpoints.obtainJWT, {username: this.user.username, password: this.user.password})
                    .then((response) => {
                        alert('با موفقیت وارد شدید');
                        this.$store.commit('updateToken', response.data.token);
                        this.$store.commit('setAuthentication', true);
                        if(this.$route.query.next){
                            this.$router.push(this.$route.query.next);
                        } else {
                            this.$router.push({ name: 'home' });
                        }
                        vinst.loading = false;
                    })
                    .catch((error) => {
                        alert('نام کاربری یا رمز عبور اشتباه است');
                        console.log(error);
                        this.$store.commit('removeToken');
                        vinst.loading = false;
                    });
                    
            }
        },
        beforeRouteEnter(to, from, next){
            console.log(to);
            const token = localStorage.getItem('t');
            if(token && ((Date.now()/1000) - jwt_decode(token).orig_iat < 604800)){
                next({ name: 'home' });
            }
            next();
        }
    }
</script>

<style scoped>
input {
    max-width: 500px;
    margin: auto;
}
</style>