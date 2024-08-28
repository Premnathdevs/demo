def palindrom(str):
    for i in range(0,len(str)//2):
        if str[i] != str[len(str)-i-1]:
         return False
    return True
    
st="radar"
if (palindrom(st)):
       print("it is palindrom")
else:
    print("it is not palindrom" )
      
