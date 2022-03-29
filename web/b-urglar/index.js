const express = require('express');
const Mustache = require('mustache');
const fs = require('fs');
const cookieParser = require('cookie-parser')
const jwt = require('jsonwebtoken');

const config = require('./config.json')

const templates = {
    index: fs.readFileSync('./templates/index.mustache', { encoding: 'utf8' }),
    login: fs.readFileSync('./templates/login.mustache', { encoding: 'utf8' }),
    profileUser: fs.readFileSync('./templates/profile_user.mustache', { encoding: 'utf8' }),
    profileAdmin: fs.readFileSync('./templates/profile_admin.mustache', { encoding: 'utf8' }),
    profileError: fs.readFileSync('./templates/profile_error.mustache', { encoding: 'utf8' }),
}

function createId() {
    const chars = 'abcdefghijklmnopqrstuvwxyz';
    const length = 8;
    return [...new Array(length)].map(_ => chars[~~(chars.length * Math.random())]).join('');
}

function log(...msg) {
    const dt = new Date().toISOString()
    console.log(dt, ...msg);
}

const app = express();
app.use(express.static('static'));
app.use(cookieParser());
app.use(express.urlencoded({ extended: false }));

function getUser(req) {
    const authToken = req.cookies[config.cookieName];
    if (!authToken) return;

    try {
        const decoded = jwt.verify(authToken, config.jwtKey);
        const authUser = config.users.find((user) => decoded.userId === user.id )
        log(`[${decoded?.ctfId}]`, 'Authorized call', req.method, req.url)
        return authUser
    } catch (e) {
        log('Invalid auth token', authToken);
    }
}

function sendTemplate(res, status, template, params) {
    res.setHeader('content-type', 'text/html')
    res.status(status).send(Mustache.render(template, params))
}

app.get('/', (req, res) => {
    const user = getUser(req);

    if (!user) {
        log('Not logged in, redirecting to login page');
        res.redirect('/login');
        return;
    }
    sendTemplate(res, 200, templates.index, { user_name: user.name, user_id: user.id })
})

app.get('/profile', (req, res) => {
    const {userId} = req.query;
    if (!userId) {
        res.redirect('/');
        return;
    }

    const user = getUser(req);
    if (!user) {
        log('Not logged in, redirecting to login page');
        res.redirect('/login');
        return;
    }

    const profile = config.users.find((user) => user.id == userId);
    if (!profile) {
        sendTemplate(res, 404, templates.profileError, { user_name: user.name, user_id: user.id, message: 'Profile not found' })
        return;
    }

    if (profile.admin) {
        sendTemplate(res, 200, templates.profileAdmin, { user_name: user.name, user_id: user.id, profile_name: profile.name, api_key: config.secretApiKey })
        return;
    }
    sendTemplate(res, 200, templates.profileUser, { user_name: user.name, user_id: user.id, profile_name: profile.name })
})

app.get('/login', (req, res) => {
    sendTemplate(res, 200, templates.login, { message: 'Please log in' })
})

app.post('/login', (req, res) => {
    const {username, password} = req.body;
    if (username !== config.loginUser.username || password !== config.loginUser.password) {
        log('Wrong username/password', username, password);
        sendTemplate(res, 401, templates.login,  {message: 'Wrong username and/or password! Please try again.'})
        return
    }

    const payload = { userId: 5, ctfId: createId() }
    log('Logged in successfully', payload);
    const token = jwt.sign(payload, config.jwtKey);
    res.cookie(config.cookieName, token, { httpOnly: true, maxAge: 24 * 60 * 60 * 1000 }).redirect('/');
})

app.get('/secret', (req, res) => {
    const apiKey = req.headers.authorization
    res.setHeader('content-type', 'application/json');

    if (!apiKey) {
        log('call to /secret without key');
        res.status(401).send(JSON.stringify({ error: true, message: 'missing header: authorization'}))
        return
    }

    const parts = apiKey.split(/ /, 2);
    if (parts[0] === config.secretApiKey || parts[1] === config.secretApiKey) {
        const payload = {
            flag: config.flag
        }
        log('successful call to /secret!');
        res.status(200).send(JSON.stringify(payload));
        return;
    }
    log('call to /secret without the correct key');
    res.status(403).send(JSON.stringify({error: true, message: 'invalid api key'}));
})

app.get('/health', (req, res) => {
    res.status(200).send('OK')
})

const port = process.env.PORT || 3000;
app.listen(port);

console.log('Listening on port', port);
