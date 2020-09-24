$(document).ready(function () {
  $("form").on("submit", function (event) {
    event.preventDefault();
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
      seccess: function () {
      },
    });
  });
});
