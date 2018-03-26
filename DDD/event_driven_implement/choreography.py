

class Customrer():
	def __init__(self, name, address, email):
		self.name = name
		self.address = address
		self.email = email

EventBook = {
	# example
	'main_event': {
		'events': ['dependent_event', ],
	}
}


def register_event(pub_event_name, sub_event):
	try:
		pub_event = EventBook[pub_event]
		pub_event.append(sub_event)
	except KeyError:
		EventBook[pub_event] = [sub_event]


def pub(event_name):
	def add(func):
		def __wrapper(*args, **kwargs):
			_r = func(*args, **kwargs)
			sub_events = EventBook[event_name]
			for sub_event in sub_events:
				sub_event(*args, **kwargs)
			return _r
		
		if event_name not in EventBook:
			EventBook[event_name] = []

		return __wrapper
	return add


def sub(event_name):
	def register(func):
		def __wrapper(*args, **kwargs):
			return func(*args, **kwargs)

		if event_name not in EventBook:
			EventBook[event_name] = []

		EventBook[event_name].append(__wrapper)
		return __wrapper
	return register


SIGNUP = 'signup'
UPDATE = 'update'


class CustomerService:
	@pub(SIGNUP)
	def signup(self, customrer):
		print("SignUp\n")

	@pub(UPDATE)
	def update(self, customrer):
		print("Update\n")


class BankService:
	@sub(SIGNUP)
	def create_account(self, customrer):
		print("Service Name: %s, Customrer Name: %s" %(self.__class__.__name__, customrer.name))


class MailService:
	@sub(SIGNUP)
	@sub(UPDATE)
	def send(self, customrer):
		print("Service Name: %s, To: %s" % (self.__class__.__name__, customrer.email))


class PostService:
	@sub(SIGNUP)
	def send(self, customrer):
		print("Service Name: %s, Address: %s" % (self.__class__.__name__, customrer.address))



if __name__ == '__main__':
	customer = Customrer(name='SELO', address='Seoul, Korea', email='rochan87@gmail.com')
	CustomerService().signup(customer)
	CustomerService().update(customer)
