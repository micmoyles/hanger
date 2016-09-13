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

    var dps = [{x: 1, y: 11}, {x: 2, y: 11}, {x: 3, y: 11}, {x: 4, y: 11}, {x: 5, y: 11}];   //dataPoints. 
 
    var chart = new CanvasJS.Chart("lineChartContainer",{
	title :{
		text: "System Frequency"
	},
	axisX: {						
		title: "Hertz"
	},
	axisY: {						
		title: "min"
	},
	data: [{
		type: "line",
		dataPoints : dps
	 }]
});
chart.render();
}
