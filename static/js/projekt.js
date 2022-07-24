const buttons = document.querySelectorAll('.kep');
const overlay = document.querySelector('.overlay');
const overlayImage = document.querySelector('.overlayimagediv img');

function open(e) {
  overlay.classList.add('opened');
  const src= e.currentTarget.querySelector('img').src;
  overlayImage.src = src;
}

function close() {
  overlay.classList.remove('open');
}

buttons.forEach(button => button.addEventListener('click', open));
if (overlay)
    overlay.addEventListener('click', close);

function modositas(){
  $('#modositoform').first().css('display','block');
  $('body').first().css('pointer-events','none');
  $('body').first().css('overflow','hidden');
  $('#modositoform').first().css('pointer-events','auto');

}
window.addEventListener('load', (event) => {
  
});