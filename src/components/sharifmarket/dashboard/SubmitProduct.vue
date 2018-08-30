<template>
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
            <h1 style="text-align: center; margin:30px;">ثبت محصولات</h1>
            <div  v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div v-else>
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
                    <input class="form-control" type="number" v-model="product.price">
                </div>
                <button class="btn btn-primary" @click="submit">تایید</button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { protectedUrlMixin } from '../../../protectedUrlMixin';

    export default {
        data() {
            return {
                product: {
                    name: '',
                    description: '',
                    price: ''
                },
                loading: false
            };
        },
        mixins: [
            protectedUrlMixin
        ],
        methods: {
            submit() {
                this.loading = true;
                var vinst = this;
                var host =  window.location.href.split("/")[0] + "//" +  window.location.href.split("/")[2]
                axios.post(host + '/api/campaign/product/create/', 
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
                            vinst.loading = false;
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
            }
        }
    }
</script>

<style scoped>
h1, h4, label, button{
    font-family: tahoma;
}
</style>