const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.get(url + lang, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
