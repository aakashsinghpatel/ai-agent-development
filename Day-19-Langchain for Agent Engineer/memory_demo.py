from model import model


response = model.invoke("My name is Akash Patel.")

print("First response:")
print(response.content)


response = model.invoke("What is my name?")

print("\nSecond response:")
print(response.content)
