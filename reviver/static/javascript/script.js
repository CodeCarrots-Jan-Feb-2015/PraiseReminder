
function validateForm(){
    
    var x = document.getElementById("text").value;
    if(x == null || x == ""){
        alert("Please enter text");
    }else{
    alert("Are you sure you want to submit: " + x + "?");
    }
//    if (x == null || x == "") {
//        alert("Please enter text!");
//    }else{
//    alert("Thank you for your submission!");
//    }
}
