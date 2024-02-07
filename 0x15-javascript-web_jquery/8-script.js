const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const result = data.results;
  result.forEach(element => {
    $('#list_movies').append('<li>' + element.title + '</li>');
  });
});
