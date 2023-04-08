import inspect
import colorama

print(f"Attributes: {dir(colorama)}\n")

print("Methods:")
for name, data in inspect.getmembers(colorama, inspect.isfunction):
    print(f"{name}: {data}")

