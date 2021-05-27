var city_label = [];
var city_data = [];
var city_colors = [];
$.each(json_city, function(i,v){
   city_label.push([i]);
   city_data.push([v,0,0]);
});
for(let i=0;i<this.city_label.length;i++){
  this.city_colors.push('#'+Math.floor(Math.random()*16777215).toString(16));
};

var region_label = [];
var region_data = [];
var region_colors = [];
$.each(json_region, function(i,v){
   region_label.push([i]);
   region_data.push([0,v,0]);
});
for(let i=0;i<this.region_label.length;i++){
  this.region_colors.push('#'+Math.floor(Math.random()*16777215).toString(16));
};

var country_label = [];
var country_data = [];
var country_colors = [];
$.each(json_country, function(i,v){
   country_label.push([i]);
   country_data.push([0,0,v]);
});
for(let i=0;i<this.country_label.length;i++){
  this.country_colors.push('#'+Math.floor(Math.random()*16777215).toString(16));
};

var ctx = document.getElementById("loc_bar").getContext('2d');
window.loc_bar = new Chart(ctx, {
   type: 'bar',
   data: {
      labels: ['City', 'Region','Country'], 
      datasets: [{}]
   },
   options: {
      responsive: false,
      legend: {
         position: 'right' 
      },
      scales: {
         xAxes: [{
            stacked: true 
         }],
         yAxes: [{
            stacked: true
         }]
      }
   }
});
for (var i = 0; i < city_label.length; i++){
   loc_bar.data.datasets.push({
      label: city_label[i],
      data: city_data[i],
      backgroundColor: city_colors[i]            
   });
}
for (var i = 0; i < region_label.length; i++){
   loc_bar.data.datasets.push({
      label: region_label[i],
      data: region_data[i],
      backgroundColor: region_colors[i]            
   });
}
for (var i = 0; i < country_label.length; i++){
   loc_bar.data.datasets.push({
      label: country_label[i],
      data: country_data[i],
      backgroundColor: country_colors[i]            
   });
}
window.loc_bar.update();