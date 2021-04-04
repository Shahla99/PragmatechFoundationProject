## Slider
1. Slider-container icherisinde slide-image onun icherisine shekilleri daxil edirik. 
2. Css de stilleri veririk 
3. index 0 yaziriq 
var slideIndex = 0;
Myslider(); 
4. Daha sonra function() yaziriq 
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
kod her defe yerine yetirilende bir deyer artir (oz-ozune prev,next buttonlari yoxdur)
5. slideIndex++;
  if (slideIndex > x.length) {slideIndex = +1}
  x[slideIndex-1].style.display = "block"; 
sonuncu slide chatdiqdan sonra yene birinciye qayitsin deye 
6. setTimeout(Myslider, 2000);
} setTimeout ise mueyyen saniye sonra funksiya icra olunsun deye  
