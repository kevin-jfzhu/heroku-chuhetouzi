// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var charts_bs_fast;
var charts_bs_vol;
var charts_bs_ensemble;
var charts_bs_slow;
var charts_it_general;
var charts_it_ensemble;
var charts_fs_high;
var charts_fs_mid;
var charts_fs_low;
var charts_pp_svm;


var ctx_performance_bs_fast = document.getElementById("大小盘-快-净值");
var ctx_drawdown_bs_fast = document.getElementById("大小盘-快-回撤");
var ctx_correctness_bs_fast = document.getElementById("大小盘-快-正确率");

var ctx_performance_bs_vol = document.getElementById("大小盘-快带量-净值");
  var ctx_drawdown_bs_vol = document.getElementById("大小盘-快带量-回撤");
  var ctx_correctness_bs_vol = document.getElementById("大小盘-快带量-正确率");

  var ctx_performance_bs_ensemble = document.getElementById("大小盘-快集成-净值");
  var ctx_drawdown_bs_ensemble = document.getElementById("大小盘-快集成-回撤");
  var ctx_correctness_bs_ensemble = document.getElementById("大小盘-快集成-正确率");



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
            min: 0.0,
            max: 1.0,
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


$.getJSON('/api/v1/strategy/bigsmall_fast').done(function(res) {
  let performance_data = res.results;
  charts_bs_fast = generate_daxiaopan_performance(performance_data, ctx_performance_bs_fast,
                                                       ctx_drawdown_bs_fast, ctx_correctness_bs_fast);
});

$.getJSON('/api/v1/strategy/bigsmall_vol').done(function(res) {
  let performance_data = res.results;
  charts_bs_vol = generate_daxiaopan_performance(performance_data, ctx_performance_bs_vol,
                                                     ctx_drawdown_bs_vol, ctx_correctness_bs_vol);
});

$.getJSON('/api/v1/strategy/bigsmall_ensemble').done(function(res) {
  let performance_data = res.results;

  charts_bs_ensemble = generate_daxiaopan_performance(performance_data, ctx_performance_bs_ensemble,
                                                          ctx_drawdown_bs_ensemble, ctx_correctness_bs_ensemble);
});

$.getJSON('/api/v1/strategy/bigsmall_slow').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_bs_slow = document.getElementById("大小盘-慢-净值");
  var ctx_drawdown_bs_slow = document.getElementById("大小盘-慢-回撤");
  var ctx_correctness_bs_slow = document.getElementById("大小盘-慢-正确率");
  charts_bs_slow = generate_daxiaopan_performance(performance_data, ctx_performance_bs_slow,
                                                      ctx_drawdown_bs_slow, ctx_correctness_bs_slow);
});

$.getJSON('/api/v1/strategy/index-timing_general').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_it_general = document.getElementById("指数择时-净值");
  var ctx_drawdown_it_general = document.getElementById("指数择时-回撤");
  var ctx_correctness_it_general = document.getElementById("指数择时-正确率");
  charts_it_general = generate_daxiaopan_performance(performance_data, ctx_performance_it_general,
                                                         ctx_drawdown_it_general, ctx_correctness_it_general);
});

$.getJSON('/api/v1/strategy/index-timing_ensemble').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_it_ensemble = document.getElementById("指数择时-集成-净值");
  var ctx_drawdown_it_ensemble = document.getElementById("指数择时-集成-回撤");
  var ctx_correctness_it_ensemble = document.getElementById("指数择时-集成-正确率");
  charts_it_ensemble = generate_daxiaopan_performance(performance_data, ctx_performance_it_ensemble,
                                                         ctx_drawdown_it_ensemble, ctx_correctness_it_ensemble);
});


$.getJSON('/api/v1/strategy/flow-sentim_high').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_fs_high = document.getElementById("资金情绪-高波-净值");
  var ctx_drawdown_fs_high = document.getElementById("资金情绪-高波-回撤");
  var ctx_correctness_fs_high = document.getElementById("资金情绪-高波-正确率");
  charts_fs_high = generate_daxiaopan_performance(performance_data, ctx_performance_fs_high,
                                                     ctx_drawdown_fs_high, ctx_correctness_fs_high);
});

$.getJSON('/api/v1/strategy/flow-sentim_mid').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_fs_mid = document.getElementById("资金情绪-中波-净值");
  var ctx_drawdown_fs_mid = document.getElementById("资金情绪-中波-回撤");
  var ctx_correctness_fs_mid = document.getElementById("资金情绪-中波-正确率");
  charts_fs_mid = generate_daxiaopan_performance(performance_data, ctx_performance_fs_mid,
                                                     ctx_drawdown_fs_mid, ctx_correctness_fs_mid);
});

$.getJSON('/api/v1/strategy/flow-sentim_low').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_fs_low = document.getElementById("资金情绪-低波-净值");
  var ctx_drawdown_fs_low = document.getElementById("资金情绪-低波-回撤");
  var ctx_correctness_fs_low = document.getElementById("资金情绪-低波-正确率");
  charts_fs_low = generate_daxiaopan_performance(performance_data, ctx_performance_fs_low,
                                                     ctx_drawdown_fs_low, ctx_correctness_fs_low);
});

$.getJSON('/api/v1/strategy/pos-price_svm').done(function(res) {
  let performance_data = res.results;
  var ctx_performance_pp_svm = document.getElementById("SVM量价-净值");
  var ctx_drawdown_pp_svm = document.getElementById("SVM量价-回撤");
  var ctx_correctness_pp_svm = document.getElementById("SVM量价-正确率");
  charts_pp_svm = generate_daxiaopan_performance(performance_data, ctx_performance_pp_svm,
                                                     ctx_drawdown_pp_svm, ctx_correctness_pp_svm);
});


var search_box = document.getElementById('search_box');
var search_btn = document.getElementById('search_button');

function load_search_value() {
    let time_string = search_box.value;

    if (time_string !== '') {
        if (moment(time_string).isValid()) {
            //alert(time_string);

            $.getJSON('/api/v1/strategy/bigsmall_fast').done(function(res) {
                let performance_data = res.results;
                console.log(charts_bs_fast);
                charts_bs_fast[0].destroy();
                charts_bs_fast[1].destroy();
                charts_bs_fast[2].destroy();
                charts_bs_fast = generate_daxiaopan_performance(performance_data, ctx_performance_bs_fast,
                                                       ctx_drawdown_bs_fast, ctx_correctness_bs_fast);
});


        } else {
            alert('您输入的起始日期有误，请重新输入')
        }
    }
}

search_btn.addEventListener('click', load_search_value);
