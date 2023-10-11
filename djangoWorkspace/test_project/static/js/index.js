window.onload = function() {
    let btn = document.getElementById('btn');

    // 버튼 클릭 시 show_msg() 함수 호출
    btn.addEventListener('click', show_msg);
};

function show_msg(){
    alert('메시지 출력')
}