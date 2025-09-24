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

  def __second_menu(self): 

    second_input = input("""
    What would you like to do next?
    1. NER
    2. Sentiment Analysis
    3.Language Detection
    4.Exit""")

    if second_input == '1':
      self.__ner()
    elif second_input == '2':
      self.__sentiment_analysis()
    elif second_input == '3':
      self.__language_detection()
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
    email = input('Enter your Email')
    password = input('Enter your Password')

    if email in self.__database:
      if self.__database[email][1] == password:
        print(f'Welcome {self.__database[email][0]}')
        self.__second_menu()
      else:
        print('Invalid Credentials, Please try again')
        self.__login()  
        # Proceed to NLP functionalities (not implemented here)
    else:
        print('Invalid Credentials, Please try again')
        self.__initial_menu()


obj = NLPApp()  

   