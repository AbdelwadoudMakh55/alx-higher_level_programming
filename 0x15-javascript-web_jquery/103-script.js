const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.get(url + lang, function (data) {
      $('#hello').html(data.hello);
    });
  });
  $('#language_code').focus(function () {
    $(document).on('keypress', function (e) {
      if (e.which === 13) {
        const lang = $('#language_code').val();
        $.get(url + lang, function (data) {
          $('#hello').html(data.hello);
        });
      }
    });
  });
});
