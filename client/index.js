import request from 'superagent';
import Chart from 'chart.js';
import React from 'react';
import ReactDOM from 'react-dom';
import randomcolor from 'randomcolor';

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


const colors = [];

for (let i = 0; i < 10; i++) {
  colors.push(randomcolor);
}

function createWordChartObject(data) {
  //const colors = data.map(() => randomcolor());
  return {
    labels: data.map(x => x.word),
    datasets: [
      {
        data: data.map(x => x.frequency),
        backgroundColor: colors,
        hoverBackgroundColor: colors
      }
    ]
  };
}

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      chartData: [],
      wordData: [],
      formValue: ''
    };

    this.chart = null;
  }
  componentDidMount() {
    this.chart = new Chart(this.canvas, {
      type: 'pie',
      data: createChartDataObject(this.state.chartData),
    });

    this.wordChart = new Chart(this.wordCanvas, {
      type: 'pie',
      data: createWordChartObject(this.state.wordData),
    });

  }
  fetch(username) {
    request
      .get('/data/' + username)
      .end((err, res) => {
        this.setState({
          chartData: res.body.chartData,
          wordData: res.body.wordData
        });
      });
  }
  componentDidUpdate() {
    this.chart.data.datasets[0].data = this.state.chartData;
    this.chart.update();

    this.wordChart.data.datasets[0].data = this.state.wordData.map(x => x.frequency);

    //const colors = this.state.wordData.map(() => randomcolor());
    //this.wordChart.data.datasets[0].backgroundColor = colors;
    //this.wordChart.data.datasets[0].hoverBackgroundColor = colors;
    this.wordChart.config.data.labels = this.state.wordData.map(x => x.word);
    this.wordChart.update();
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
        <div className='form'>
          <label>Twitter username:</label>
          <input
            type="text"
            value={this.state.formValue}
            onChange={(e) => this.handleChange(e)}
            onKeyPress={(e) => this.handleOnKeyPress(e)}
          />
          <button onClick={e => this.handleSubmitPress(e)}>Submit</button>
        </div>
        <div className='half'>
          <h2>Posting times</h2>
          <canvas ref={canvas => this.canvas=canvas} id="canvas"></canvas>
        </div>
        <div className='half'>
          <h2>Most frequently used words</h2>
          <canvas ref={canvas => this.wordCanvas=canvas} id="canvas"></canvas>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <Main />,
  document.getElementById('root')
);
