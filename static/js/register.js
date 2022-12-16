function bindCaptchaBtnClick() {
    $("#captcha-btn").on("click", function (event) {
        var $this = $(this);
        var email = $("input[name='email']").val();
        if (!email) {
            alert("please input email first ");
            return;
        }
        $.ajax({
            url: "/user/captcha",
            method: "POST",
            data: {
                "email": email
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    $this.off("click");
                    var countDown = 60;
                    var timer = setInterval(function () {
                        countDown -= 1;
                        if (countDown > 0) {
                            $this.text(countDown + "秒后重新发送");
                        } else {
                            $this.text("获取验证码");
                            bindCaptchaBtnClick();
                            clearInterval(timer);
                        }
                    }, 1000);
                    alert("captcha send success...");
                } else {
                    alert(res['message']);
                }
            }
        })
    });
}

$(function () {
    // var csrftoken = $('meta[name=csrf-token]').attr('content')
    // $.ajaxSetup({
    //     beforeSend: function (xhr, settings) {
    //         if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
    //             xhr.setRequestHeader("X-CSRFToken", csrftoken)
    //         }
    //     }
    // })
    bindCaptchaBtnClick();
});

