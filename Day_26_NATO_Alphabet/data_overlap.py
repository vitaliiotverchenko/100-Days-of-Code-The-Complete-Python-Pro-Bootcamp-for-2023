with open("Day_26_NATO_Alphabet\\file1.txt") as file1:
    file1_data = file1.read().strip().split("\n")
    lenght1 = len(file1_data)
with open("Day_26_NATO_Alphabet\\file2.txt") as file2:
    file2_data = file2.read().strip().split("\n")
    lenght2 = len(file2_data)
if lenght1 <= lenght2:
    result = [int(number) for number in file2_data if number in file1_data]
else:
    result = [int(number) for number in file1_data if number in file2_data]
print(result)
