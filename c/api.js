async function start_chatting(context, model) {
  let r = await fetch("/chat/", {
      method: "POST",
      mode: "no-cors",
      headers: { 
          'Content-Type': 'application/json',
          'Model': model
      }
  })
  if (typeof context == "string" && context != "")
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
  console.log(chatid)
  chatid = chatid.chatid;
  Cookies.set('chatid', chatid);
}
async function chat(message) {
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
  chats.push({ 'role': 'assistant', 'message': res })
  console.log(chats[chats.length - 1])
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
}