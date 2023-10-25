$(document).ready(function(){
    $('#bSearchFrm').on('submit', function(event){
        // submit 이벤트 기본 기능 : 페이지 새로고침
        // 페이지 새로고침 되지 않도록
        event.preventDefault();

        // 폼에 입력한 값들을 쿼리 스트링 방식의 데이터로 변환
        // serialize() 사용 : 쿼리 스트링 방식의 데이터로 변환
        let formData = $(this).serialize();

        $.ajax({
            type:'post',
            url:'http://127.0.0.1:8000/book/search_form/',
            data:formData,
            dataType: 'json',
            success:function(result){
                console.log(result)
                console.log(result.book_list_json)

                let book_list = result.book_list_json;

                // 반환된 결과를 searchResultBox <div>에 테이블 형태로 출력 (삽입)
                // div 태그에 삽입 : append()
                // 실행할 때마다 append() 이전 결과 뒤에 계속 append 됨
                // 다 삭제한 후 append 수행
                $('#searchResultBox').empty()

                // 테이블 태그 문자열로 생성
                const str = `
                    <table id="book_list">
                    <tr>
                        <th>도서번호</th>
                        <th>도서명</th>
                        <th>저자</th>
                        <th>도서가격</th>
                        <th>출간일</th>
                        <th>재고</th>
                        <th>출판사 번호</th>
                    </tr>
                `

                $('#searchResultBox').append(str);

                // 데이터 추출해서 append
                if(book_list.length == 0){
                    $('#book_list').append('<tr align="center"><td colspan="6">찾는 상품이 없습니다</td></tr>')
                } else {
                    for(let i=0; i<book_list.length; i++){
                        $('#book_list').append('<tr><td>' + 
                            book_list[i].pk + '</td><td>' +
                            book_list[i].fields.bookname + '</td><td>' + 
                            book_list[i].fields.bookauthor + '</td><td>' + 
                            book_list[i].fields.bookprice + '</td><td>' + 
                            str(book_list[i].fields.bookdate) + '</td><td>' + 
                            book_list[i].fields.bookstock + '</td><td>' + 
                            book_list[i].fields.pubno + '</td></tr>');
                    }
                }

                $('#searchResultBox').append('</table>');
            },
            error:function(){
                // 오류 발생 시 수행되는 함수
                alert('오류 발생')
            },
            complete:function(){
                // 완료 되었을 때 수행된 함수
            }
        });
    })
});