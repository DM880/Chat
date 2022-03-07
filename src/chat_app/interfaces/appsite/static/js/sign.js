// Check min requirements password

var check_password = function() {

  password1 = document.getElementById('password1');
  password2 = document.getElementById('password2');
  button = document.getElementById('btn-submit');
  message = document.getElementById('message-div');

  if ((password1.value == password2.value) && password1.value.length > 7) {
    button.type = "submit";
    password1.style.color = '#6ECB63';
    password2.style.color = '#6ECB63';
    message.innerHTML = 'Password matching';
    message.style.color = '#6ECB63';
  }
  else if(password1.value.length > 7) {
    button.type = "button";
    password1.style.color = '#DA1212';
    password2.style.color = '#DA1212';
    message.innerHTML = 'Password not matching';
    message.style.color = '#DA1212';
  }
  else{
    button.type = "button";
    password1.style.color = '#DA1212';
    password2.style.color = '#DA1212';
    message.innerHTML = 'Password must be at least 8 characters';
    message.style.color = '#DA1212';
  }
}