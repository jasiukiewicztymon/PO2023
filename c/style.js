window.onload = (e) => {
    let l = document.getElementById('resizer');
    let h = l.querySelector('header'),
        chat = l.querySelector('#chat'),
        cin = l.querySelector('#chatInput'),
        f = l.querySelector('footer');

    let min = 0;

    Array.prototype.slice.call(chat.children).forEach(element => {
      //console.log(element, element.offsetHeight, element.getBoundingClientRect())
      min += element.offsetHeight;
    });

    if (l.offsetHeight - (cin.offsetHeight + h.offsetHeight + f.offsetHeight) > min)
      chat.style.height = `calc(100vh - ${cin.offsetHeight + h.offsetHeight + f.offsetHeight}px)`;
    else chat.style.height = `${min}px`;

    let cc = chat.querySelector('#chatclouds'),
        d = (chat.querySelector('#context').offsetHeight + chat.querySelector('#chatInput').offsetHeight);

    min = 680;
    h = chat.offsetHeight - d;

    //console.log(h, min)

    if (h > min) cc.style.height = `calc(100% - ${d + 20}px)`
    else cc.style.height = `${min}px`
}

window.onresize = window.onload;

function textareaModifier(e, max, min) {
  let t = e.target;
  t.rows = min;
  let r = t.scrollHeight / 24;
  t.rows = r < max ? r : max;

  window.onload();
}