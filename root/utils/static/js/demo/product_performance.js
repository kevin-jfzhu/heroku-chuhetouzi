// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function generate_product_performance(dates, unit_values, ctx) {
  let productChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
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
        data: unit_values,
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
  let dates = res.dates;
  let unit_values = res.unit_values;
  var ctx_p1 = document.getElementById("储贺1号");
  var productChart = generate_product_performance(dates, unit_values, ctx_p1);
});


$.getJSON('/api/v1/performance/product/lianghuayihao').done(function(res) {
  let dates = res.dates;
  let unit_values = res.unit_values;
  var ctx_p2 = document.getElementById("储贺量化1号");
  var productChart = generate_product_performance(dates, unit_values, ctx_p2);
});



$(window).ready(function(){
  console.log('Page is ready');
  let btn = document.getElementById('confirm_search_button');
  btn.addEventListener('click', function () {
    let value_in_search_box = document.getElementById('search_date').value;
    console.log(value_in_search_box);
    console.log(Date.parse(value_in_search_box));
  })
});
