import math
 
# step 1
p = 3
q = 11
 
# step 2
n = p*q
print("n =", n)
 
# step 3
phi = (p-1)*(q-1)
 
# step 4
e = 7
while(1<e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print("e =", e)
# step 5
d = 3
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
 
# plain text
with open('C:/Users/yonaaani/OneDrive/Рабочий стол/lab5/rsa1.txt', 'r') as file:
    plaintext = file.read().strip()
    
msg = int(plaintext)
print(f'Original message:{msg}')
 
# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print(f'Decrypted message: {M}')      
