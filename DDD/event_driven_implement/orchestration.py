

class Customrer():
	def __init__(self, name, address, email):
		self.name = name
		self.address = address
		self.email = email


class CustomerService():

	def signup(self, customrer):
		# 계좌 개설
		BankService().create_account(customrer)

		# 환영 메일 발송
		MailService().send(customrer.email)

		# 가입 패키지 발송
		PostService().send(customrer.address)


class BankService():
	def create_account(self, customrer):
		print("Service Name: %s, Customrer Name: %s" %(self.__class__.__name__, customrer.name))


class MailService():
	def send(self, to):
		print("Service Name: %s, To: %s" % (self.__class__.__name__, to))


class PostService():
	def send(self, to):
		print("Service Name: %s, Address: %s" % (self.__class__.__name__, to))


if __name__ == '__main__':
	customer = Customrer(name='SELO', address='Seoul, Korea', email='rochan87@gmail.com')
	CustomerService().signup(customer)
