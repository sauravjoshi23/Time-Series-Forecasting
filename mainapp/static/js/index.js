function getX(cnt, data) {
        //console.log(cnt, data[cnt])
        val = data[cnt]['Date']
        //console.log(val)
         return val;
}

function getY(cnt, data) {
        //console.log(cnt, data[cnt])
        val = data[cnt]['Sales']
        //console.log(val)
         return val;
}

var cnt = 0
var data = model_data.replace(/'/g, '"');
data = JSON.parse(data)
var len = data.length

Plotly.plot('chart',[{
        x:[getX(cnt, data)],
        y:[getY(cnt, data)],
        type:'linear'
}]);

setInterval(function() {
    cnt += 1
  if(cnt < len)
  {
    Plotly.extendTraces('chart', { x: [[getX(cnt, data)]], y: [[getY(cnt, data)]] }, [0])
  }
}, 10);
