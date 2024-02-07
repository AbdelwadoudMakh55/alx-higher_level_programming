const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data) {
    $('#hello').html(data.hello);
  });
});
