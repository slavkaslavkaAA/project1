def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% mink \n[b] Non-fat milk \n[c] Soy milk \n>')

  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
      print_message()
      return order_latte()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return 'Latte'
  else:
    return 'None'

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print(print_message()) 
    return 'None'

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  
  drink_type = get_drink_type()
  
  
  
  print("Alright, that\'s a {} {}!".format(size, drink_type))
  
  name = input('Can I get your name please? \n>')
  
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

coffee_bot()
