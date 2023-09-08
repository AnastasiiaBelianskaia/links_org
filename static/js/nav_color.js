const menu = $("#nav_menu");
const colorpicker = $("#colorpicker");

const getColor = () => {
    const color = localStorage.getItem("color");
    menu.attr('style', `background-color: ${color} !important`);
}

const changeColor = () => {
    const color = colorpicker.val();
    localStorage.setItem("color", color);
    getColor();
}

colorpicker.on("change", changeColor);

getColor();