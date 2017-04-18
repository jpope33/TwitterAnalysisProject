'use strict';

var express = require('express');
var join = require('path').join;

var app = express();

app.use(express.static(join(__dirname, 'public')));

app.get('/', function (req, res) {
  res.sendFile(join(__dirname, 'public', 'index.html'));
});

app.get('/data', function (req, res) {
  res.json({
    username: 'hello',
    chartData: [
      57, 13, 10, 20
    ]
  });
});

app.listen(8080, function () {
  console.log('hi');
});
