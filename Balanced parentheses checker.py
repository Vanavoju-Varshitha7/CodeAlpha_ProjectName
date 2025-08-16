string1=input("enter your string:")
lst=[]
if(len(string1)%2==0):
    for i in range(0,int(len(string1)/2)):
        lst.append(string1[i])
    for i in range((len(lst)-1),-1,-1):
            for j in range(int(len(string1)/2),len(string1)):
              if(lst[i]=='{' and string1[j]=='}'):
                 lst.pop()    
                 break
              if(lst[i]=='[' and string1[j]==']'):
                    lst.pop()
                    break
              if(lst[i]=='(' and string1[j]==')'):
                  lst.pop()
                  break
    if(len(lst)==0):
            print("String is balanced.")     
    else:
            print("String is unbalanced")
            
else:
    print("The String is unbalanced")