const form = $("#modal-linkform");
const formContent = $("#modal-linkform .modal-content");

const loadForm = (e) => {
  $.ajax({
    url: e.target.getAttribute("data-url"),
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      form.modal("show");
    },
    success: function (data) {
      formContent.html(data.html_form);
    }
  });
};

var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
          $("#modal-linkform .modal-content").html('<p>Link Added</p>');
          setTimeout(() => {
            $("#modal-linkform").modal("hide");
            location.reload();
          }, 1000)
      }
    });
    return false;
  };

$(".js-add-link").click(loadForm);
$("#modal-linkform").on("submit", ".js-link-form", saveForm);
