// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function generate_daxiaopan_performance(dxp_data, ctx_performance, ctx_drawdown, ctx_correctness) {
  let performanceChart = new Chart(ctx_performance, {
    type: 'line',
    data: {
      labels: dxp_data.dates,
      datasets: [{
        label: "策略净值",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 1,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 1,
        data: dxp_data.strategy_values,
      }],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 25,
          top: 5,
          bottom: 5
        }
      },
      title: {
        display: true,
        text: "策略净值"
      },
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false,
            maxTicksLimit: 10
          }
        }],
        yAxes: [{
          ticks: {
            min: 0.5,
            stepSize: 0.5,
            precision: 1,
            // Include a dollar sign in the ticks
            callback: function (value, index, values) {
              return value;
            }
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          }
        }],
      },
      legend: {
        display: false
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        titleMarginBottom: 10,
        titleFontColor: '#6e707e',
        titleFontSize: 14,
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        intersect: false,
        mode: 'index',
        caretPadding: 10,
        callbacks: {
          label: function (tooltipItem, chart) {
            var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
            console.log(tooltipItem.yLabel);
            return datasetLabel + ': ' + tooltipItem.yLabel;
          }
        }
      }
    }
  });
  let drawdownChart = new Chart(ctx_drawdown, {
    type: 'line',
    data: {
      labels: dxp_data.dates,
      datasets: [{
        label: "最大回撤",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 0,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: dxp_data.trailing_drawdowns,
      }],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 25,
          top: 5,
          bottom: 5
        }
      },
      title: {
        display: true,
        text: "最大回撤"
      },
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false,
            maxTicksLimit: 10
          }
        }],
        yAxes: [{
          ticks: {
            fixedStepSize: 0.05,
            maxTicksLimit: 5,
            padding: 10,
            // Include a dollar sign in the ticks
            callback: function (value, index, values) {
              return value;
            }
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          }
        }],
      },
      legend: {
        display: false
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        titleMarginBottom: 10,
        titleFontColor: '#6e707e',
        titleFontSize: 14,
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        intersect: false,
        mode: 'index',
        caretPadding: 10,
        callbacks: {
          label: function (tooltipItem, chart) {
            var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
            console.log(tooltipItem.yLabel);
            return datasetLabel + ': ' + tooltipItem.yLabel;
          }
        }
      }
    }
  });
  let correctnessChart = new Chart(ctx_correctness, {
    type: 'line',
    data: {
      labels: dxp_data.dates,
      datasets: [{
        label: "滚动正确率",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 0,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: dxp_data.rolling_accuracies,
      }],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 25,
          top: 5,
          bottom: 5
        }
      },
      title: {
        display: true,
        text: "滚动正确率"
      },
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: true,
            maxTicksLimit: 11
          }
        }],
        yAxes: [{
          ticks: {
            min: 0.2,
            max: 0.8,
            // Include a dollar sign in the ticks
            //callback: function (value, index, values) {
            //  return value;
            //}
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          }
        }],
      },
      legend: {
        display: false
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        titleMarginBottom: 10,
        titleFontColor: '#6e707e',
        titleFontSize: 14,
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        intersect: false,
        mode: 'index',
        caretPadding: 10,
        callbacks: {
          label: function (tooltipItem, chart) {
            var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
            console.log(tooltipItem.yLabel);
            return datasetLabel + ': ' + tooltipItem.yLabel;
          }
        }
      }
    }
  });
  let charts = [performanceChart, drawdownChart, correctnessChart]
  return charts;
}


$.getJSON('/api/v1/strategy/dxp/fast').done(function(res) {
  let dxp_performance_data = res.results;
  console.log(dxp_performance_data);
  var ctx_performance_dxp_kuai = document.getElementById("大小盘-复合-净值");
  var ctx_drawdown_dxp_kuai = document.getElementById("大小盘-复合-回撤");
  var ctx_correctness_dxp_kuai = document.getElementById("大小盘-复合-正确率");
  var charts_dxp_kuai = generate_daxiaopan_performance(dxp_performance_data, ctx_performance_dxp_kuai,
                                                       ctx_drawdown_dxp_kuai, ctx_correctness_dxp_kuai);
});


