
greeting = "Good Morning"
a = 4

if greeting == "Morning":
    print("Condition Matches")
else:
    print("Condition Not Matched")
print("if else condition code is completed")

if a > 2:
    print("Condition Matches")
else:
    print("Condition Not Matched")
print("if else condition code is completed")


#for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of first natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1,6):  #range(i,j) -> i to j-1
    summation = summation + j
    print(j)
print(summation)

print("****************************************")
for k in range(1,10,5):
    print(k)

print("****************************************")
for m in range(10):
    print(m)
