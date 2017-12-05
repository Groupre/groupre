$(document).ready(function(){
    document.getElementById('bourne').onclick() = function(){
        alert('From Static');        
        var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
        xmlhttp.open("POST", "/json-handler");
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        xmlhttp.send(JSON.stringify({name:"Json Bourne", time:"2pm"}));
    };
});
