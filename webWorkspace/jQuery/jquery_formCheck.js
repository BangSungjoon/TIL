// 회원가입 폼 유효성 확인

$(document).ready(function() {
    // 시작 시 id 입력란에 포커스
    $('#id').focus();


    // 키보드 이벤트
    // 휴대폰 번호 첫 번째 입련란에 입력값이 3개가 되면 다음으로 포커스 이동
    $('#hp1').on('keyup', function(){
        if($(this).val().length == 3) {
            $('#hp2').focus();
        }
    });

    $('#hp2').on('keyup', function(){
        if($(this).val().length == 4) {
            $('#hp3').focus();
        }
    });

    // 엔터키 눌렀을 때 무조건 submit 되지 않도록
    // 문서 전체에 이벤트 처리
    // [Enter] 아스키 코드값 : 13
    $(document).on('keydown', function(e) {
        if(e.keyCode == 13) return false;
    });


    // 엔터키 눌렀을 때 포커스 이동
    $('#id').on('keydown', function(e) {
        // id를 입력하고 엔터키 눌렀을 때
        if($('#id').val() != "" && e.keyCode == 13) {
            $('#pwd').focus();
        }
    });

    // newMemberForm의 submit(전송)[완료] 버튼 눌렀을 때
    $('#newMemberForm').on('submit', function(){
        // id를 입력하지 않은 경우
        if($('#id').val() == "") {
            alert("아이디를 입력하세요");
            $('#id').focus();
            return false; // 서버로 전송되지 않도록 전송 기능 막음
        }

        // 비밀번호 입력하지 않은 경우

        // 라디오 버튼 선택하지 않은 경우
        if(!$('input[type="radio"]').is(':checked')) {
            alert("학년을 선택하세요");
            return false;
        }

        if(!$('input[type="checkbox"]').is(':checked')) {
            alert("관심분야를 1개 이상 선택하세요");
            return false;
        }
    }); // 폼 submit 끝
}); // ready 끝