
document.getElementById("btn").addEventListener("click",sendlogininfo);

function sendlogininfo(){
    var username = document.getElementById("ID").value;
    var pass = document.getElementById("passwd").value;
    fetch("http://localhost:5000/login", {
    method: "POST",
    redirect: "follow",
    body: JSON.stringify({
        uid: username,
        password: pass,
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    .then((response)=>{         
        if(response.redirected){
            window.location.href = response.url;
        }
        
    });
}