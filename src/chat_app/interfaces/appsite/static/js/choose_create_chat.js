// Checkboxes

function check(input){
    var checkboxes = document.getElementsByClassName("type-chat");

    for(var i = 0; i < checkboxes.length; i++)
    {
  		//uncheck all
  		if(checkboxes[i].checked == true)
  		{
  			checkboxes[i].checked = false;
  		}
  	}
  	//set checked of clicked object
  	if(input.checked == true)
  	{
  		input.checked = false;
  	}
  	else
  	{
  		input.checked = true;
  	}
}


// Show/Hide Key Input

function hideKey(input){
   var key = document.getElementById('create-key');

    if(input.checked){
      key.style.opacity = 0;
      key.readOnly = true;
      key.required = false;
    }
}


function showKey(input){

 var key = document.getElementById('create-key');

    if(input.checked){
      key.style.opacity = 1;
      key.readOnly = false;
      key.required = true;
    }
}