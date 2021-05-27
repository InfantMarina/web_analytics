// for dynamically adding labels to the bar chart
var label = [];
var data = [];
$.each(json_os, function(i,v){
  label.push(i);
  data.push(v);
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
var ctx = document.getElementById('os_pie').getContext('2d');
var os_pie = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: label,
        datasets: [{
            label: 'OS',
            data: data,
            backgroundColor: colors,
            // borderWidth: 1
        }]
    },
    options: {
      responsive: false,
      title: {
        display: true,
        text: 'Users OS'
    }
      // cutoutPercentage: 80
    }
});
