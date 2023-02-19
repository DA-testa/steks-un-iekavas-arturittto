#Artūrs Čubukovs 16.grupa 221RDB127 1.m.d.Datu struktūras
class Bracket:
    def __init__(self, char, position):
        self.char = char
        self.position = position
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i))

        if char in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, char):
                return i + 1
                
            if are_matching(opening_brackets_stack[-1].char, char):
                opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[-1].position + 1
def main():
    text = input()
    if 'I' in text:
        text = input()
    elif 'F' in text:
        file = "./test/5"
        with open(file) as f:
            text = f.read()
    mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)
if __name__ == "__main__":
    main()
