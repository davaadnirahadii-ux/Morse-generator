import re

ascii_art = """
       .--.   
     /  -  \\   
    (  ( )  )  
     \\  -  /
       \\ /
     _.'   '._
    /  {  }  \\    | Morse generator | Created by: \033[31mDavaXbot \033[0m
"""

DavaMorse = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',
    '.': 'E',     '..-.': 'F',  '--.': 'G',   '....': 'H',
    '..': 'I',    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '/': ' '
}

text_to_morse = {}
for morse, char in DavaMorse.items():
    text_to_morse[char] = morse
text_to_morse[' '] = '/'

def text_to_morse_code(input_text):
    upper_input = input_text.upper()
    result = []
    for char in upper_input:
        if char in text_to_morse:
            result.append(text_to_morse[char])
        elif char == ' ':
            result.append('/')
        else:
            result.append('?')
    return ' '.join(result)

def morse_to_text(morse):
    words = morse.strip().split(' / ')
    result = []
    for word in words:
        chars = re.split(r'\s+', word.strip())
        decoded = ''
        for code in chars:
            if code in DavaMorse:
                decoded += DavaMorse[code]
            elif code == '/':
                decoded += ' '
            else:
                decoded += '?'
        result.append(decoded)
    return ' '.join(result)

def main():
    print(ascii_art)
    
    input_text = input('[ + ] Enter the text you want to convert to Morse code: ')
    morse_result = text_to_morse_code(input_text)
    print(f'\n[ + ] Morse code: {morse_result}')
    
    morse_input = input('\n[ + ] Enter Morse code to convert back to text (or press enter to skip): ')
    if morse_input.strip():
        text_result = morse_to_text(morse_input)
        print(f'\n[ + ] Text: {text_result}')

if __name__ == '__main__':
    main()