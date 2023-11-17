var chats = [];
var chatid = Cookies.get('chatid');

// initialization of chatting at the begining 
start_chatting();

function ask(e) {
  chat(document.getElementById('userInput').value);
  document.getElementById('userInput').value = "";
}