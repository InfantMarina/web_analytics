// for dynamically adding labels to the bar chart
var label = [];
var data = [];
$.each(json_page_name, function(i,v){
  label.push(i);
  data.push(v);
// console.log(i,v);
});

// for dynamically adding colors to pie chart
var colors = ['#009dbe','#005f82','#00b3d0','#004c6d','#0088ab','#00c9e1','#00e0f1','#00f7ff','#007397'];
// var color_picker = [];
// var colors = ['#00876c','#6aaa96','#aecdc2','#f1f1f1','#f0b8b8','#e67f83','#d43d51'];
// for(let i=0;i<this.label.length;i++){
  // this.color_picker.push(colors[Math.floor(Math.random() * colors.length)]);
// }
// console.log(color_picker)
// console.log(colors);
// this.colors.push('#'+Math.floor(Math.random()*16777215).toString(16));
var ctx = document.getElementById('user_line_chart').getContext('2d');
var user_line_chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: 'Each Page Count',
            data: data,
            // backgroundColor: colors,
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
        text: 'Page Visited By Users'
    }
      // cutoutPercentage: 80
    }
});

// var ctx = document.getElementById("mypiechart");
// var mypiechart = new Chart(ctx, {
//   type: 'pie',
//   data: {
//     labels: [
//       'Red',
//       'Blue',
//       'Yellow'
//     ],
//     datasets: [{
//       label: 'My First Dataset',
//       data: [300, 50, 100],
//       backgroundColor: [
//         'rgb(255, 99, 132)',
//         'rgb(54, 162, 235)',
//         'rgb(255, 205, 86)'
//       ],
//       hoverOffset: 4
//     }]
//   },
//   options: {
//     // maintainAspectRatio: false,
//     tooltips: {
//     //   backgroundColor: "rgb(255,255,255)", 
//     //   bodyFontColor: "#858796",
//     //   borderColor: '#dddfeb',
//     //   borderWidth: 1,
//     //   xPadding: 5,
//     //   yPadding: 5,
//     //   displayColors: false,
//     //   caretPadding: 50,
//         responsive: true,
//         maintainAspectRatio: false,
//     },
//     legend: {
//       display: false
//     },
//     cutoutPercentage: 70,
//   },
// });