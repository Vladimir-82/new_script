import typing
import yaml


with open('input.yaml') as f:
    data = yaml.safe_load(f)
args = [values for values in data.values()]


result = []
mod = int
for var1 in args:
    if type(var1) != mod:
        typing.cast(mod, var1)
        var1 = mod(var1)
    result.append(var1)

to_yaml = {'IT': result[0], 'id': result[1], 'to_id': result[2]}

with open('output.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)