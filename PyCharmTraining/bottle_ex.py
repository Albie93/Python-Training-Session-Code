import bottle

app = bottle.Bottle()

@app.route('/')
def homepage():
    return 'WelcomePage'

@app.route('/Hello')
def helloPage():
    return 'hello page'

@app.route('/xyz/<name>')
def msg(name):
    return "Hello " + name

@app.route('/login')
def loginpage():
    return '''<form action='/login1' method='post'>
                user: <input type = text name = uname />
                      <input type = submit value = submit>'''

@app.post('/login1')
def login1page():
    r = bottle.request.forms.get('uname')
    return 'User = ' + r

@app.route('/QueryDB')
def queryDB():
    import sqlite3
    con = sqlite3.connect('my_DB')
    cur=con.cursor()
    cur.execute('select * from log_data')
    r = cur.fetchall()
    return str(r)

app.run(host='127.0.0.1',port='8000')

