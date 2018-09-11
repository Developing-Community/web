<template>
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
            <h1 style="text-align: center; margin:30px;">انتخاب گروه</h1>
            <div  v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div style="text-align: center;" v-else>
                
                <button class="btn btn-primary" style = "margin: 5px;" v-for="gp in groups" @click="enroll(gp)">
                    {{gp.name}}
                </button>
                <br/>
                <hr/>
                <div class="form-group">
                    <label>افزودن گروه جدید</label>
                    <input class="form-control" @keyup.enter="submit" type="text" v-model="group.name">
                </div>
                <button class="btn btn-primary" @click="submit">تایید</button>

                
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { protectedUrlMixin } from '../../protectedUrlMixin';
    export default {
        data() {
            return {
                group: {
                    name: ''
                },
                groups: [],
                loading: true
            };
        },
        mixins: [
            protectedUrlMixin
        ],
        methods: {
            enroll(gp) {
                this.loading = true;
                var vinst = this;
                axios.post(this.$store.state.hostUrl + '/api/team/enroll/', 
                {
                    'group': gp.id,
                }, // the data to post
                { headers: {
                'Content-type': 'application/json',
                'Authorization' : 'JWT ' + localStorage.getItem('t')
                }
                }).then(response => {
                    console.log("good");
                    console.log(response.data);
                    if(response.statusText == "Created"){
                        alert("ثبت تیم با موفقیت انجام شد");
                    }
                    vinst.loading = false;
                    this.$router.push({ name: 'sharif-dashboard' });
                })
                .catch(err => {
                    console.log("bad");
                    console.log(err.response);
                    vinst.loading = false;
                });
            },
            submit() {
                this.loading = true;
                var vinst = this;
                axios.post(this.$store.state.hostUrl + '/api/team/create/', 
                this.group, // the data to post
                { headers: {
                'Content-type': 'application/json',
                'Authorization' : 'JWT ' + localStorage.getItem('t')
                }
                }).then(response => {
                    console.log("good");
                    console.log(response.data);
                    if(response.statusText == "Created"){
                        alert("ثبت تیم با موفقیت انجام شد");
                    }
                    vinst.loading = false;
                    this.$router.push({ name: 'sharif-dashboard' });
                })
                .catch(err => {
                    console.log("bad");
                    console.log(err.response);
                    if(err.response.data.name){
                        alert("Group name: " + err.response.data.name[0]);
                    }
                    vinst.loading = false;
                });
            }
        },
        created(){
            var vinst = this;
            axios.get(this.$store.state.hostUrl + '/api/team/list/').then(response => {
                    this.groups = response.data;
                    vinst.loading = false;
                })
        }
    }
</script>

<style scoped>
h1, h4, label, button{
    font-family: tahoma;
}
</style>