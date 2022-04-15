from pprint import pprint

sentence = 'This is a common interview question'
# transform to a dictionary with the count as the value

count_dic = dict()
for char in [*sentence]:
    # print(char in sentence)
    if char not in count_dic and char is not char.isspace():
        count_dic[char] = 1
    else:
        count_dic[char] += 1
# pprint(count_dic, width=1)
print(count_dic.items())

frequency = sorted(count_dic.items(), key=lambda x: x[1], reverse=True)
print(frequency[0])
