Problem-4:  Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
    (examples)
    input: [1,2,8,9,12,46,76,82,15,20,30]
    Output:
        {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
//Python program to count the frequency of the elements in a list using a dictionary
def CountFrequency(my_list):
// creating an empty dictionary
freq={}
for item in my_list:
if{item in freq):
freq[item]+=1
else:
freq[item]=1
for key,value in freq.items():
print("%d : %d " %(key,value))
//drive function
if__ name__== "__main__":
my_list=[1,2,3,4,5,6,7,8,9]
CountFrequency(my_list)
