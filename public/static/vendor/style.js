var y=window.pageYOffset;
window.onscroll=function(){
   
    if(window.pageYOffset>420){
        console.log(window.pageYOffset)
        document.getElementById("nav2").style.top="0px";
    }
    else{
        document.getElementById("nav2").style.top="-55px";

    }
}

document.getElementById("on").addEventListener('click',function(){
document.getElementById("nav3").style.left="0";
});
document.getElementById("off").addEventListener('click',function(){
document.getElementById("nav3").style.left="-20%";
});

