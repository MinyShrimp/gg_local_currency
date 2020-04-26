
//////////////////////////////////////////////////////////////////////////
// 데이터 찾기
//////////////////////////////////////////////////////////////////////////
$(document).ready(function() {
    $('#submit').click(function() {
        if($("input[name=REFINE_LOTNO_ADDR]").val() == '' && $("input[name=CMPNM_NM]").val() == '' && $("input[name=INDUTYPE_NM]").val() == '') {
            alert('셋 중 하나는 입력해야 합니다.');
            return false;
        }
    });
});