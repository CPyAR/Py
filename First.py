

# Input data validation AR
y =input ('input your name:' ) # data type str
#count method returns the number of times a value appears in a string
if  ( y.count("0")!=0 or y.count("1")!=0 or y.count("2")!=0 or y.count("3")!=0 or y.count("4")!=0 or y.count("5")!=0 or y.count("6")!=0 or y.count("7")!=0 or y.count("8")!=0 or y.count("9")!=0 ):
  print ("invalid data" )
# isalnum method verifies if all values in a string is alfanumeric
elif y.isalnum()== False: 
   print ("invalid data" )
else:
  print ("Hello" , y )
