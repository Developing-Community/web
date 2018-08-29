<template>
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
            <h1 style="text-align: center; margin:30px;">ثبت گروه</h1>
            <div class="form-group">
                <label>نام گروه</label>
                <input class="form-control" type="text" v-model="group.name">
            </div>
            <button class="btn btn-primary" @click="submit">ثبت نام</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                group: {
                    name: ''
                },
            };
        },
        methods: {
            submit() {
                var host =  window.location.href.split("/")[0] + "//" +  window.location.href.split("/")[2]
                axios.post(host + '/api/team/create/', 
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
                        })
                        .catch(err => {
                            console.log("bad");
                            console.log(err.response);
                            if(err.response.data.name){
                                alert("Group name: " + err.response.data.name[0]);
                            }
                        });
            }
        }
    }
</script>

<style>
</style>