$(function() {
   $('#menu-button').on('click', function() {
      $('#main-nav').toggle();
   });

   reverseNav();

   $(window).resize(reverseNav);
});

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
