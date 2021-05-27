// var min = min_time;
// var max = max_time;
var label = [];
var data = [];
$.each(json_time_data, function(i,v){
    label.push(i);
    data.push(v);
  });
var ctx = document.getElementById('time_diff_chart').getContext('2d');
var time_diff_chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: [],
            data: data,
            // backgroundColor: ['#009dbe','#f0a566'],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1,
            // borderWidth: 1
        }]
    },
    options: {
      responsive: false,
      title: {
        display: true,
        text: 'Time Spent On Website'
    }
    },
    legend: {
        display: false
    },
    tooltip: {
        enabled: false
    },
});