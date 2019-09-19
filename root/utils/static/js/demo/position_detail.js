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

var time_string;

var chuheyihao_performance;
var lianghuayihao_performance;
var ctx_chuheyihao = document.getElementById("储贺1号");
var ctx_lianghuayihao = document.getElementById("储贺量化1号");

var ctx_chuheyihao_position_detail = document.getElementById("储贺1号持仓明细");
var ctx_lianghuayihao_position_detail = document.getElementById("储贺量化1号持仓明细");
var chuheyihao_position_detail_btn = document.getElementById('chuheyihao_position_detail_btn');
var lianghuayihao_position_detail_btn = document.getElementById('lianghuayihao_position_detail_btn');

var chart_chuheyihao;
var chart_lianghuayihao;

var chart_chuheyihao_position_detail;
var chart_lianghuayihao_position_detail;

function generate_position_detail(position_detail, ctx_position_detail, chart_product) {
    var strategies = ['大小盘(快)','大小盘(带量)','大小盘(集成)','大小盘(慢)','指数择时','指数择时(集成)','资金情绪(低波)'];
    var series_data = [];
    for(var s_index in strategies){
        var strategy = strategies[s_index]
        if(strategy in position_detail.series_dict){
            series_data.push({
                name: strategy,
                symbol: "none",
                type:'line',
                stack: '总量',
                areaStyle: {},
                data: position_detail.series_dict[strategy]
            })
        }
    }

    let positionDetailChart = echarts.init(ctx_position_detail);
    detail_option = {
        title: {
            text: "策略资金占用分布",
            left: "center"
        },
        tooltip: {
            triggerOn: "mousemove|click",
            borderColor: "#333",
            trigger: "axis",
            borderWidth: 0,
            backgroundColor: "rgba(50,50,50,0.7)",
            textStyle: {
                fontSize: 14
            },
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            },
            formatter: function(params) {
                let list = [];
                let listItem = '';
                for (var i in params) {
                    list.push(
                        '<i style="display: inline-block;width: 10px;height: 10px;background: '+params[i].color+';margin-right: 5px;border-radius: 50%;}"></i><span style="display:inline-block;">' +
                        params[i].seriesName +'</span>&nbsp&nbsp：' +params[i].value.toFixed(2)+'%')
                }
                listItem = list.join('<br>');
                return '<div class="showBox">' + listItem + '</div>'
            }
        },
        legend: {
            selectedMode: "multiple",
            top: "6.5%",
            show: true,
            orient: "horizontal",
            textStyle: {
                fontSize: 12
            },
            left: "center",
            padding: 10,
            y: 'bottom',
            data: strategies
        },
        grid:{
            left: '1.5%',
            right: '1.5%',
            bottom: '5%',
            containLabel: true
        },
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data : position_detail.dates
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel: { show: true, interval: 'auto', formatter: '{value}%' },
                min: 0,
                max: 100
            }
        ],
        series : series_data
    };
    positionDetailChart.setOption(detail_option, true);
    chart_product.setOption({series:[{name: '估测净值', data: position_detail.unit_values}], legend:{data: ['收盘净值', '估测净值']}});
    return positionDetailChart;
}

function generate_product_performance(product_performance, ctx) {
    let productChart = echarts.init(ctx);
    zip= rows=>rows[0].map((_,c)=>rows.map(row=>row[c]));
    unit_values = zip([product_performance.dates, product_performance.unit_values]);
    product_option = {
                        tooltip: {
                            triggerOn: "mousemove|click",
                            borderColor: "#333",
                            trigger: "axis",
                            borderWidth: 0,
                            backgroundColor: "rgba(50,50,50,0.7)",
                            textStyle: {
                                fontSize: 14
                            },
                            axisPointer: {
                                type: 'cross',
                                label: {
                                    backgroundColor: '#6a7985'
                                }
                            }
                        },
                        legend: {
                            selectedMode: "multiple",
                            top: "6.5%",
                            show: true,
                            orient: "horizontal",
                            textStyle: {
                                fontSize: 12
                            },
                            left: "center",
                            padding: 10,
                            y: 'bottom',
                            data: ['收盘净值']
                        },
                        grid:{
                            left: '1.5%',
                            right: '1.5%',
                            bottom: '5%',
                            containLabel: true
                        },
                        xAxis: {
                            type: 'time',
                            boundaryGap : false,
                            splitLine: {
                                show: false
                            }
                        },
                        yAxis: {
                            scale: true,
                            type: 'value',
                            boundaryGap: [0, '100%'],
                            splitLine: {
                                show: true
                            }
                        },
                        series: [{
                            name: '收盘净值',
                            type: 'line',
                            symbol: "none",
                            itemStyle: {
                                normal: {
                                    color: '#4e73df',
                                    label: {
                                      color:       '#4e73df',
                                      borderColor: '#4e73df',
                                    },
                                    lineStyle:{
                                      color:'#4e73df'
                                    }
                                }
                            },
                            data: unit_values
                        },{
                            name: '估测净值',
                            type: 'line',
                            symbol: "none",
                            itemStyle: {
                                normal: {
                                    color: '#ea6f5a',
                                    label: {
                                      color:       '#ea6f5a',
                                      borderColor: '#ea6f5a',
                                    },
                                    lineStyle:{
                                      color:'#ea6f5a'
                                    }
                                }
                            },
                            data: []
                        }]
                    };
    productChart.setOption(product_option, true);
    return productChart;
}


