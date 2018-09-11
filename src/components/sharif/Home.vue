<template>
    <div class="row">
            <h1 style="margin:30px; text-align: center;">بازارچه کسب و کار شریف</h1>
            <div  v-if="loading" style="width: 100%; text-align: center;">
                <img style="margin: auto;" src="/static/loading.gif" />
            </div>
            <div style="text-align: center;" v-else>
                <hr/>
                <!-- <div style = "border: 2px solid #444444; border-radius: 5px; padding: 10px; margin: 10px;" v-for="product in products">
                    <p>نام محصول: {{ product.name }}</p>
                    <p>توضیحات: {{ product.description }}</p>
                    <p>نام قیمت: {{ product.price }}</p>
                    <p>غرفه: {{ product.seller.name }}</p>
                </div> -->

                
                <div class="row">
                    <div class="col-sm-6 col-md-4 col-lg-3" v-for="product in products">
                        <div class="panel panel-default">
                            <div class="panel-body quote">
                                                    <p>نام محصول: {{ product.name }}</p>
                                    <p>توضیحات: {{ product.description }}</p>
                                    <p>قیمت: {{ product.price }}</p>
                                    <p class="alert alert-info">غرفه {{ product.seller.name }}</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                products: [

                ],
                loading: false
            };
        },
        methods: {
            getProducts(){
                this.loading = true;
                var vinst = this;
                axios.get(this.$store.state.hostUrl + '/api/campaign/product/list/').then(response => {
                    console.log(response.data);
                    vinst.products = response.data;
                    vinst.loading = false;
                }).catch(err => {
                    vinst.loading = false;
                })
            },
        },
        created(){
            this.getProducts();
        }
    }
</script>

<style scoped>
h1, h4, label, button{
    font-family: tahoma;
}
.panel-body {
    font-family: 'tahoma', cursive;
    font-size: 16px;
    color: #6e6e6e;
}
</style>