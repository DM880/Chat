// Info

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


// Robot

var robot = document.getElementById("robot");
var robot_after = document.getElementById("robot_after");
var my_info_container = document.getElementById("my-info-container");


robot.addEventListener('click',function(){
  if(robot.style.display == 'block')
  {
    robotAfter();
    }
  else{
    robotBefore();
  }
  });


robot_after.addEventListener('click',function(){
  if(robot_after.style.display == 'block')
  {
    robotBefore();
  }
  else{
    robotAfter();
  }
  });


function robotAfter(){
  robot.style.display = 'none';
  robot_after.style.display = "block";
  my_info_container.style.display = "block";
}

function robotBefore(){
  robot.style.display = "block";
  robot_after.style.display = "none";
  my_info_container.style.display = "none";
}