$.getJSON('/api/v1/performance/product/chuheyihao').done(function(res) {
    chuheyihao_performance = res.results;
    chart_chuheyihao = generate_product_performance(chuheyihao_performance, ctx_chuheyihao);
    window.addEventListener("resize", () => { chart_chuheyihao.resize();});
});


$.getJSON('/api/v1/performance/product/lianghuayihao').done(function(res) {
    lianghuayihao_performance = res.results;
    chart_lianghuayihao = generate_product_performance(lianghuayihao_performance, ctx_lianghuayihao);
    window.addEventListener("resize", () => { chart_lianghuayihao.resize();});
});


function load_search_value() {
    time_string = date_picker.datepicker("getDate").toISOString().substring(0, 10);

    if (moment(time_string).isValid()) {
        //alert(time_string);
        $.getJSON('/api/v1/performance/product/chuheyihao?start_date='+time_string).done(function(res) {
            chuheyihao_performance = res.results;
            chart_chuheyihao.dispose();
            chart_chuheyihao = generate_product_performance(chuheyihao_performance, ctx_chuheyihao);
            window.addEventListener("resize", () => { chart_chuheyihao.resize();});
        });

        $.getJSON('/api/v1/performance/product/lianghuayihao?start_date='+time_string).done(function(res) {
            lianghuayihao_performance = res.results;
            chart_lianghuayihao.dispose();
            chart_lianghuayihao = generate_product_performance(lianghuayihao_performance, ctx_lianghuayihao);
            window.addEventListener("resize", () => { chart_lianghuayihao.resize();});
        });

        if(document.getElementById("chuheyihao_position_detail_btn").style.display=="none"){
            $.getJSON('/api/v1/performance/product/chuheyihao/detail?start_date='+time_string).done(function(res) {
                chuheyihao_position_detail = res.results;
                chart_chuheyihao_position_detail.dispose();
                chart_chuheyihao_position_detail = generate_position_detail(chuheyihao_position_detail, ctx_chuheyihao_position_detail, chart_chuheyihao);
                window.addEventListener("resize", () => { chart_chuheyihao_position_detail.resize();});
            })
        }
        if(document.getElementById("lianghuayihao_position_detail_btn").style.display=="none"){
            $.getJSON('/api/v1/performance/product/lianghuayihao/detail?start_date='+time_string).done(function(res) {
                lianghuayihao_position_detail = res.results;
                chart_lianghuayihao_position_detail.dispose();
                chart_lianghuayihao_position_detail = generate_position_detail(lianghuayihao_position_detail, ctx_lianghuayihao_position_detail, chart_lianghuayihao);
                window.addEventListener("resize", () => { chart_lianghuayihao_position_detail.resize();});

            })
        }   
    }
}

search_btn.addEventListener('click', load_search_value);


function load_product_detail(product_name){
    let req_url = '/api/v1/performance/product/'+product_name+'/detail';
    if(typeof(time_string)!="undefined"){
        req_url += '?start_date='+time_string;
    }

    $.getJSON(req_url).done(function(res) {
        if(res.success_code==1){
            var chart_area = document.getElementById(product_name+"-detail");
            var target_btn = document.getElementById(product_name+"_position_detail_btn");

            // target_btn.innerText = "收起";
            target_btn.style.display="none"
            chart_area.style.display="block";

            if(product_name=="chuheyihao"){
              chuheyihao_position_detail = res.results;
              chart_chuheyihao_position_detail = generate_position_detail(chuheyihao_position_detail, ctx_chuheyihao_position_detail, chart_chuheyihao);
              window.addEventListener("resize", () => { chart_chuheyihao_position_detail.resize();});
            }else{
              lianghuayihao_position_detail = res.results;
              chart_lianghuayihao_position_detail = generate_position_detail(lianghuayihao_position_detail, ctx_lianghuayihao_position_detail, chart_lianghuayihao);
              window.addEventListener("resize", () => { chart_lianghuayihao_position_detail.resize();});
            }
        }else{
            $("#login_modal").modal("show");
        }
    })

}
chuheyihao_position_detail_btn.addEventListener('click', function(){ load_product_detail("chuheyihao") })
lianghuayihao_position_detail_btn.addEventListener('click', function(){ load_product_detail("lianghuayihao") })


// login
toastr.options = { // toastr配置
    "closeButton": false, //是否显示关闭按钮
    "debug": false, //是否使用debug模式
    "progressBar": true, //是否显示进度条，当为false时候不显示；当为true时候，显示进度条，当进度条缩短到0时候，消息通知弹窗消失
    "positionClass": "toast-top-center",//显示的动画时间
    "showDuration": "200", //显示的动画时间
    "hideDuration": "200", //消失的动画时间
    "timeOut": "600", //展现时间
    "extendedTimeOut": "600", //加长展示时间
    "showEasing": "swing", //显示时的动画缓冲方式
    "hideEasing": "linear", //消失时的动画缓冲方式
    "showMethod": "fadeIn", //显示时的动画方式
    "hideMethod": "fadeOut" //消失时的动画方式
}

var login_submit = document.getElementById('login_submit')
var login_username = document.getElementById('login_username')
var login_password = document.getElementById('login_password')

var login_success = document.getElementById('login_success')
var login_fail = document.getElementById('login_fail')


function login_post()
{
    $.post('/user/login', {"username": login_username.value, "password": login_password.value}, function(res){
        if(res.success_code!=0){
            toastr.success('登陆成功');
            $("#login_modal").modal('hide');
            chuheyihao_position_detail_btn.click();
            lianghuayihao_position_detail_btn.click()
        }else{
            toastr.warning('登陆失败');
        }
    })
};

login_submit.addEventListener('click', function(){login_post()});
