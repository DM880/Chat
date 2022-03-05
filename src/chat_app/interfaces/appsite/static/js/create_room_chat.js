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

var robot = document.getElementById("robot");
var robot_container = document.getElementById("robot-container");
var robot_after = document.getElementById("robot_after");
var my_info_container = document.getElementById("my-info-container");

  robot.addEventListener("mouseover",function(){
    robot_after.style.display = "block";
    robot.style.display = "none";
    my_info_container.style.display = "block";
  });

  robot_container.addEventListener("mouseleave",function(){
    robot.style.display = "block";
    robot_after.style.display = "none";
    my_info_container.style.display = "none";
  });