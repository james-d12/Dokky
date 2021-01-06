const data = document.getElementsByClassName("header-link");

function search(){
    const searchText = document.getElementById("input-search").value.toString();

    for (let index = 0; index < data.length; ++index) {
        if(data[index].innerText.includes(searchText)){
            data[index].style.display = "block";
        }
        else{
            data[index].style.display = "none";
        }   
    }
}

function toggle_sidebar(){
    let visibility = document.getElementById("sidebar-id").style.display;
    
    if(visibility == "none"){
        document.getElementById("sidebar-id").style.display = "block"
        document.getElementById("main-id").style.marginLeft = "450px"
    }
    else{
        document.getElementById("sidebar-id").style.display = "none"
        document.getElementById("main-id").style.marginLeft = "0px"
    }
}

function changeTheme(){
    console.log(document.getElementById('theme').href);
    if (document.getElementById('theme').href.includes("sheets/dark.css")) {
        console.log("Changing to light theme.")
        document.getElementById('theme').href = "sheets/light.css";
    } else {
        console.log("Changing to dark theme.")
        document.getElementById('theme').href = "sheets/dark.css";
    }
}