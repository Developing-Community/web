<template>
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
            <h1 style="text-align: center; margin:30px;">ثبت نام</h1>
            <div  v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div v-else>
                <div class="form-group">
                    <label>نام کاربری</label>
                    <input class="form-control" type="text" v-model="user.username">
                </div>  
                <div class="form-group">
                    <label>ایمیل</label>
                    <input class="form-control" type="text" v-model="user.email">
                </div>
                <div class="form-group">
                    <label>کلمه عبور</label>
                    <input class="form-control" type="password" v-model="user.password">
                </div>
                <div class="form-group">
                    <label>نام</label>
                    <input class="form-control" type="text" v-model="user.first_name">
                </div>
                <div class="form-group">
                    <label>نام خانوادگی</label>
                    <input class="form-control" @keyup.enter="submit" type="text" v-model="user.last_name">
                </div>
                <button class="btn btn-primary" @click="submit">ثبت نام</button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                user: {
                    username: '',
                    email: '',
                    password: '',
                    first_name: '',
                    last_name: ''
                },
                loading: false
            };
        },
        methods: {
            submit() {
                this.loading = true;
                var vinst = this;
                var host =  window.location.href.split("/")[0] + "//" +  window.location.href.split("/")[2]
                axios.post(host + '/api/user/register/', 
                this.user, // the data to post
                { headers: {
                'Content-type': 'application/json',
                }
                }).then(response => {
                            console.log("good");
                            console.log(response.data);
                            if(response.statusText == "Created"){
                                alert("ثبت نام با موفقیت انجام شد");
                            }
                            vinst.$store.dispatch('obtainToken', {username: this.user.username, password: this.user.password})
                            .then( () => {
                                vinst.loading = false;
                                this.$router.push({ name: 'sharif-submit-team' });
                            });
                        })
                        .catch(err => {
                            console.log("bad");
                            console.log(err.response);
                            if(err.response.data.username){
                                alert("Username: " + err.response.data.username[0]);
                            }
                            if(err.response.data.password){
                                alert("Password: " + err.response.data.password[0]);
                            }
                            if(err.response.data.email){
                                alert("Email: " + err.response.data.email[0]);
                            }
                            if(err.response.data.first_name){
                                alert("First name: " + err.response.data.first_name[0]);
                            }
                            if(err.response.data.last_name){
                                alert("Last name: " + err.response.data.last_name[0]);
                            }
                            vinst.loading = false;
                        });
            }
        }
    }
</script>

<style>
</style>