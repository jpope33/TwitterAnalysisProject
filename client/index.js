'use strict';

var Chart = require('chart.js');

var request = require('superagent');

function createChartDataObject(data) {
  return {
    labels: [
      "Early",
      "Mid-day",
      "Evening",
      "Late"
    ],
    datasets: [
      {
        data: data,
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#CEFF56"
        ],
        hoverBackgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#CEFF56"
        ]
      }
    ]
  };
}

var ctx = document.getElementById('canvas');
var chart;

//var req = {
  //username: 'andre_zs'
//};

request
  .get('/data/andre_zs')
  .end(function (err, res) {
    //console.log(res.body);
    chart = new Chart(ctx, {
      type: 'pie',
      data: createChartDataObject(res.body.chartData),
      //options: options
    });
  });



//var chart = new Chart(ctx, {
  //type: 'bar',
  //data: data,
  //options: {
    //scales: {
      //yAxes: [{
        //ticks: {
          //beginAtZero:true
        //}
      //}]
    //}
  //}
//});
