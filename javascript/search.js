

function search(){
    let data = document.getElementsByClassName("header-link");
    let searchText = document.getElementById("input-search").value.toString()

    for (let index = 0; index < data.length; index++) {
        data[index].style.display = "block"
        const text = data[index].innerText

        if(!text.includes(searchText)){
            data[index].style.display = "none"
        }
    }
}