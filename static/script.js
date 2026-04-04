console.log("yeah javascript works");
window.onload= function(){
  const button=document.querySelector('.save_button');
  function cheansColor(){
  document.body.style.backgroundColor='red'}
  button.addEventListener('touchstart',cheansColor);
  button.addEventListener('click', cheansColor);
          };