window.onload = function () {


    var doughnutChart = new CanvasJS.Chart("doughnutChartContainer",
    {
      title:{
        text: "Current Tracked Production"
      },
      data: [
      {
       type: "doughnut",
       dataPoints: [
       {  y: 95.37, indexLabel: "Active" },
       {  y:  4.0, indexLabel: "Inactive" },
       ]
     }
     ]
   });
   doughnutChart.render();

    var dps = [{x: 1, y: 11}, {x: 2, y: 12}, {x: 3, y: 11}, {x: 4, y: 10}, {x: 5, y: 11}, {x:6,y:12},{x:7,y:12.5}];   //dataPoints. 
 
    var chart = new CanvasJS.Chart("lineChartContainer",{
	title :{
		text: "System Frequency"
	},
	axisX: {						
		title: "Time"
	},
	axisY: {						
		title: "Hertz"
	},
	data: [{
		type: "line",
		dataPoints : dps
	 }]
});
chart.render();
var xVal = dps.length + 1;
var yVal = 10;	
var updateInterval =  500;
var updateChart = function () {
      	
      	
      	yVal = yVal +  Math.round(1 + Math.random() *(-1-1));
      	dps.push({x: xVal,y: yVal});
      	
      	xVal++;
      	if (dps.length > 200 )
      	{
      		dps.shift();				
      	}

      	chart.render();		

	// update chart after specified time. 

};
setInterval(function(){updateChart()}, updateInterval); 
}
