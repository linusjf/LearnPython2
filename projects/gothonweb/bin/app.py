import web

urls = ('/', 'Index','/foo','Foo')


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

class Foo(object):
	def GET(self):
		greeting  = "Foo, World"
		return render.foo(greeting = greeting)

if __name__ == "__main__":
	app.run()
