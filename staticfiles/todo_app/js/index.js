
function show_form() {
    let form_div = document.getElementById("form-div");
    let form = document.getElementById("form");

    form_div.style.position = "absolute";
    form.style.display = "block";

}

function cancel() {
    let form_div = document.getElementById("form-div");
    let form = document.getElementById("form");

    form_div.style.position = "relative";
    form.style.display = "none";
}

document.getElementById("add-task-btn").addEventListener("click", show_form);
