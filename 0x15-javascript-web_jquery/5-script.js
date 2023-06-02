const div = $('DIV#add_item');
const list = $('UL.my_list');

div.click(function () {
  list.append('<li>Item</li>');
});
