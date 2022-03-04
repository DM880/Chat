function openInfo(){
  document.getElementById('info').style.display = 'block';
}


function closeInfo(){
  document.getElementById('info').style.display = 'none';
}


function openCloseInfo(){
 var info = document.getElementById('info');

 if(info.style.display == 'block')
 {
   info.style.display = 'none';
  }
  else{
    info.style.display = 'block';
  }

}