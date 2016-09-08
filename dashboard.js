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
}
