if(localStorage.getItem('dokky-theme') != null){
    setTheme(localStorage.getItem('dokky-theme'))
} else {
    setTheme('theme-light');
}

function setTheme(themeName) {
    localStorage.setItem('dokky-theme', themeName);
    document.documentElement.className = themeName;
}

function toggleItem(id){
    var element = document.getElementById(id)
    if(element.style.display === "block" || element.style.display === ""){
        element.style.display = "none"
    } else {
        element.style.display = "block"
    }

}

var links = document.getElementsByClassName('sidebar-link');

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
