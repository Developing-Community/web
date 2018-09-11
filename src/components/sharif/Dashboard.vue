<template>
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3" style="text-align: center;">
            <h1 style="margin:30px;">داشبورد</h1>
            <h3>تیم {{ group.name }}</h3>
            <button class="btn btn-primary" style="margin: 10px;" @click="$router.push({name: 'sharif-submit-team'})">تغییر تیم</button>
            <div  v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div style="text-align: center;" v-else>
                <hr/>
                
                <div style="border: 2px solid #444444; border-radius: 5px; padding: 10px; margin: 20px;">
                    <h4 style="text-align: center;">محصولات شما</h4>
                    <div style = "border: 2px solid #444444; border-radius: 5px; padding: 10px; margin: 10px;" v-for="product in products">
                        <p>نام محصول: {{ product.name }}</p>
                        <p>توضیحات: {{ product.description }}</p>
                        <p>قیمت: {{ product.price }}</p>
                    </div>
                </div>
                
                <div style="border: 2px solid #444444; border-radius: 5px; padding: 10px; margin: 20px;">
                    <h4 style="text-align: center;">افزودن محصول</h4>
                    <div class="form-group">
                        <label>نام محصول</label>
                        <input class="form-control" type="text" v-model="product.name">
                    </div>
                    <div class="form-group">
                        <label>توضیحات</label>
                        <textarea rows="5" class="form-control" v-model="product.description"></textarea>
                    </div>
                    <div class="form-group">
                        <label>قیمت</label>
                        <input class="form-control" @keyup.enter="submit" type="number" v-model="product.price">
                    </div>
                    <button class="btn btn-primary" @click="submit">تایید</button>
                </div>

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
                product: {
                    name: '',
                    description: '',
                    price: ''
                },
                group: {
                    id: 0,
                    name: ''
                },
                products: [

                ],
                loading: true
            };
        },
        mixins: [
            protectedUrlMixin
        ],
        methods: {
            getProducts(){
                this.loading = true;
                var vinst = this;
                axios.get(this.$store.state.hostUrl + '/api/campaign/product/list/?group=' + vinst.group.id).then(response => {
                    this.products = response.data;
                    vinst.loading = false;
                }).catch(err => {
                    console.log(err);
                    vinst.loading = false;
                })
            },
            submit() {
                this.loading = true;
                var vinst = this;
                axios.post(this.$store.state.hostUrl + '/api/campaign/product/create/', 
                this.product, // the data to post
                { headers: {
                'Content-type': 'application/json',
                'Authorization' : 'JWT ' + localStorage.getItem('t')
                }
                }).then(response => {
                    console.log("good");
                    console.log(response.data);
                    if(response.statusText == "Created"){
                        alert("ثبت محصول با موفقیت انجام شد");
                    }
                    vinst.product.name = '';
                    vinst.product.description = '';
                    vinst.product.price = 0;
                    this.getProducts();
                })
                .catch(err => {
                    console.log("bad");
                    console.log(err.response);
                    if(err.response.data.name){
                        alert("Product name: " + err.response.data.name[0]);
                    }
                    if(err.response.data.description){
                        alert("description: " + err.response.data.description[0]);
                    }
                    if(err.response.data.price){
                        alert("price: " + err.response.data.price[0]);
                    }
                    vinst.loading = false;
                });
            },
        },
        created(){
            var vinst = this;
            axios.get(this.$store.state.hostUrl + '/api/team/getuserteam/',
                {
                    headers: {
                        'Authorization' : 'JWT ' + localStorage.getItem('t')
                        }
                })
            .then(response => {
                console.log("good");
                if(response.data.length != 1) {
                    vinst.loading = false;
                    vinst.$router.push({ name: 'sharif-submit-team' });
                } else {
                    vinst.group = response.data[0];
                    this.getProducts();
                }
            })
        }
    }
</script>

<style scoped>
h1, h4, label, button{
    font-family: tahoma;
}
</style>