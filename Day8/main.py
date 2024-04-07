from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(txt, sft, drc):
    new_text = ""
    for t in txt:
        if t not in alphabet:
            new_text += t
        else:
            idx = alphabet.index(t)
            if drc == "encode":
                new_idx = (idx + sft) % 26
            else:
                new_idx = (idx - sft) % 26
            new_text += alphabet[new_idx]
    print(f"The {drc}d text is {new_text}")


print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction not in ["encode", "decode"]:
        print("Please enter the word correctly.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    loop = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if loop == "no":
        break
    else:
        continue
