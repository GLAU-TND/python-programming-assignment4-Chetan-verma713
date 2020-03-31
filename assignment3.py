sub_set = input('Enter the subset : ')
print('Enter the set : ',end = '')
given_set = list(map(str,input().split()))
output_set = []
c = len(sub_set)
for i in given_set:
    if i[:c] == sub_set:
        output_set.append(i)
print('output set is : ',output_set)
