const mysql = require('mysql')

const DB = mysql.createConnection({
    host: 'localhost',
    user: 'user',
    password: 'password',
    database: 'rage_test'
})

DB.connect(function (err){
    if(err){
        console.error("--- Database connection error: " + err.stack)
        return;
    }
    console.log('+++ Successfully connected to database')
})

module.exports = DB