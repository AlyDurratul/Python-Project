print("WELCOME TO SURVIVE GAME! \n ") 
name =input("What is your name? \n : ")
age = int(input("What is your age? \n : "))

health = 10

if age >= 18:
  print("You are old enough to play! ")
  
  wants_to_play = input("Do you want to play? Yes or No \n : ").lower()
  if wants_to_play == "yes":
    print("You are starting with", health, "health")
    print("Lets play! \n ")
    
    left_or_right = input("First choice....Left or Right(left/right)? \n : ")
    if left_or_right == "left":
      ans = input("Nice, you follow the path and reach a lake \n Do you swim across or go around (across/around)? \n : ")
      
      if ans == "around":
        print("You went around and reached the other side of the lake. \n ")
        
      elif ans == "across":
        print("You managed to get across, but were bit by a fish and lost 5 health. \n ")
        health -= 5
        
      ans = input("You notice a house and a river, Which do you go to(river/house)? \n : ")
      if ans == "house":
        print("You go to the house and are greted by the owner...He does not like you and you lose five health. \n ")
        health -= 5
        
        if health <= 0:
          print("You have 0 health and lost the game. ")
        else: 
          print("But,you survived and  win the game. ")
          
      else:
         print("You fell in the river and lost. ")
      
    else:
      print("you fell down and lost.....")
    
  else:
    print("Good bye")
    
else:
  print("You are not old enough to play...")
  
