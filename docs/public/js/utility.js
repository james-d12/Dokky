var sidebar = document.getElementById('sidebar');
var links = document.getElementsByClassName('sidebar-link');

window.onload = function() {
    if(localStorage.getItem('dokky-theme') != null){
        setTheme(localStorage.getItem('dokky-theme'))
    } else {
        setTheme('theme-light');
    }
};

function setTheme(themeName) {
    localStorage.setItem('dokky-theme', themeName);
    document.documentElement.className = themeName;
}

function toggleSidebar(){
    var display = window.getComputedStyle(sidebar).display

    if(display === "flex"){
        console.log("disabling sidebar");
        sidebar.style.display = "none"
    } else {
        console.log("enabling sidebar");
        sidebar.style.display = "flex"
    }
}

function toggleItem(id){
    var element = document.getElementById(id)
    var display = window.getComputedStyle(element).display

    if(display === "block"){
        element.style.display = "none"
    } else {
        element.style.display = "block"
    }
}

function search(){
    var length = links.length;
    var searchText = document.getElementById("input-search").value.toString();

    for (let index = 0; index < length; ++index) {
        if(links[index].innerText.includes(searchText)){
            links[index].style.display = "block";
        } else{
            links[index].style.display = "none";
        }   
    }
}
