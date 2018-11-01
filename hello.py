def app(environ, start_response):
	#buisness logic
	
	status = "200 OK"	
	headers = [
		('Content-Type', 'text/plain')
	]
	#body = 'Hello'
	#body = [environ['QUERY_STRING'].replace('&', '\n')]
	body = [bytes(i + '\n','ascii') for i in environ['QUERY_STRING'].split('&')]
	start_response(status, headers)
	return body
