 function phoneWrapDiv(){
  var width = screen.width;
  if(width < 500){
    document.getElementById("wrap-div").classList.remove('wrap');
    document.getElementById("wrap-div").classList.add('phone');
  }
  else{
    document.getElementById("wrap-div").classList.add('wrap');
    document.getElementById("wrap-div").classList.remove('phone');
  }
}