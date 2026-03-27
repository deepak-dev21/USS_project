async function sendData(){
    let data = document.getElementById("data").value;
    let secure = document.getElementById("secure").checked;

    let res = await fetch("/send",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({data,secure})
    });

    let out = await res.json();
    document.getElementById("output").innerText = JSON.stringify(out,null,2);
}

async function loadLogs(){
    let res = await fetch("/logs");
    let data = await res.json();
    document.getElementById("logs").innerText = JSON.stringify(data,null,2);
}