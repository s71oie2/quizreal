// 로그인해야 메뉴 들어가짐 알림창
function needLogin() {
    var con_test = confirm("로그인이 필요합니다.");
    if(con_test){
      location.href ='/user/login/'
    }
}

// summernote 에디터 설정
$(document).ready(function() {
     $('#summernote').summernote({
         height: 300,
         minHeight: null,
         maxHeight: null,
         airMode: true,  // 테두리가 사라짐

     });
    // 5.28 소이
    $(this).summernote("insertImage", url);
});

// 5.28 소이
//노트 쓰기 금지
$(document).ready(function(){
    // 안 써지게 막음
    $('.note-editable').attr('contenteditable', false)
});

