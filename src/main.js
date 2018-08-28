import Vue from 'vue'
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import App from './App.vue'

Vue.use(VueResource);
Vue.use(VueRouter);

var url = window.location.href
var arr = url.split("/");
var host = arr[0] + "//" + arr[2]

Vue.http.options.root = host + "/api/";
Vue.http.headers.post['Content-Type'] = 'application/json'


new Vue({
  el: '#app',
  render: h => h(App)
})
