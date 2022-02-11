import typing
import os

BASE_DIR = os.getcwd()

args = [3, 5, 6, '7']
result = []
mod = int
for var1 in args:
    if type(var1) != mod:
        typing.cast(mod, var1)
        var1 = mod(var1)
    result.append(var1)

print(f'Путь к каталогу проекта - {BASE_DIR}')
print(result)

