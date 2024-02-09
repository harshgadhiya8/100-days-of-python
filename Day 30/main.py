# try:
#     file = open('file.txt')
#     a_dict = {'sdfgvfsdg':'sdfgvsgs'}
#     print(a_dict['sdfgvfsdg'])
# except FileNotFoundError:
#     file = open('file.txt','w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'That key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError('udjfbghsdjuf')

h = int(input())
w = int(input())

if h > 3:
    raise ValueError('Human height should not be over 3')


bmi = w/h**2
print(bmi)