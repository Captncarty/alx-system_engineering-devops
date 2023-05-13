//Simple Express.js RESTful API
'use strict';

//initialize
const
    port = 8888,
    express = require('express'),
    app = express();

// /hello/ Get Request
app.get('/hello/read/:name?', (req, res) => 
    res
        .append('Access-Control-Allow-Origin', '*')     //OPtional to allow access for fetch when hosting on a domain* or specific domian
        .json(
            {message: `Hello ${req.params.name || 'world'}!`} 
        )
);

// start server
app.listen(port, () => 
    console.log(`Server started on Port ${port}`)
);