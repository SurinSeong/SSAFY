packed_values = 1, 2, 3, 4, 5

# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5


def my_function(x, y, z):
    print(x, y, z)


names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter


def my_function(x, y, z):
    print(x, y, z)


my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
# 이때, **my_dict = my_dict['x'], my_dict['y'], my_dict['z'] 이라고 생각하면 편할 듯!
