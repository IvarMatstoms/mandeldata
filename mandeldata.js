function update(){
  $.get("mandeldata",function(data){
    var mb=JSON.parse(data)
    var WIDTH=mb.length
    var HEIGHT=mb[0].length
    $("#mb").attr("width",WIDTH)
    $("#mb").attr("height",HEIGHT)
    var canvas=document.getElementById("mb").getContext("2d")
    var i=0;
    while(i<WIDTH){
      var j=0;
      while(j<HEIGHT){
        var color="";
        if(mb[i][j]==-1){
          color="#000";
        }else{
		  
          //color="#fff";
		 var red=Math.max((mb[i][j]/100)*255,255)
		  color=rgbToHex(red,255,0)
        }
        canvas.fillStyle = color
        canvas.fillRect(i,j,1,1)
        j=j+1
      }
      i=i+1
    }

  })
}
function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}