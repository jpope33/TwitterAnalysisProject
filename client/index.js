import request from 'superagent';
import Chart from 'chart.js';
import React from 'react';
import ReactDOM from 'react-dom';

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

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      chartData: [],
      username: ''
    };

    this.chart = null;
  }
  componentDidMount() {
    this.chart = new Chart(this.canvas, {
      type: 'pie',
      data: createChartDataObject(this.state.chartData),
      //options: options
    });
    request
      .get('/data/andre_zs')
      .end((err, res) => {
        this.setState({
          chartData: res.body.chartData
        });
      });
  }
  componentDidUpdate() {
    this.chart = new Chart(this.canvas, {
      type: 'pie',
      data: createChartDataObject(this.state.chartData),
    });
  }
  handleChange(event) {
    this.setState({
      username: event.target.value
    });
  }
  render() {
    return (
      <div>
        <h1>Twitter User Analysis</h1>
        <div>
          <label>Twitter username:</label>
          <input
            type="text"
            value={this.state.username}
            onChange={this.handleChange}
          />
        </div>
        <canvas ref={(canvas) => this.canvas=canvas} id="canvas"></canvas>
      </div>
    );
  }
}

ReactDOM.render(
  <Main />,
  document.getElementById('root')
);
