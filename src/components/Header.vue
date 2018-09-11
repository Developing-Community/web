<template>
    <div>
<nav class="navbar navbar-expand-md col-12" id="nav">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <img src="/static/img/menu.png">
    </button>

    <div class="collapse navbar-collapse mt-2" id="navbarSupportedContent">
        <ul class="navbar-nav mr-0" style="background-color: #223052;" id="nav-ul">
            <li class="nav-item active">
                <router-link :to="{name: 'home'}" tag="a" class="btn font"><a>خانه</a></router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{name: 'groups'}" tag="a" class="btn font"><a>لینک گروه ها</a></router-link>
            </li>
            <li class="nav-item dropdown">
                <a class="btn font dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    پروفایل
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">

                    <div v-if="isAuthenticated">
                    <router-link :to="{name: 'logout'}" tag="a" class="dropdown-item font"><a>خروج</a></router-link>
                    </div>
                    <div v-else>
                    <router-link :to="{name: 'register'}" tag="a" class="dropdown-item font"><a>ثبت نام</a></router-link>
                    <router-link :to="{name: 'login'}" tag="a" class="dropdown-item font"><a>ورود</a></router-link>
                    </div>

                </div>
            </li>
        </ul>
        <!-- TODO: Add search -->
        <!--<form class="form-inline my-2 my-lg-0" dir="ltr">-->
            <!--<input class="form-control mr-sm-2 font " type="search" placeholder="جست و جو" aria-label="Search">-->
            <!--<button class="btn btn-outline-success my-2 my-sm-0 font mr-1" type="submit">جست و جو</button>-->
        <!--</form>-->
    </div>
    <a class="nav-link text-white font-weight-bold" id="nav-brand">Developing Community</a>
    <img src="/static/img/logo-header-small.png" class="img">



</nav>

<!--<div class="container col-12" style="padding-top: 70px; background-color: #1c1c39;height: 500px" id="main-header">-->
    <!--<div class="col-3" style="display: inline-block;position: relative;bottom: 120px;right: -40px">-->
        <!--<img src="{% static 'img/quest.png' %}" style="width: 300px;">-->
    <!--</div>-->
    <!--<div id="carouselExampleIndicators" class="carousel slide col-8" data-ride="carousel" style="background-color: #1c1c39;display: inline-block">-->
        <!--<div class="carousel-inner" >-->
            <!--<div class="carousel-item active">-->
                <!--<div class="jumbotron jumbotron-fluid" style="height: 350px;background-color: #1c1c39;">-->
                    <!--<div class="container" style="direction: rtl">-->
                        <!--&lt;!&ndash;-->
                        <!--<p class="lead text-white">-->
                            <!--پلتفرمی برای یادگیری، آموزش و فعالیت در کنار انسان های مختلف از حوزه های مختلف-->
                        <!--</p>-->
                        <!--&ndash;&gt;-->
                        <!--<p class="font font-weight-bold text-white" style="font-size: 50px;margin:40px;">هدف گروه</p>-->
                        <!--<p class="lead text-white" style="margin:40px; margin-bottom:10px;">بعد از وارد شدن به گروه حوزه هایی رو برای یادگیری خودتون انتخاب می کنید و هر هفته از فعالیتی که برای یادگیری اون حوزه انجام دادید به بقیه اعضای تیم گزارش می دید. گزارش جزئیات خاصی نیاز نداره و میتونه در حد ۴-۵ جمله باشه. مثلا این که یه آموزش آنلاین درباره اون حوزه شروع کردید یا یک کتاب دربارش خوندید. البته گزارش دقیق تر برای انتقال تجربه یادگیریتون به دیگران بهتر هست-->

                        <!--</p>-->
                        <!--{% block about_link %}-->
                        <!--<a href = "{{ request.build_absolute_uri }}#about">اطلاعات بیشتر</a>-->
                        <!--{% endblock about_link %}-->
                    <!--</div>-->
                <!--</div>-->
            <!--</div>-->
            <!--<div class="carousel-item">-->
                <!--<div class="jumbotron jumbotron-fluid" style="height: 350px;background-color: #1c1c39;">-->
                    <!--<div class="container">-->
                        <!--<p class="font font-weight-bold text-white" style="font-size: 50px;">گام دوم</p>-->
                        <!--<p class="lead text-white">هدف گروه ما این هست که تو یه محیط ساختار یافته یاد بگیرید و نهایتا تو این کامیونیتی تو فعالیت ها و تیم های مختلف شرکت کنید و با آدمای مختلف در حوزه های مختلف آشنا بشید و اگر سوال یا راهنمایی هم خواستید ازشون کمک بگیرید. منظور از فعالیت، هروقتی برای انجام فعالیت های تیمی واقعی آماده شدید، اگر توی کاری به هم تیمی هایی از حوزه خودتون یا حوزه های دیگه نیاز داشتید از طریق این گروه سابقه گزارش ها و فعالیتشون رو ببینید و با شناخت نسبی که پیدا کردید بهشون پیشنهاد بدید و نهایتا در قالب تیم با هم کار کنید. سعی کنید گزارش های جذاب بنویسید و فعالیت کنید تا دیگران هم شما رو به عنوان هم تیمی انتخاب کنند-->
                        <!--</p>-->
                    <!--</div>-->
                <!--</div>-->
            <!--</div>-->
            <!--<div class="carousel-item">-->
                <!--<div class="jumbotron jumbotron-fluid" style="height: 350px;background-color: #1c1c39;">-->
                    <!--<div class="container">-->
                        <!--<p class="font font-weight-bold text-white" style="font-size: 50px;">گام اول</p>-->
                        <!--<p class="lead text-white">هدف گروه ما این هست که تو یه محیط ساختار یافته یاد بگیرید و نهایتا تو این کامیونیتی تو فعالیت ها و تیم های مختلف شرکت کنید و با آدمای مختلف در حوزه های مختلف آشنا بشید و اگر سوال یا راهنمایی هم خواستید ازشون کمک بگیرید. منظور از فعالیت، هر فعالیتی تو هر حوزه ای هست. از یه تحقیق گروهی در علوم انسانی و پایه گرفته تا یک پروژه ی فیلم سازی یا برنامه نویسی-->
                        <!--</p>-->
                    <!--</div>-->
                <!--</div>-->
            <!--</div>-->
        <!--</div>-->
        <!--<a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">-->
            <!--<span class="carousel-control-prev-icon" aria-hidden="true"></span>-->
            <!--<span class="sr-only">Previous</span>-->
        <!--</a>-->
        <!--<a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">-->
            <!--<span class="carousel-control-next-icon" aria-hidden="true"></span>-->
            <!--<span class="sr-only">Next</span>-->
        <!--</a>-->
        <!--</div>-->
    <!--</div>-->
<!--</div>-->
<img class="ui centered small image logo" id="top_logo" src="/static/img/logo4.jpg" alt="Logo">
    </div>
</template>

<script>
    export default {
        computed:{
            isAuthenticated(){
                return this.$store.getters.isAuthenticated;
            }
        }
    }
</script>

<style>
</style>