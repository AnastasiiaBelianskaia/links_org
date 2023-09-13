const form = $("#modal-linkform");
const formContent = $("#modal-linkform .modal-content");
const menu = $("#nav_menu");
const colorpicker = $("#colorpicker");

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
          if (data.form_is_valid) {
              $("#modal-linkform .modal-content").html('<p>Link Added</p>');
              setTimeout(() => {
                $("#modal-linkform").modal("hide");
                location.reload();
              }, 1000)
          } else {
            $("#modal-linkform .modal-content").append('<p class="modal-error">Link already exists</p>');
          }
      }
    });
    return false;
  };

 const CopyLink = (e) => {
    const button = e.target;
    const linkContent = $(`#current-link_${button.getAttribute("data-id")}`).text();
    navigator.clipboard.writeText(linkContent);

    $(".alert").removeClass('d-none');

    setTimeout(() => {
       $(".alert").addClass('d-none')
      }, 2000)
}

const getColor = () => {
    const color = localStorage.getItem("color");
    menu.attr('style', `background-color: ${color} !important`);
}

const changeColor = () => {
    const color = colorpicker.val();
    localStorage.setItem("color", color);
    getColor();
}

$(".js-add-link").click(loadForm);
$("#modal-linkform").on("submit", ".js-link-form", saveForm);
$(".js-copy-link").click(CopyLink);
colorpicker.on("change", changeColor);

getColor();
