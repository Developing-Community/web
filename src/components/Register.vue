<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1 style="text-align: center; margin:30px;">ثبت نام</h1>
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
                    <input class="form-control" type="text" v-model="user.password">
                </div>
                <div class="form-group">
                    <label>نام</label>
                    <input class="form-control" type="text" v-model="user.first_name">
                </div>
                <div class="form-group">
                    <label>نام خانوادگی</label>
                    <input class="form-control" type="text" v-model="user.last_name">
                </div>
                <button class="btn btn-primary" @click="submit">ثبت نام</button>
            </div>
        </div>
    </div>
</template>

<script>
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
                resource: {},
            };
        },
        methods: {
            submit() {
                this.resource.save({}, this.user)
                        .then(response => {
                            console.log("good");
                            console.log(response);
                            if(response.statusText == "Created"){
                                alert("ثبت نام با موفقیت انجام شد");
                            }
                        })
                        .catch(err => {
                            return err.json();
                        })
                        .then(err => {
                            console.log("bad");
                            console.log(err);
                            if(err.username){
                                alert("Username: " + err.username[0]);
                            }
                        });
            }
        },
        created() {
            const customActions = {
                saveAlt: {method: 'POST', url: 'alternative.json'}
            };
            this.resource = this.$resource('user/register/', {}, customActions);
        }
    }
</script>

<style>
</style>