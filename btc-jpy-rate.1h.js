#!/usr/local/bin/node

const PAIR = 'btc_jpy';
const AMOUNT = 1;
const https = require('https');

const getRate = (orderType) => {
  const options = {
    protocol: 'https:',
    hostname: 'coincheck.com',
    path: `/api/exchange/orders/rate?pair=${PAIR}&amount=${AMOUNT}&order_type=${orderType}`,
    method: 'GET'
  };

  const req = https.request(options, res => {
    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });

    res.on('end', () => {
      let response = JSON.parse(data);
      console.log('%s rate: %s', orderType, response.rate);
      console.log('price: %s', response.price);
      console.log('amount: %s', response.amount);
      console.log('---');
    });
  });

  req.on('error', e => {
    console.log(e);
  });

  req.end();
};

getRate('buy');
getRate('sell');
