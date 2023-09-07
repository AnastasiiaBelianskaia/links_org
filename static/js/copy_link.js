const CopyLink = (e) => {
    const button = e.target;
    const linkContent = $(`#current-link_${button.getAttribute("data-id")}`).text();
    navigator.clipboard.writeText(linkContent);

    $(".alert").removeClass('d-none');

    setTimeout(() => {
       $(".alert").addClass('d-none')
      }, 2000)
}

$(".js-copy-link").click(CopyLink);