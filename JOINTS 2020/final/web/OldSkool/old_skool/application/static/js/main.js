
$(document).ready(function(){
  $("#profile_form").submit(function(e) {
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    var url = "/profile";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        window.location.href = "/profile";
      }
    };
  
    var form_submit = document.forms[0]
    var data = JSON.stringify({"bio": form_submit.bio.value, "motto": form_submit.motto.value});
    xhr.send(data);
  });

  notif_msg = $("#notif_msg");
  if(notif_msg){
    notif_msg.slideUp(3000);
  }

});

function reportcurhat(id){
  $.ajax({
    url: window.location.origin + "/report",
    data: {'curhat_link' : window.location.origin + "/curhat/" + id},
    type: 'POST',
    cache: false,
    success: function(data){
      alert("Report Sukses, Curhat Akan di Cek Admin");
    }
});

}

