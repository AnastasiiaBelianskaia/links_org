const form = $("#modal-form");
const formContent = $("#modal-form .modal-content");
const menu = $("#nav_menu");
const colorpicker = $("#colorpicker");

const loadForm = (e) => {
  $.ajax({
    url: e.target.getAttribute("data-url"),
    type: 'get',
    dataType: 'json',
    beforeSend: () => {
      form.modal("show");
    },
    success: (data) => {
      formContent.html(data.html_form);
    }
  });
};

const saveForm = (e) => {
    const formEl = $(e.currentTarget);
    $.ajax({
      url: formEl.attr("action"),
      data: formEl.serialize(),
      type: formEl.attr("method"),
      dataType: 'json',
      success: (data) => {
          if (data.form_is_valid) {
              formContent.html(`<p>${formEl.attr("data-id")} Added</p>`);
              setTimeout(() => {
                form.modal("hide");
                location.reload();
              }, 1000)
          } else {
            formContent.append(`<p class="modal-error">${formEl.attr("data-id")} already exists</p>`);
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
$(".js-add-category").click(loadForm);
form.on("submit", ".js-link-form", saveForm);
form.on("submit", ".js-category-form", saveForm);
$(".js-copy-link").click(CopyLink);
colorpicker.on("change", changeColor);

getColor();
