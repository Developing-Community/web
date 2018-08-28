<template>


	<div class="wrapper row-form" style="margin: 20px">
		<div class="ml-content-table">

					<div class="mt30 mb30" style="background-color: 111111; padding: 20px; margin: 0px; border-radius: 20px;">
						<div class="container-fluid hero">
							<div class="container">

<div class="row pb60">
	<div class="col-xs-12 col-md-8 col-md-offset-2 align-center" >
		<img class="img-responsive display-inline" style="margin: auto" src="https://bucket.mlcdn.com/a/1252/1252702/images/f139f7841342247a4dc54dbf979ffd1fafd4a476.png" alt="" width="150" style="display: block;" border="0">
	</div>
</div>

<div class="row">
	<div class="col-xs-12 col-md-8 col-md-offset-2">
		<h4 style="text-align: center">بازارچه کسب و کار دانشگاه شریف</h4>
	</div>
</div>

<div class="row" style="margin: 0px;">
	<div class="col-xs-12 col-md-8 col-md-offset-2">
		<p style="text-align: center">برای ثبت نام در بازارچه فرم زیر را پر کنید</p>
	</div>
</div>

<div class="row" style="text-align: center">
	<div class="col-xs-12 col-md-8 col-md-offset-2 ml-subscribe-form" id="mlb2-1019552">


            {% if messages %}
                <div class='messages'>

                <ul class="messages">
                {% for message in messages %}
                <li class="html_safe success alert alert-info">{{ message }}</li>
                {% endfor %}
                </ul>

                </div>
            {% endif %}

        <form method='POST' action='' enctype='multipart/form-data' class="djform">{% csrf_token %}
        {% form form=form %}{% endform %}
            <input type='submit' class="btn-primary" style="margin: 10px 5px; padding: 0px 40px; font-size: 20px;" value='تایید'/>
        </form>
		<style>
			input, select, textarea{
    color: #abcdef;
}

textarea:focus, input:focus {
    color: #abcdef;
}
		</style>
	</div>
</div>



							</div>
						</div>
					</div>

					<div class="container-fluid ml-11">
						<div class="container">
























<div class="row">
	<div class="col-sm-10 col-sm-offset-1">
		<div class="row countdown" id="timer-11" data-date="2018-08-31 16:00:00">
			<div class="col-sm-3 col-sm-3 col-xs-12 col-xs-pad">
				<div class="clock">
					<span class="days">4</span>
					<div class="smalltext">روز</div>
				</div>
			</div>
			<div class="col-sm-3 col-sm-3 col-xs-12 col-xs-pad">
				<div class="clock">
				<span class="hours">15</span>
				<div class="smalltext">ساعت</div>
				</div>
			</div>
			<div class="col-sm-3 col-sm-3 col-xs-12 col-xs-pad">
				<div class="clock">
				<span class="minutes">27</span>
				<div class="smalltext">دقیقه</div>
				</div>
			</div>
			<div class="col-sm-3 col-sm-3 col-xs-12">
				<div class="clock">
				<span class="seconds">42</span>
				<div class="smalltext">ثانیه</div>
				</div>
			</div>
		</div>
	</div>
</div>



						</div>
					</div>
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
</template>

<script>

    function timers() {
		setTimeout(function(){
			$('.countdown').each(function() {
			    if (! $(this).data('countdown-bound')) {
                    var id = $(this).attr('id');
                    var date = $(this).attr('data-date');

                    $(this).data('countdown-bound', true);
                    initializeClock(id, date);
                }
			});
		});
	}

	$(document).ready(function () {
		timers();

        $('body').on('DOMNodeInserted',function(e) {
            timers();
        });
	});

	function getTimeRemaining(endtime) {
        endtime = endtime.replace(' ', 'T');

        var t = Date.parse(endtime) - Date.parse(new Date());
		var seconds = Math.floor((t / 1000) % 60);
		var minutes = Math.floor((t / 1000 / 60) % 60);
		var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
		var days = Math.floor(t / (1000 * 60 * 60 * 24));
		return {
			'total': t,
			'days': days,
			'hours': hours,
			'minutes': minutes,
			'seconds': seconds
		};
	}

	function initializeClock (id, endtime) {
		var clock = document.getElementById(id);
		var daysSpan = clock.querySelector('.days');
		var hoursSpan = clock.querySelector('.hours');
		var minutesSpan = clock.querySelector('.minutes');
		var secondsSpan = clock.querySelector('.seconds');

		function updateClock() {
			var t = getTimeRemaining(endtime);

			daysSpan.innerHTML = t.days;
			hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
			minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
			secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

			if (t.total <= 0) {
				daysSpan.innerHTML = '00';
				hoursSpan.innerHTML = '00';
				minutesSpan.innerHTML = '00';
				secondsSpan.innerHTML = '00';
			}
		}

		updateClock();

		if (window['timerinterval' + id]) {
			clearInterval(window['timerinterval' + id]);
		}

		window['timerinterval' + id] = setInterval(updateClock, 1000);
	}

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
            this.resource = this.$resource('user/register/', {}, customActions);
        }
    }
</script>

<style type="text/css">
.ml-11 .countdown {
	color: #ffffff;
	text-align: center;
	font-size: 36px;
}
.ml-11 .countdown .clock {
	padding: 10px;
	border-radius: 7px;
	background: #111111;
	display: inline-block;
}
.ml-11 .countdown .clock > span {
	padding: 15px;
	border-radius: 3px;
	background: #222222;
	display: inline-block;
	margin-bottom: 10px;
	min-width: 100px;
}
.ml-11 {
	padding-bottom: 30px;
	padding-top: 30px;
}
.ml-11 .countdown .smalltext {
	font-size: 14px;
}
.ml-11 h1 {
	color: #ffffff;
	font-size: 36px;
	font-weight: normal; font-style: normal; text-decoration: none;
	text-align: center;
	margin-bottom: 30px;
}
@media (max-width: 768px) {
	.clock,
	.clock > span {
		width: 100% !important;
	}
	.col-xs-pad .clock {
		width: 100% !important;
		margin-bottom: 15px;
	}
}
.clock{
    min-width: 120px;
}
</style>