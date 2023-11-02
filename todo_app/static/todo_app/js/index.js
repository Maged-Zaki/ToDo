let url = `ws://${window.location.host}/ws/my_tasks`

const chatSocket = new WebSocket(url)

    chatSocket.onmessage = function(e){
        let data = JSON.parse(e.data)

        let task_content = data["task_content"]
        let task_id = data["task_id"]

        let tr_task = document.getElementById(`${task_id}`)
        tr_task.classList.add("date-reached-js")

        alert(`The following task just reached the finish time: ${task_content}`)


    }





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


function show_group_form() {
    let form_div = document.getElementById("group-form-div");
    let form = document.getElementById("group_form");

    form_div.style.position = "absolute";
    form.style.display = "block";

}

function cancel_group_form() {
    let form_div = document.getElementById("group-form-div");
    let form = document.getElementById("group_form");

    form_div.style.position = "relative";
    form.style.display = "none";
}


document.getElementById("add-task-btn").addEventListener("click", show_form);

document.getElementById("group-task-btn").addEventListener("click", show_group_form);
