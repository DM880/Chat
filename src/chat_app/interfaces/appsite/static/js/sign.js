window.addEventListener("resize",function(){
  if(window.matchMedia("(max-width: 500px)").matches){
    document.getElementById("wrap-div").classList.remove('wrap');
    document.getElementById("wrap-div").classList.add('phone');
  }
  else{
    document.getElementById("wrap-div").classList.add('wrap');
    document.getElementById("wrap-div").classList.remove('phone');
  }
})