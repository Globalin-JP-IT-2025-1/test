// alert2
function openPopup() {
    window.open(
        'popup.html', // 열고자 하는 HTML 파일 경로
        '팝업창', // 창의 이름
        'width=800,height=600,toolbar=no,scrollbars=no,resizable=no,menubar=no,status=no' // 옵션 설정
    );
}

function closePopup() {
    window.close();
}