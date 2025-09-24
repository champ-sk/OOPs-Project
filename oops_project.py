class NLPApp:
  def __init__(self) :
    self.__database = {}
    self.__initial_menu()

  def __initial_menu(self):
    first_input = input("""
    Hi! How would you like to proceed?
    1. Not a member? Register
    2. Already a member? Login
    3. Galti s aa gya? Exit.
    """)

    if first_input =='1':
      self.__register()
    elif first_input == '2':
      self.__login()
    else:
      exit()

  def __register(self):
    name = input('Enter your Name')
    email = input('Enter your Email')
    password = input('Enter your Password')

    if email in self.__database:
      print('Email already exists')
    else:
      self.__database[email] = [name, password]
      print('Registration Successful, Now you can Login')
      print(self.__database)
      self.__login()

  def __login(self):
    print('login')   

obj = NLPApp()  

   