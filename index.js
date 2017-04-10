var express = require('express');
var sqlite3 = require('sqlite3');
var db      = new sqlite3.Database('bits/ASKDONALD.db');
var Promise = require('bluebird');

var app = express();
var port = 8080;

app.use(express.static('docs'));

app.get('/', function(req, res, next) {
  res.sendFile('index.html', { root: __dirname + '/docs/'});
});

app.get('/tweets', function(req, res, next) {
  db.all('SELECT * FROM TWEETS LIMIT 10', function(error, rows) {
    res.send(rows);
  });
});

app.listen(port);
console.log('Server running on 127.0.0.1:8080');

