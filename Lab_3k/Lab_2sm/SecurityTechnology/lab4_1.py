import numpy as np

expansion_key=[4,1,2,3,2,3,4,1]
s_key1=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
s_key2=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
straight_key1=[1,3,4,2]

def expansion_box(key, value):
	print(key, value)
	sol=[value[key[i]-1] for i in range(len(key))]
	return sol


def sbox(key, a):
	print(a)
	x,y=int(str(a[0])+str(a[3]),2),int(str(a[1])+str(a[2]),2)
	sol="00"+bin(key[x][y])[2:]
	return [int(sol[0]),int(sol[1])]

def xor(a, b):
	return [a[i]^b[i] for i in range(len(a))]

def sdes_fun(key, right):
	print(right, key, "a")
	ex_right=expansion_box(expansion_key, right)
	print(ex_right,'b')
	xor_right=xor(key,ex_right)
	print(xor_right,'c')
	s_right=sbox(s_key1, xor_right[:4]) + sbox(s_key2, xor_right[4:])
	straight_right=expansion_box(straight_key1, s_right)
	return straight_right

def round(key, character):
	a = list(map(int, bin(character)[2:]))+[0]*8
	print(a)
	left,right=a[:4],a[4:]
	right1= sdes_fun(key, right)
	return int("".join( map(str,(right + xor(left, right1)))),2)

def p_box(key, values):
	li = [0 for _ in range(len(key))]
	for i,ele in enumerate(key):
		li[i] = values[ele]
	return li

def left_shift(key):
	return [key[-1]]+key[:len(key)-1]

def gen_keys(key):
	assert len(key)==10
	key = p_box([3,5,2,7,4,0,1,9,8,6], key)
	part1 = left_shift(key[:5])
	part2 = left_shift(key[5:])
	key1 = p_box([6,3,7,4,3,5,0,9], part1+part2)
	part1 = left_shift(part1)
	part2 = left_shift(part2)
	key2 = p_box([3,1,7,6,8,4,0,2], part1+part2)
	return key1, key2

def main():
    print("Welcome to secure encryption bank...")
    msg = list(map(ord, input("Please enter your message that needs to be encrypted: ")))

    key_input = input("Got it. Now, enter 10-digit secret key (binary or decimal): ")

    key_binary = format(int(key_input, 2) if key_input.isdigit() else int(key_input), '010b')
    key_binary = key_binary[-10:]
    key = list(map(int, key_binary))

    key1, key2 = gen_keys(key)

    # Encryption
    cipher = [round(key1, ch) for ch in msg]
    cipher = [round(key2, ch) for ch in cipher]
    print("Here's your encrypted message:", cipher)

main()


