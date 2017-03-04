msg = []
with open("message_hitler.txt") as msg_f:
    for line in msg_f:
        msg.append(line)

letters = "E-N-I-R-S-T-A-H-D-U-L-C-G-M-O-B-W-F-K-Z-V-P-J-Y-X-Q-1-9-3-0-4-2-6-8-7".lower().split("-")
total = 18158
max_letters = []
for i in range(2, 27):
    freqs = [{letter:0 for letter in letters} for j in range(i)]
    counter = 0
    for string in msg:
        for letter in string:
            if letter in letters:
                freqs[counter][letter.lower()] += 1
                counter +=1
                counter %=i
    freq_letter_tupls = []
    for j in range(i):
        freq_letter_tupls.append(sorted([(freqs[j][letter]/(total/i+1), letter) for letter in freqs[j]])[::-1])
    print(freq_letter_tupls)
    maxes = []
    for j in range(i):
        maxes.append(freq_letter_tupls[j][0])
    max_letters.append(maxes)
print(max_letters)
