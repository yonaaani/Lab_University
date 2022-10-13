function str_del(){
   selection = window.getSelection().toString();
   var str = document.getElementById("elem").textContent;
   var start = str.indexOf(selection);
   var end = start+selection.length;
   var result = str.slice(0,start) + str.slice(end);
   document.getElementById("elem").textContent = result;
}

function getProperty(){
var obj = {
key:'value'
};
var output = getProperty(obj, 'key');
console.log(output);
}