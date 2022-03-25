def inputToMorsecode(sentenceInFunction):
    morseCodeDict = {' ': '_', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-',
                     '/': '-..-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                     '6': '-....', '7': '--...', '8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.',
                     '?': '..--..', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                     'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                     'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--.-'}

    # sentence ex : Ameez loves food
    # A m e e z  l o v e s  f o o d

    output = []
    for ele in sentenceInFunction:
        output.append(morseCodeDict[ele])

    for ele in output:
        print(ele, end='')


def main():
    testCase = int(input())
    while testCase != 0:
        sentence = input()
        sentence = sentence.upper()
        inputToMorsecode(sentence)
        testCase -= 1


if __name__ == '__main__':
    main()
