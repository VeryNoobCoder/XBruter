import itertools
import random
import string


password = ''.join(random.choices(string.ascii_lowercase, k=4))
print(f"Target password: {password}")

print("Cracking combinations...")
for guess_tuple in itertools.product(string.ascii_lowercase, repeat=len(password)):
    guess = ''.join(guess_tuple)
    print(f"Cracking password: {guess}")

    if guess == password:
        print(f"Password has been cracked: {guess}")
        break
