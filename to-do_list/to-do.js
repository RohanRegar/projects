const inputbox = document.getElementById("input-box")
const listcontainer = document.getElementById("listcontainer")
console.log(inputbox.value);
function addtask(){
    if (inputbox.value==""){
        alert("Write a task to add");
    }
    else{
        let li = document.createElement("li");
        li.innerHTML=inputbox.value;
        listcontainer.appendChild(li);
        let s  =document.createElement("span")
        s.innerHTML="\u00d7";
        li.appendChild(s);
        savedata();
    }
    inputbox.value="";
}
listcontainer.addEventListener("click",function(e){
    if (e.target.tagName==="LI"){
        e.target.classList.toggle("checked");
        savedata();
    }
    else if (e.target.tagName==="SPAN"){
        e.target.parentElement.remove();
        savedata()
    }
},false);

function savedata(){
    localStorage.setItem("data",listcontainer.innerHTML)
}

function getdata(){
    listcontainer.innerHTML = localStorage.getItem("data");
}

getdata();