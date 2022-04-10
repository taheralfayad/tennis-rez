var today = new Date();
var last = new Date();
var dd = today.getDate();
var lastday = dd + 2;
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
    
today = yyyy + '-' + mm + '-' + dd;
last = yyyy + '-' + mm + '-' + lastday;


document.getElementById("datefield").setAttribute("min", today);
document.getElementById("datefield").setAttribute("max", last);