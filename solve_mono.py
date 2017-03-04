msg = []
letter_freqs = {}
with open("message_hitler.txt") as msg_f:
    for line in msg_f:
        msg.append(line)
with open("message_hitler_freq.txt") as msg_freq_f:
    for line in msg_freq_f:
        line = line.strip()
        letter_freqs[line.split(" ")[1]] = int(line.split(" ")[0])
print(letter_freqs)
total = 0
for letter in letter_freqs:
    total += letter_freqs[letter]
freq_letter_tupls = sorted([(letter_freqs[letter]/total, letter) for letter in letter_freqs])[::-1]
german_freq_order = "E-N-I-R-S-T-A-H-D-U-L-C-G-M-O-B-W-F-K-Z-V-P-J-Y-X-Q-1-9-3-0-4-2-6-8-7".lower().split("-")
print(german_freq_order)
tentative_dict = {freq_letter_tupls[i][1]: german_freq_order[i] for i in range(len(german_freq_order))}
#lol
tentative_dict[" "] = " "
tentative_dict[","] = ","
tentative_dict["."] = "."
tentative_dict["?"] = "?"
tentative_dict["!"] = "!"
tentative_dict["\n"] = "\n"
tentative_dict["-"] = "-"
tentative_dict[";"] = ";"
tentative_dict[":"] = ":"
print(tentative_dict)
def replace_letters(string):
    return "".join([tentative_dict[letter.lower()] for letter in string])
message = [replace_letters(line) for line in msg]
print(message)
