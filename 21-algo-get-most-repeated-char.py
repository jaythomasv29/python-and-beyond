
sentence = 'This is a common interview question'
# transform to a dictionary with the count as the value

count_dic = dict()
for char in [*sentence]:
    # print(char in sentence)
    if char not in count_dic and char is not char.isspace():
        count_dic[char] = 1
    else:
        count_dic[char] += 1

print(count_dic.items())

frequency = sorted(count_dic.items(), key=lambda x: x[1], reverse=True)
print(frequency[0])


# using .get( with default value)
def get_most_repeated_char(str):
    count = {}
    for char in str:
        count[char] = count.get(char, 0) + 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)[0]


print('.get', get_most_repeated_char(sentence))
