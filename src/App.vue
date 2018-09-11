<template>
    <div>
        <app-header></app-header>
        <router-view></router-view>
        <app-footer></app-footer>
    </div>
</template>

<script>
    import Header from "./components/Header.vue"
    import Footer from "./components/Footer.vue"
    export default {
        components:
        {
            appHeader: Header,
            appFooter: Footer
        }
    }
</script>

<style>
@font-face {
    font-family: IRANSans;
    src: url(/static/fonts/IranSansWeb.ttf) format("ttf");
}


a {
    color: #2900a8;
}

.navbar-nav mr-0 a {
    color:white;
}

a, p, li, .font {
    text-align: right;
    font-family: IRANSans;
}

.carousel-item p {
    margin: 20px;
    line-height: 10px;
}

#nav {
    z-index: 50;
    margin: 0;
    padding: 0;
    height: 70px;
    direction: rtl;
    background-color: #223052;
    position: fixed;
    top: 0;
    transition: all 0.4s;
}

.img {
    width: 80px;
    height: 70px;
    padding: 15px 0 15px 5px;
    margin-bottom: 20px;
    position: fixed;
    left: 0;
    top: 0;
}

#nav-brand {
    position: fixed;
    left: 80px;
}

#header{
    background-color: white;
    direction: rtl;
    display: inline-block;
}

p.blue {
    background-color: #223052;
    font-size: 30px;
    border-radius: 0 0 200px 200px;
    padding-left: 80px;
    transition: 0.2s;
    z-index: 3;
}

p.blue:hover{
    transform: scale(1.1);
}

#footer {
    background-color: #08203c;
    position: relative;
    top: 70px;
    bottom: 0;
    height: 150px;
}

#footer div {
    padding-top: 30px;
}

#footer div ul {
    position: relative;
    margin-left: 42%;

}

#footer div ul li {
    list-style-type: none;
    display: inline-block;
    margin-left: 10px;
    transition: all 0.4s;
}

#footer div ul li:hover {
    transform: scale(1.1);
}

@media screen and (max-width: 992px){
    #god{
        display: none;
    }
    #main-header{
        display: none;
    }

}

@media screen and (max-width: 768px) {

    #nav-ul {
        margin-top: 30px;
    }

}

@media screen and (max-width: 440px) {
    #footer div ul {
     margin-left: 20%;
    }

}

@media screen and (max-width: 368px) {
    #footer div ul {
        margin-left: 10px;
    }
    #nav-brand{
        display: none;
    }
}

body .navbar .nav-item .btn {
    color: white !important;
}

/* social icons */

.social:hover {
     -webkit-transform: scale(1.1);
     -moz-transform: scale(1.1);
     -o-transform: scale(1.1);
 }
 .social {
     -webkit-transform: scale(0.8);
     /* Browser Variations: */

     -moz-transform: scale(0.8);
     -o-transform: scale(0.8);
     -webkit-transition-duration: 0.5s;
     -moz-transition-duration: 0.5s;
     -o-transition-duration: 0.5s;

 }

#footer .text-center .social{
     color: white;
}

/*
    Multicoloured Hover Variations
*/

 #footer .text-center #social-tw:hover {
     color: #4099FF;
 }
 #footer .text-center #social-gh:hover {
     color: #d34836;
 }
 #footer .text-center #social-em:hover {
     color: #f39c12;
 }
 #footer .text-center #social-in:hover {
     color: #f39c12;
 }
 #footer .text-center #social-tg:hover {
     color: #4099FF;
 }
 #footer .text-center #social-sl:hover {
     color: #44CC4D;
 }



 /* for child themes */
div.container {
    min-height: 450px;
}

.bot_container{


    margin-top: 20px;
    margin-bottom: 20px;
}


.logo{
    margin: 70px auto 20px auto;
    height: 200px;
    width: 200px;
}

.content{
    text-align:right;
}
.content h1{
    padding: 10px;
    font-size: 27px;
    font-weight: bold;
}

.content p, .content li{
    font-size:17px;
    line-height: 30px;
}

@media screen and (min-width: 768px) {
    #top_logo {
        display: block;
    }
    .content{
        padding: 0px 100px;
    }
}

@media screen and (max-width: 768px) {
    #top_logo {
        display: none;
    }
    #base_container {
        margin-top:100px;
    }
    .content{
        padding: 0px 30px;
    }
}

#about #join-us p, #about #join-us {
    text-align: center;
}
</style>
