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

const deleteButton = (e) => {
    const delButton = e.target;
    const linkId = delButton.getAttribute("data-id");
    const token = delButton.getAttribute("data-token");
    form.modal("show");
    formContent.html(
        "<button class='btn btn-outline-secondary pb-3 pt-2 pl=2 pr=2' id='cansel_delete'>cansel</button>" +
        "<button class='btn btn-primary pb-3 pt-2 pl=2 pr=2' id='success_delete'>confirm delete</button>"
    )

    const actionDelete = () => (
        $.ajax({
          url: `/linksorg/delete_link/${linkId}/`,
          data: {
            csrfmiddlewaretoken: token,
            pk: linkId
          },
          type: "post",
          dataType: 'json',
          complete: (xhr) => {
              if (xhr.status === 200) {
                formContent.html("<p>Link is deleted</p>");
                setTimeout(() => {
                  form.modal("hide");
                  location.reload();
                }, 1000)
              }
          }
        })
    )

    $("#success_delete").click(actionDelete);
    $("#cansel_delete").click(() => form.modal("hide"));
}

$(".js-add-link").click(loadForm);
$(".js-add-category").click(loadForm);
$(".js-delete-link").click(deleteButton);
form.on("submit", ".js-link-form", saveForm);
form.on("submit", ".js-category-form", saveForm);
$(".js-copy-link").click(CopyLink);
colorpicker.on("change", changeColor);

getColor();
