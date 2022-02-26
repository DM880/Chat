const roomName = JSON.parse(document.getElementById('room-name').textContent);

        var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

        const chatSocket = new WebSocket(
            ws_scheme
            + '://'
            + window.location.host
            +'/chats/'
            + roomName
            + '/'
        );

     chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);

            var time_data = new Date();

            var date = getDate(time_data);
            var time = getTime(time_data);

            var timestamp = date + ', ' + time;

            // Get css class based on handler
            var classes = handler(data.message);

            var html_message = '<div class="message '+classes+'">'
                                + (data.message + '\n') + '<br><p class="timestamp">'+ timestamp +'</p></div>';

            // Show message
            document.querySelector('#chat-log').innerHTML += html_message;

            // Keep bottom page on added content
            window.scrollTo(0,document.body.scrollHeight);
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

           document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            const room_name = JSON.parse(document.getElementById('room-name').textContent);
            const username = JSON.parse(document.getElementById('username').textContent);
            chatSocket.send(JSON.stringify({
                'message': message,
                'username': username,
                'room_name':room_name,
            }));
            messageInputDom.value = '';
        };


// Get css class
function handler(message){

    var username = JSON.parse(document.getElementById('username').textContent);

    var sender = message.substr(0,username.length)

    if(sender == username){
        return 'sender-message';
        }
    else{
        return 'receiver-message';
        }
}


// Load page at bottom

window.onload = function () {
  window.scrollTo(0,document.body.scrollHeight);
}

// Timestamp functions

const month_names = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"];

function getDate(timestamp){
    var month = month_names[timestamp.getMonth()].substring(0,3);
    var day = timestamp.getDate();
    var year = timestamp.getFullYear();
    var date = month + '. ' + day + ', ' + year;
    return date;
}


function getTime(timestamp){
    var hours = timestamp.getHours();
    var minutes = timestamp.getMinutes();
    var make_time = hours >= 12 ? 'p.m.' : 'a.m.';
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var time = hours + ':' + minutes + ' ' + make_time;
    return time;
}


// function random_color(){
//     var colors = ['#FF6464', '#FFE162', '#0000ff'];
//     var random = colors[Math.floor(Math.random() * colors.length)];
//     return random;
// }