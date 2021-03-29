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

function changeTheme(){
    const themeElement = document.getElementById('theme')
    const themeChangeText = document.getElementById('changeThemeText')

    if(themeElement.href.includes("dark_theme.css")){
        themeElement.href = themeElement.href.replace("dark_theme.css", "light_theme.css")
        themeChangeText.innerHTML = "Switch To Dark Theme"
    } else {
        themeElement.href = themeElement.href.replace("light_theme.css", "dark_theme.css")
        themeChangeText.innerHTML = "Switch To Light Theme"
    }
}