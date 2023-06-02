const div = $('DIV#toggle_header');
const header = $('header');

div.click(function () {
  header.toggleClass('red green');
});
