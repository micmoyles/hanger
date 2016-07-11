window.onload = function () {
	var dps = [{x: 1, y: 10}, {x: 2, y: 10}, {x: 3, y: 10}, {x: 4, y: 10}, {x: 5, y: 10}];   //dataPoints. 
	var dps2 = [{x: 1, y: 11}, {x: 2, y: 11}, {x: 3, y: 11}, {x: 4, y: 11}, {x: 5, y: 11}];   //dataPoints. 
 
var chart = new CanvasJS.Chart("chartContainer",{
	title :{
		text: "Historical Book"
	},
	axisX: {						
		title: "Time"
	},
	axisY: {						
		title: "GBP"
	},
	data: [{
		type: "line",
		dataPoints : dps
	},
	{type: "line",
	 dataPoints: dps2
	 }]
});
chart.render();


    var xVal = dps.length + 1;
    var yVal = 100;	
    var updateInterval = 1000;
     
    $('.btn-pause').click(function () {
	clearInterval(interval);
    });
    $('.btn-resume').click(function () {
	setInterval(function(){updateChart()}, updateInterval);
    });
    var updateChart = function () {
    	
    	
    		yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
    		y2Val = yVal - 10;
    		dps.push({x: xVal,y: yVal,});
    		dps2.push({x: xVal,y: y2Val,});
    		
    		
    		xVal++;
    	
    	chart.render();		
};	
    	// update chart after specified time. 
    var interval = setInterval(function(){updateChart()}, updateInterval); 
    
    var doughnutChart = new CanvasJS.Chart("doughnutChartContainer",
    {
      title:{
        text: "Volume Available"
      },
      data: [
      {
       type: "doughnut",
       dataPoints: [
       {  y: 53.37, indexLabel: "Bid" },
       {  y: 35.0, indexLabel: "Ask" },
       ]
     }
     ]
   });
   doughnutChart.render();
}
