let DB = require('../core/database')

mp.events.add('onLoginAttempt', (player, data) => {
    data = JSON.parse(data);
    DB.query('SELECT * FROM accounts WHERE login = ? LIMIT 1', [data.login], function (err, results) {
        if (results.length === 0) return player.call('showAuthError', ['Bad login.']);
        const dbPassword = results[0].password;
        if (data.password === dbPassword) return player.call('hideLoginDialog');

        player.call('showAuthError', ['Bad login.'])
    })
})

mp.events.add('onRegisterAttempt', (player, data) => {
    data = JSON.parse(data);

    DB.query('SELECT id FROM accounts WHERE login = ?', [data.login], function (err, results) {
        if (results.length > 0) return player.call('showAuthError', ['Account already exists']);

        DB.query("INSERT INTO accounts SET login = ?, password = ?", [data.login, data.password], function (err, results) {
            player.call('hideLoginDialog')
        })
    })
})

