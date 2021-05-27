TimeMe.initialize({
    currentPageName: "my-home-page", // current page
    idleTimeoutInSeconds: 5, // stop recording time due to inactivity
});


// user details function to extract data from the api
function User(json) {
    //  browser name
    var sys_data = detect.parse(navigator.userAgent);
    var browser = sys_data.browser.family;
    var os = sys_data.os.family;
    // detecting device
    if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
        device = "mobile";
      }else{
        device = "deskop";
    }
    
    const parameter = {
        "ip":json.ip,
        "city":json.city,
        "region": json.region,
        "country": json.country,
        "loc": json.loc,
        "org": json.org,
        "postal": json.postal,
        "timezone": json.timezone,
        "sitelink": window.location.href,
        "pagename": document.title,
        "referral": document.referrer,
        "browser": browser,
        "os": os,
        "date": new Date(),
        "device": device
    }
    console.log(parameter);
    // to load the  data to the api
    window.onload = function (event) {
        // alert('hi');
        //console.log(parameter);
        //console.log('onload event');
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("POST","http://127.0.0.1:8000/Web_Analytics/User_Details/", true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        // xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xmlhttp.onreadystatechange = function() {
        };
        xmlhttp.send(JSON.stringify(parameter));
        
        //console.log(document.getElementById('mydiv').innerHTML);
        
        //timer start
    TimeMe.trackTimeOnElement('area-of-interest-1');
    TimeMe.trackTimeOnElement('area-of-interest-2');
    setInterval(function () {
        let timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
        // console.log(timeSpentOnPage);
        // to load the data before the page closes
        window.onbeforeunload = function (event) {
            // var x = document.getElementById('confirm');
            // var show = x.getAttribute('data-confirm');
            xmlhttp=new XMLHttpRequest();
                xmlhttp.open("POST","http://127.0.0.1:8000/Web_Analytics/Time_Details/", true);
                xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                let timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
                let ip = json.ip;
                xmlhttp.send(JSON.stringify({ "time_diff": timeSpentOnPage, "ip": ip, "page":document.title }));
            }
    }, 37);
    };
}

// let data = sessionStorage.getItem('id');
// console.log(data);
// console.log('proces-1');
// console.log(document.getElementById('mydiv'));

// window.onload2 = function () {

//     //timer start
//     TimeMe.trackTimeOnElement('area-of-interest-1');
//     TimeMe.trackTimeOnElement('area-of-interest-2');
//     setInterval(function () {
//         let timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
//         //console.log(timeSpentOnPage);

//         window.onbeforeunload = function (event) {
//             xmlhttp=new XMLHttpRequest();
//             xmlhttp.open("POST","http://127.0.0.1:8000/Web_Analytics/Time_Details/", true);
//             xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//             let timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
//             xmlhttp.send(timeSpentOnPage);
//         };
//         // document.getElementById('timeInSeconds').textContent = timeSpentOnPage.toFixed(2);

//         // if (TimeMe.isUserCurrentlyOnPage && TimeMe.isUserCurrentlyIdle === false) {
//         //     document.getElementById('activityStatus').textContent = "You are actively using this page."
//         // } else {
//         //     document.getElementById('activityStatus').textContent = "You have left the page."
//         // }

//         // let timeSpentOnElement = TimeMe.getTimeOnElementInSeconds('area-of-interest-1');
//         // document.getElementById('area-of-interest-time-1').textContent = timeSpentOnElement.toFixed(2);

//         // let timeSpentOnElement2 = TimeMe.getTimeOnElementInSeconds('area-of-interest-2');
//         // document.getElementById('area-of-interest-time-2').textContent = timeSpentOnElement2.toFixed(2);

//     }, 37);
// }

function include(file) {
  
    var script  = document.createElement('script');
    script.src  = file;
    script.type = 'text/javascript';
    script.defer = true;
    document.getElementsByTagName('head').item(0).appendChild(script);   
  }
     
 
  /* Include Many js files */
  include('http://ipinfo.io/?format=jsonp&callback=User'); // External User data api
//   include('https://cdnjs.cloudflare.com/ajax/libs/Detect.js/2.2.2/detect.min.js'); 
  
