// Set calendar for change date
var date_picker = $('#datepicker');
date_picker.datepicker({
    weekStart: 1,
    daysOfWeekHighlighted: "6,0",
    autoclose: true,
    todayHighlight: true,
});
date_picker.datepicker("setDate", moment().add(-365, 'day')._d);
var search_btn = document.getElementById('search_button');


// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var chuheyihao_performance;
var lianghuayihao_performance;
var ctx_chuheyihao = document.getElementById("储贺1号");
var ctx_lianghuayihao = document.getElementById("储贺量化1号");

var chart_chuheyihao;
var chart_lianghuayihao;


function generate_product_performance(product_performance, ctx) {
  let productChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: product_performance.dates,
      datasets: [{
        label: "收盘净值",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 2,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: product_performance.unit_values,
      }],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 25,
          top: 25,
          bottom: 0
        }
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
  return productChart;
}


$.getJSON('/api/v1/performance/product/chuheyihao').done(function(res) {
  chuheyihao_performance = res.results;
  chart_chuheyihao = generate_product_performance(chuheyihao_performance, ctx_chuheyihao);
});


$.getJSON('/api/v1/performance/product/lianghuayihao').done(function(res) {
  lianghuayihao_performance = res.results;
  chart_lianghuayihao = generate_product_performance(lianghuayihao_performance, ctx_lianghuayihao);
});


function load_search_value() {
    let time_string = date_picker.datepicker("getDate").toISOString().substring(0, 10);

    if (moment(time_string).isValid()) {
        //alert(time_string);

        $.getJSON('/api/v1/performance/product/chuheyihao?start_date='+time_string).done(function(res) {
            chuheyihao_performance = res.results;
            chart_chuheyihao.destroy();
            chart_chuheyihao = generate_product_performance(chuheyihao_performance, ctx_chuheyihao);
        });

        $.getJSON('/api/v1/performance/product/lianghuayihao?start_date='+time_string).done(function(res) {
            lianghuayihao_performance = res.results;
            chart_lianghuayihao.destroy();
            chart_lianghuayihao = generate_product_performance(lianghuayihao_performance, ctx_lianghuayihao);
        });
    }
}

search_btn.addEventListener('click', load_search_value);

