// import Swal from 'sweetalert2' // --> html 파일에 <script> 태그로 cdn ? 추가 시 import 필요 없음.
// import toastr from 'toastr';
// import 'toastr/build/toastr.min.css';

// 기본 알림 기능
document.getElementById("basic").addEventListener("click", () => {
  window.alert(`
    위치 정보를 가져올 수 없습니다.
    위치 정보를 허용하였는지 다시 한 번 확인해주세요..!
    `);
});

// Sweetalert2
document.getElementById("sweet").addEventListener("click", () => {
  Swal.fire({
    title: '위치 정보 가져오기 실패',
    text: "위치 정보를 허용하였는지 다시 한 번 확인해주세요..!",
    icon: 'error',
    confirmButtonText: '확인'
  });
});


// Toastr
document.getElementById("toast").addEventListener("click", () => {
  toastr.options = {
    "closeButton": true,
    // "debug": false,
    // "newestOnTop": false,
    // "progressBar": false,
    "positionClass": "toast-top-full-width",
    // "preventDuplicates": false,
    // "onclick": null,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
  }

  toastr["error"]("위치 정보를 허용하였는지 다시 한 번 확인해주세요..!", "위치 정보 가져오기 실패")


});