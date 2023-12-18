def kbc():
   print("welcome to kbc quize compitition :")

def que1():
   
   que1="who is prime minister in india :"
   ans="vijay rupani","amit shah","sardar patel","narendra modi"
   print(que1)
   print(ans)
   ans = input("enter your ans :")
   if ans == "narendra modi":
      print("right ans")
   else:
      print("wrong ans")

def que2():
   que2="what is your fav movie :"
   ans="sambhadur","dunkey","animal","sultan mirza"
   print(que2)
   print(ans)
   ans = input("enter your ans :")
   if ans == "sambhadur":
      print("right ans")
   else:
      print("wrong ans")

def que3():
   
   que3="what is your fav colour :"
   ans="green","red","yellow","pink"
   print(que3)
   print(ans)
   ans = input("enter your ans :")
   if ans == "yellow":
      print("right ans")
   else:
      print("wrong ans")

def que4():
   
   que4="what is your favourite food :"
   ans="pizza","pasta","dabeli","burgur"
   print(que1)
   print(ans)
   ans = input("enter your ans :")
   if ans == "burgur":
      print("right ans")
   else:
      print("wrong ans")

def que5():
   
   que5="what is your fav game :"
   ans="candycrush","candy crush soda","pubg","bubble shooter"
   print(que5)
   print(ans)
   ans = input("enter your ans :")
   if ans == "candycrush":
      print("right ans")
   else:
      print("wrong ans")

def que6():

   que6="which country would you like to visit :"
   ans="canada","australia","india","london"
   print(que6)
   print(ans)
   ans = input("enter your ans :")
   if ans == "london":
      print("right ans")
   else:
      print("wrong ans")

def que7():
   
   que7="what is most popular cricketer:"
   ans="virat kohl","ms dhoni","jadeja","gill"
   print(que7)
   print(ans)
   ans = input("enter your ans :")
   if ans == "virat kohli":
      print("right ans")
   else:
      print("wrong ans")

status=True
while status:
   kbc()
   choice=int(input("enter your choice :"))
   if choice==1:
      que1()
   elif choice==2:
      que2()
   elif choice==3:
      que3()
   elif choice==4:
      que4()
   elif choice==5:
      que5() 
   elif choice==6:
      que6()  
   elif choice==7:
      que7()  
  
      
   m_choice=input("do yo want to continue que press y for yes and press n for no :")
   if m_choice=='y'or m_choice=='Y':
      status = True
   else:
      status = False











      

    




 
    