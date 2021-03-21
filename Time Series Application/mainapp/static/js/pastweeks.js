// Future Week Form AJAX
$('#form2').on('submit', function(e){
  e.preventDefault();
  $.ajax({
       type : "POST",
       url: "/pastweeks/",
       data: {
        weeks : $('#weeks2').val(),
        ci : $('#ci2').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        dataType: "json",
       },

       success: function(data){
          //console.log(data)
          //console.log(typeof data)
          //plotting data
          pastweeksjs(data)
       },
       error: function(errorMessage) {
            console.log(errorMessage)
       }
   });
});


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

function pastweeksjs(send) {
    var cnt = 0
    var data = send.replace(/'/g, '"');
    data = JSON.parse(data)
    var len = data.length

    var sales = []
    var dates =[]
    var mean_ci_lower = []
    var mean_ci_upper = []
    var true_sales = []

    var i;
    for (i = 0; i < len; i++) {
        sales.push(data[i]['Sales'])
        dates.push(data[i]['Date'])
        mean_ci_lower.push(data[i]['Mean_CI_lower'])
        mean_ci_upper.push(data[i]['Mean_CI_upper'])
        true_sales.push(data[i]['True_Sales'])
    }

//    console.log(sales)
//    console.log(dates)
//    console.log(mean_ci_lower)
//    console.log(typeof mean_ci_upper)

    var trace1 = {
      x: dates,
      y: mean_ci_lower,
      type: 'scatter',
      name:'mean_ci_lower'
    };

    var trace2 = {
      x: dates,
      y: sales,
      type: 'scatter',
      'name':'sales'
    };

    var trace3 = {
      x: dates,
      y: mean_ci_upper,
      type: 'scatter',
      'name':'mean_ci_upper'
    };

    var trace4 = {
      x: dates,
      y: true_sales,
      type: 'scatter',
      'name':'true_sales'
    };

    var plot_data = [trace1, trace2,trace3,trace4];

    Plotly.newPlot('pastweeks', plot_data);


//    Plotly.plot('futureweeks',[{
//            x:[getX(cnt, data)],
//            y:[getY(cnt, data)],
//            type:'line'
//    }]);
//
//    setInterval(function() {
//        cnt += 1
//      if(cnt < len)
//      {
//        Plotly.extendTraces('futureweeks', { x: [[getX(cnt, data)]], y: [[getY(cnt, data)]] }, [0])
//      }
//    }, 10);
}