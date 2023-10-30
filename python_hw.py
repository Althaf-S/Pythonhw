#first python program
def fizzbizz(n):
  for i in range (1,n+1):
    if i % 15 == 0:
      print("fizzbizz")
    elif i % 5 == 0:
      print("bizz")
    elif i % 3 == 0 :
      print("fizz")
    else :
      print(i)

#n = int(input("Enter any number to do operations : "))
#fizzbizz(n)


#program to find whether provided string is palindrome
def palindrome(s):
  w= ''
  for i in s:
    w = i + w
  if w == s:
    print("The string you provided is palindrome")
  else :
    print("The string you provided is not palindrome")
    
#s = input("Enter your string to check if it is palindrome: ")
#palindrome(s)



#program to find whether provided string is pangaram
def pangram(s):

  w = ''
  c = 0

  for i in s:
    if i != ' ':
      w = w+i
  w = w.lower()
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  for i in alphabets: 
    if i in w:
      c += 1
  if c == len(alphabets):
    print("Is pangarm")
  else :
    print("Not pangarm")
    
#s = input("Enter your string here : ")     
#pangram(s)


