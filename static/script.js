console.log("yeah javascript works");
window.onload= function(){
  const button=document.querySelector('.save_button');
  function cheansColor(){
  document.body.style.backgroundColor='red';
  setTimeout(function(){
    document.body.style.backgroundColor='lightgreen'}, 3000);
  };
  button.addEventListener('touchstart',cheansColor);
  button.addEventListener('click', cheansColor);
};
  