#!/usr/local/bin/node

const PAIR = 'btc_jpy';
const https = require('https');

const options = {
  protocol: 'https:',
  hostname: 'coincheck.com',
  path: '/api/rate/' + PAIR,
  method: 'GET'
};

const req = https.request(options, res => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    let response = JSON.parse(data);
    console.log('rate: %s', response.rate);
  });
});

req.on('error', e => {
  console.error(e);
});

req.end();
