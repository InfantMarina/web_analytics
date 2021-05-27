var data = unique_visitors;
data_index = parseInt(data[0]);
// for calculating percentage for data
var i,len;
var data_count = 0;
// if data is greater than 99
if (data.length > 2){
    for (i = 0; len = data.length, i < len; i++) {
        // console.log(data[i]);
        data_count += parseInt(data[i]);
    }
    // if data is of format N00
    if (data_index == data_count){
        var denominator = parseInt(data_index + '00');
        // console.log(denominator);
        percent_data = (data * 100)/denominator;
    }else{
        var denominator = parseInt((data_index+1) + '00');
        console.log(denominator);
        percent_data = (data * 100)/denominator;
    }
}else{
    percent_data = (data * 100)/100;
}
var remaining_data = 100 - percent_data;
var ctx = document.getElementById('unique_doughnut').getContext('2d');
var unique_doughnut = new Chart(ctx, {
    type: 'doughnut',
    data: {
        datasets: [{
            label: ['a','b'],
            data: [percent_data,remaining_data],
            backgroundColor: ['#004C97'],
            // borderColor: colors,
            borderWidth: 1
        }]
    },
    options: {
      responsive: false,
      cutoutPercentage: 80,
    },
    legend: {
        display: false
    },
    tooltip: {
        enabled: false
    },
});