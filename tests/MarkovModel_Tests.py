# Save with Pickle
from RainbowChain import RainbowChain

model = RainbowChain("test_data.txt", 3)

print("FORWARD:\n")
for i in range(10):
    print(model.generate_sentence())

print("\n\n\n")

print("BACKWARD:\n")
for i in range(10):
    print(model.generate_sentence(True))

print("\n\n\n")

print("MIDDLE OUT:\n")
for i in range(10):
    print(model.generate_with_seed('coffee'))
