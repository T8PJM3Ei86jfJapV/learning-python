# -*- coding: utf-8 -*-

def log(cls):
	def wrapper(*args, **kwargs):
		print cls.__name__
		return cls(*args, **kwargs)
	return wrapper

@log
def foo():
	print 'Hello world!'

def main(argv=None):
	foo()

if __name__ == "__main__":
	main()