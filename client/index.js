'use strict';

var Chart = require('chart.js');

var data = {
  labels: [
    "Early",
    "Mid-day",
    "Evening",
    "Late"
  ],
  datasets: [
    {
      data: [300, 50, 100, 42],
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

var ctx = document.getElementById('canvas');
var chart = new Chart(ctx, {
  type: 'pie',
  data: data,
  //options: options
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
