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
      formValue: ''
    };

    this.chart = null;
  }
  componentDidMount() {
    this.chart = new Chart(this.canvas, {
      type: 'pie',
      data: createChartDataObject(this.state.chartData),
    });
  }
  fetch(username) {
    request
      .get('/data/' + username)
      .end((err, res) => {
        this.setState({
          chartData: res.body.chartData
        });
      });
  }
  componentDidUpdate() {
    this.chart.data.datasets[0].data = this.state.chartData;
    this.chart.update();
  }
  handleChange(event) {
    const username = event.target.value;
    this.setState({
      formValue: username
    });
  }
  handleOnKeyPress(event) {
    if (event.key === 'Enter') {
      const username = event.target.value;
      this.submit(username);
    }
  }
  submit(username) {
    this.setState({
      username: username
    });
    
    if (username !== '') {
      this.fetch(username);
    }
  }
  handleSubmitPress(e) {
    e.preventDefault();
    this.submit(this.state.formValue);
  }
  render() {
    return (
      <div>
        <h1>Twitter User Analysis</h1>
        <div>
          <label>Twitter username:</label>
          <input
            type="text"
            value={this.state.formValue}
            onChange={(e) => this.handleChange(e)}
            onKeyPress={(e) => this.handleOnKeyPress(e)}
          />
          <button onClick={e => this.handleSubmitPress(e)}>Submit</button>
        </div>
        <canvas ref={canvas => this.canvas=canvas} id="canvas"></canvas>
      </div>
    );
  }
}

ReactDOM.render(
  <Main />,
  document.getElementById('root')
);
