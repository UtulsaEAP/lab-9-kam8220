def feet_to_steps(user_feet):
   #write your code here
   return int(user_feet/2.5)

if __name__ == '__main__':
    user_feet=float(input())
    print(feet_to_steps(user_feet))
    #take input feet steps here
    #store it into the function
    
    #print your steps here
    feet_to_steps(5280)