"""You are tasked with a complex matrix operation. 
You will need to input the size of the matrix and then provide the elements of the matrix. 
The main matrix must then be divided into two submatrices: one for even-indexed elements and the other for odd-indexed elements. 
Following this, you are required to sort both the even and odd matrices in ascending order. 
Finally, you must calculate and print the sum of the second largest numbers from both matrices.

For example:

Enter the size of the array: 5
Enter the element at the 0th index: 3
Enter the element at the 1st index: 4
Enter the element at the 2nd index: 1
Enter the element at the 3rd index: 7
Enter the element at the 4th index: 9

After sorting:
Sorted even array: 1 3 9
Sorted odd array: 4 7

The sum of the second largest numbers from both matrices is 7."""

# create empty array 
array = []
evenArr = []
oddArr = []

# take input for array size
n = int(input("Enter the size of the array:"))

# append values in array
for i in range(0,n):
    number = int(input("Enter Element at {} index:".format(i)))
    array.append(number)
    if i % 2 == 0:
        evenArr.append(array[i])
    else:
        oddArr.append(array[i])
        
#sort even array        
evenArr = sorted(evenArr)
print("Sorted Even Array:", evenArr[0:len(evenArr)])

#sort odd array
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])

# addition of second largest number 
print("The sum is: ",evenArr[-2] + oddArr[-2])
