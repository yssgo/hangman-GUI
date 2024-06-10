//hangman-GUI.js  
  'use strict'
  window.addEventListener("DOMContentLoaded", (event)=>{
    let comment_spans =document.querySelectorAll(".token.comment");
    for(let i=0; i < comment_spans.length; i++){
      let html_code = comment_spans[i].innerHTML;
      let re_anchor = RegExp(/\[([^\]]+)\]\(([^\)]+)\)/, "gm");
      comment_spans[i].innerHTML = html_code.replace(re_anchor, "<a href=\"$2\">$1</a>");
    }
  });
  
