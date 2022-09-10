rint("Welcom to calculator app")


first_input = int(input("Enter first number: "))
symbols = input("choose a symbol + - / *: ")
second_input = int(input("Enter second number: "))


if symbols == "+" :
  ans = int(first_input+second_input)
  print(f"{first_input}+{second_input} = {ans}")

  
elif symbols == "/" :
  ans = first_input/second_input
  print(f"{first_input}/{second_input} = {ans}")

  
if symbols == "*" :
  ans = first_input*second_input
  print(f"{first_input}*{second_input} = {ans}")

  
elif symbols == "-" :
  ans = first_input-second_input
  print(f"{first_input}-{second_input} = {ans}")