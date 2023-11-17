async function start_chatting(context, model) {
  r = await fetch("/chat/", {
      method: "POST",
      mode: "no-cors",
      headers: { 
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'context': context || '',
        'model': model || ''
      })
  })
  chatid = await r.json();
  //console.log(chatid)
  chatid = chatid.chatid;
  console.warn('Changed API')
  Cookies.set('chatid', chatid);
}
async function chat(message) {
  chats.push(message)
  let ui = document.getElementById('userInput'),
  s = document.getElementById('send');

  s.disabled  = "true";

  //console.log(ui, s)

  let r = await fetch(`/chat/${chatid}/`, {
      method: "POST",
      mode: "no-cors",
      headers: { 
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'question': message
      })
  })
  
  let res = await r.json();
  chats.push(res.content)
  //console.log(chats[chats.length - 1])

  let u = document.createElement('div');
  u.innerText = chats[chats.length - 1];
  document.getElementById('chatclouds').appendChild(u);

  s.removeAttribute('disabled')
}
async function get_chat() {
  let r = await fetch(`/chat/${chatid}/`, {
      method: "GET", 
      mode: "no-cors",
      headers: { 
          'Content-Type': 'application/json',
      }
  })
  
  let res = await r.json();

  console.log(res)

  if (res.status == 'error' || res.content.length == 0) start_chatting()
  else {
    let i = 0;
    if (res.content[0].role != 'user') i++;
  
    for (;i<res.content.length;i++) {
      let u = document.createElement('div');
      u.innerText = res.content[i].content;
      document.getElementById('chatclouds').appendChild(u);
    }
  }
}