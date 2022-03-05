var info_menu = document.getElementById('info-menu');
var info = document.getElementById('info');

  info_menu.addEventListener('mouseover',function(){
    info.style.display = 'block';
});

  info_menu.addEventListener('mouseleave',function(){
    info.style.display = 'none';
});


  info_menu.addEventListener('click',function(){
 if(info.style.display == 'block')
 {
   info.style.display = 'none';
  }
  else{
    info.style.display = 'block';
  }
});