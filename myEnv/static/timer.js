function timer(time) {
    var hour = 0;
    var min = 0;
    var sec = 0;

    var x = setInterval(function () {
        min = parseInt(time / 60);
        sec = time % 60;

        document.getElementById("timer").innerHTML =
            hour + "시 " + min + "분 " + sec + "초";
        time--; // 1초 줄이기

        if (time < 0) { // 0초가 되면 사용종료와 동시에 LED off
            clearInterval(x);
            publish('led1', 0);
            publish('led2', 2);
            publish('led3', 4);
            document.getElementById("timer").innerHTML = "사용이 종료 되었습니다.";
        }
    }, 1000); // 1초에 한번씩 timer 함수 호출
}
