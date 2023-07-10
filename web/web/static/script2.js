// 모달창 js - 회원 탈퇴

const btn = document.getElementById('popupBtn tab-01');
const modal2 = document.getElementById('modalWrap');
const closeBtn = document.getElementById('closeBtn');

btn.onclick = function() {
  modal2.style.display = 'block';
}
closeBtn.onclick = function() {
  modal2.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target == modal2) {
    modal2.style.display = "none";
  }
}
