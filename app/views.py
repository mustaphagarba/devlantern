from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'Nickname': 'Miguel'}
	return '''
<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
	<h1> Hello and welcome to the DevLantern blog, ''' + user[Miguel] + '''</h1>
	</body>
</html>