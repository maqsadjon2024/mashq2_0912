#6
kublar = [son**3 for son in range(1, 6)]
print(kublar)

#7
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for row in matrix for item in row]
print(flat_list)

#8
words = ["dog", "cat", "mouse"]
first_letters = [word[0] for word in words]
print(first_letters)

#9
numbers = [-5, 3, -1, 0, 7, -2]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

#10
numbers = list(range(1, 11))
even_odd = ["juft" if num % 2 == 0 else "toq" for num in numbers]
print(even_odd)
