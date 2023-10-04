setInterval(()=>{
    let d = new Date();
    hour.innerHTML = (d.getHours()<10 ? "0":"" )+ d.getHours();
    minute.innerHTML = (d.getMinutes()<10 ? "0":"" )+ d.getMinutes();
    second.innerHTML = (d.getSeconds()<10 ? "0":"" )+ d.getSeconds();
},
1000)