const prev = document.querySelector(".prev");
const openn = document.querySelector(".open");
const high = document.querySelector(".high");
const low = document.querySelector(".low");
const predicted_price = document.querySelector(".predicted_price");

if(openn.innerText>prev.innerText){
    openn.style.color = '#38E177';
}else{
    openn.style.color = '#EA2831';
}

if(predicted_price.innerText>openn.innerText && predicted_price.innerText>prev.innerText){
    predicted_price.style.color = '#38E177';
}else if(predicted_price.innerText<openn.innerText && predicted_price.innerText>prev.innerText){
    predicted_price.style.color = 'yellow'
}else{
    predicted_price.style.color = '#EA2831';
}

high.style.color = '#38E177';
low.style.color = '#EA2831';

const words = document.querySelectorAll('.word-changer > span')

let main = gsap.timeline({repeat: -1});

for (let i = 0; i < words.length; i++) {
  let delay = i*2 - 1;
  let wordTL = gsap.timeline();
  if(i !== 0) {
    wordTL.from(words[i], 1, { y: '-60%', opacity: 0 ,ease: 'SlowMo.out' });
  }
  
  if(i !== words.length - 1) {
    wordTL.to(words[i], 1, { y: '80%', opacity: 0, ease: 'SlowMo.out'});
  }
  main.add(wordTL, delay);
}

gsap.to('.stock-symbol',{
  opacity: 1,
  repeat : -1,
  duration : 2.5
})