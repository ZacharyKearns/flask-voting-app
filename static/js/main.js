$(function() {
   $('#menu-button').on('click', function() {
      $('#main-nav').toggle();
   });

   reverseNav();

   $(window).resize(reverseNav);

   $('#twitter').attr(
      'href',
      'https://twitter.com/home?status=Vote%20on%20this%20awesome%20poll!%20' +
      window.location.href +
      '%20%23freeCodeCamp'
   );

   var labels = [];
   var data = [];
   var backgroundColors = [];
   var borderColors = [];

   $(".option").each(function() {
      var color = randomColor();
      labels.push($(this).text());
      backgroundColors.push(color.background);
      borderColors.push(color.border);
   });

   $(".votes").each(function() {
      data.push(parseInt($(this).text()));
   });

   var ctx = $("#chart");
   var chart = new Chart(ctx, {
      type: 'bar',
      data: {
         labels: labels,
         datasets: [{
            label: '# of Votes',
            data: data,
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            borderWidth: 1
         }]
      }, // End of data
      options: {
         scales: {
            yAxes: [{
               ticks: {
                  beginAtZero:true
               }
            }] // End of yAxes
         } // End of scales
      } // End of options
   }); // End of Bar Chart
}); // End of Document Ready

function reverseNav() {
   if ($('#menu-button').css('display') == 'block' &&
       $('.list-group li:first-child a').text() !== 'Home' ||
       $('#menu-button').css('display') == 'none' &&
       $('.list-group li:first-child a').text() == 'Home') {
      var list = $('.list-group');
      var listItems = list.children('li');
      list.append(listItems.get().reverse());
   }
}

function randomInt() {
   return Math.floor(Math.random() * 156) + 100;
}

function randomColor() {
   var r = randomInt();
   var g = randomInt();
   var b = randomInt();
   var darkR = r - 100;
   var darkG = g - 100;
   var darkB = b - 100;
   var backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
   var borderColor = 'rgb(' + darkR + ',' + darkG + ',' + darkB + ')';
   return { 'background': backgroundColor, 'border': borderColor };
}
