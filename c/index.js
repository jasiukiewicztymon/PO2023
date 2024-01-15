var chats = [];
var chatid = Cookies.get('chatid');

if (Cookies.get('chatid')) get_chat();
else start_chatting();
// initialization of chatting at the begining 


function ask(e) {
  let userinput = document.getElementById('userInput').value;
  if (document.getElementById('userInput').value.length < 1) {
    window.alert("Ton message ne peut pas être vide!");
    return;
  }

  chat(userinput);
  let u = document.createElement('div');
  u.innerText = userinput;
  document.getElementById('chatclouds').appendChild(u);
  document.getElementById('userInput').value = "";
  document.getElementById('userInput').rows = 2;
}

function restart(e) {
  s = document.getElementById('send');
  s.disabled  = "true";
  document.getElementById('chatclouds').replaceChildren();
  start_chatting(document.getElementById('contextInput').value);
  document.getElementById('contextInput').value = "";
  s.removeAttribute('disabled')
}
