import matplotlib.pyplot as plt
import time
import random
import string

# message generation

length = 1000000

character_list = []

for i in range(length):

    letter = random.choice(string.ascii_letters)

    character_list.append(letter)

message = "".join(character_list)

# key for the complex encryption
key = "SECRET"

# Caesar encryption

def encrypt_caesar(text):

    result_list = []

    for c in text:
        new_char = chr((ord(c) + 3) % 256)
        result_list.append(new_char)
    result = "".join(result_list)
    return result

# labyrinth encryption 

def encrypt_labyrinth(text, key):

    result_list = []
    key_length = len(key)
    for i in range(len(text)):
        letter = text[i]
        shift = ord(key[i % key_length])
        new_char = chr((ord(letter) + shift) % 256)
        result_list.append(new_char)
    result = "".join(result_list)
    return result

# message encryption

print("Caesar encryption...")
caesar_encrypted = encrypt_caesar(message)

print("Labyrinth encryption...")
labyrinth_encrypted = encrypt_labyrinth(message, key)

# caesar cracking

def crack_caesar(encrypted_text):
    start = time.perf_counter()
    for shift in range(256):
        result_list = []
        for c in encrypted_text[:30]:
            new_char = chr((ord(c) - shift) % 256)
            result_list.append(new_char)
        result = "".join(result_list)
        if result == message[:30]:
            elapsed_time = time.perf_counter() - start
            print("Caesar cracked")
            print("Shift found:", shift)
            return elapsed_time

# Labyrinth cracking

def crack_labyrinth(encrypted_text):

    start = time.perf_counter()

    alphabet = string.ascii_uppercase

    attempts = 0

    # simulation of a more difficult attack

    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:

                    test_key = a + b + c + d

                    result_list = []

                    # only 30 characters
                    for i in range(30):

                        letter = encrypted_text[i]

                        shift = ord(test_key[i % 4])

                        new_char = chr((ord(letter) - shift) % 256)

                        result_list.append(new_char)

                    result = "".join(result_list)

                    attempts = attempts + 1

                    # limit to avoid a program that runs too long

                    if attempts >= 300000:

                        elapsed_time = time.perf_counter() - start

                        print("Labyrinth not cracked")
                        print("Attempts:", attempts)

                        return elapsed_time

# tests

print()
print("Caesar cracking in progress...")

caesar_time = crack_caesar(caesar_encrypted)

print()
print("Labyrinth cracking in progress...")

labyrinth_time = crack_labyrinth(labyrinth_encrypted)

# results

print()

print("Caesar time:", round(caesar_time, 5), "seconds")

print("Labyrinth time:", round(labyrinth_time, 5), "seconds")

# graph

names = ["Caesar", "Labyrinth"]

times = [caesar_time, labyrinth_time]

plt.figure(figsize=(8, 5))

plt.bar(names, times, color=["blue", "red"])

plt.title("Comparison of cracking time")

plt.ylabel("Time in seconds")

# display values

for i in range(len(times)):

    plt.text(i, times[i], str(round(times[i], 5)) + " s", ha="center")
    
plt.show()