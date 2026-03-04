#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length):
    # Define the character set: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# User input: ask for password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Generate and display the password
new_password = generate_password(length)
print("Generated Password:", new_password)


# In[ ]:




