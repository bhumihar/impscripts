var timevariable=0;
var i=0;
bcl=setInterval(function(){
timevariable=Math.random();
b=document.getElementsByClassName('uiTextareaAutogrow _552m')
b[0].value="hello dude " + i
var ev = document.createEvent('KeyboardEvent');
// Send key '13' (= enter)
ev.initKeyEvent(
    'keydown', true, true, window, false, false, false, false, 13, 0);
  b[0].dispatchEvent(ev);
i++
},1000+timevariable*1000)