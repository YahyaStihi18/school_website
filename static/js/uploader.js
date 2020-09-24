function check_ex() {
  var fullPath  = document.getElementById("id_video").value;
  if (fullPath) {
    var startIndex =
      fullPath.indexOf("\\") >= 0
        ? fullPath.lastIndexOf("\\")
        : fullPath.lastIndexOf("/");
    var filename = fullPath.substring(startIndex);
    if (filename.indexOf("\\") === 0 || filename.indexOf("/") === 0) {
      filename = filename.substring(1);
    }
    var x = filename.split('.').pop();
    if (x != 'mp4') {
      alert(x +' format is not allowed in video input, use only (mp4) extensions');
      location.reload()
    };
    
  }
}

$(document).ready(function () {
  $("form").on("submit", function (event) {
    event.preventDefault();
    check_ex();
    var formData = new FormData($("form")[0]);
    $.ajax({
      xhr: function () {
        var xhr = new window.XMLHttpRequest();
        xhr.upload.addEventListener("progress", function (e) {
          if (e.lengthComputable) {
            document.getElementById("loading_btn").classList.remove("d-none");
            document.getElementById("save_btn").classList.add("d-none");
            document.getElementById("progressdiv").classList.remove("d-none");

            var percent = Math.round((e.loaded / e.total) * 100);
            if (percent == 100) {
              document.getElementById("message_button").click();
            }

            $("#progressbar")
              .attr("aria-valuenow", percent)
              .css("width", percent + "%")
              .text(percent + " %");
          }
        });
        return xhr;
      },
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      seccess: function () {},
    });
  });
});
