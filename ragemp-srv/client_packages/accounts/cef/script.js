function showRegister() {
    resetError()
    document.getElementById('login').style.display = "none";
    document.getElementById('register').style.display = "block";
}

function showLogin() {
    resetError()

    document.getElementById('register').style.display = "none";
    document.getElementById('login').style.display = "block";
}

function loginAttempt() {
    const login = document.getElementById('log-login').value
    const password = document.getElementById('log-password').value

    resetError()

    if (!login || login.length < 3) {
        showError('Enter login.')
        return;
    }
    if (!password || password.length < 6) {
        showError('Enter password with minimum 6 symbols.')
        return;
    }

    mp.trigger('loginAttempt', JSON.stringify({login, password}))
}

function registerAttempt() {
    const login = document.getElementById('reg-login').value
    const password = document.getElementById('reg-password').value
    const passwordConfirm = document.getElementById('reg-password-confirm').value

    resetError()

    if (!login || login.length < 3) {
        showError('Enter login.')
        return;
    }
    if (!password || password.length < 6) {
        showError('Enter password with minimum 6 symbols.')
        return;
    }
    if (password !== passwordConfirm) {
        showError('Confirm your password.')
        return;
    }


    mp.trigger('registerAttempt', JSON.stringify({login, password}))
}

function showError(message) {
    const errorBlock = document.getElementById('error')
    errorBlock.innerText = message
    errorBlock.style.display = 'block';
}

function resetError() {
    const errorBlock = document.getElementById('error')
    errorBlock.innerText = ''
    errorBlock.style.display = 'none'
}
