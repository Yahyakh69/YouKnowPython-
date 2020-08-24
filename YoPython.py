

# finds the length of the longest substring without repeating characters.
x=input("enter what you want")
x=x.replace(" ", "") #lets remove the white space :)
y=dict()
m=list(x)
z=set(x)
#dictionary case
for i in range(len(m)) : 
  if m[i] in y.keys() :
    y[m[i]] += 1 
  else :
    y[m[i]] = 1 
print(f"the length of the longest substring without repeating characters is {len(y)}")

# set case same result only much easier 
print(f"the length of the longest substring without repeating characters is {len(z)}")

# get the most common word or letter in a string 
numbers=[]
max_=[]
for j,z in y.items() : 
   numbers.append(z)
max_.append(max(numbers)) # get the maximum existed letters
q=max_[0] #since it's only one number so we put that value in value 

# now lets extract that letter depending on q value
l=[] 
for s,v in y.items() : 
     if v==q : #what is the value in the y that is equal to q
       l.append(s) #put it here


gg =''.join(map(str, l)) #now lets see what is the possible word
print(f" {gg} is the only common letter or phrase")
print("you want to shuffle it ? ")
print("why you don't give it a try" )
