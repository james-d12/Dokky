const links = document.getElementsByClassName("header-link");
const checkboxes = document.getElementsByClassName("toggle-checkbox");

function search(){
    const length = links.length;
    const searchText = document.getElementById("input-search").value.toString();

    for (let index = 0; index < length; ++index) {
        if(links[index].innerText.includes(searchText)){
            links[index].style.display = "block";
        } else{
            links[index].style.display = "none";
        }   
    }
}

function toggleSidebar(){
    const visibility = document.getElementById("sidebar-id").style.display;

    switch (visibility) {
        case "none":
            document.getElementById("sidebar-id").style.display = "block"
            document.getElementById("main-id").style.marginLeft = "450px"
            break;
        default:
            document.getElementById("sidebar-id").style.display = "none"
            document.getElementById("main-id").style.marginLeft = "0px"
            break;
    }
}

function toggleCheckboxes(){
    const length = checkboxes.length;
    for(let index = 0; index < length; ++index){
        const item = checkboxes[index];
        item.checked = !item.checked;
    }
}

function changeTheme(){
    if (document.getElementById('theme').href.includes("sheets/dark.css")) {
        console.log("Changing to light theme.")
        document.getElementById('theme').href = "sheets/light.css";
    } else {
        console.log("Changing to dark theme.")
        document.getElementById('theme').href = "sheets/dark.css";
    }
}