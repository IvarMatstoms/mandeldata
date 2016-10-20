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
          color="#fff";
        }
        canvas.fillStyle = color
        canvas.fillRect(i,j,1,1)
        j=j+1
      }
      i=i+1
    }

  })
}
