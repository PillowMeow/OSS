def reverse(word): return word[::-1]
print(reverse('testing'))


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspbrry', 'banana']
print(sorted(fruits, key=reverse))