#Simple class to translate to/from Morse.
#Ria Jairam, N2RJ 2023
#Use the slash (/) char to separate words and spaces are translated to slash.


class Morse:
  def __init__(self):
    #International Morse, Roman alphabet (for now). Easy to add others, eg. Cyrillic. 
    self.CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-', 
        ' ': '/'}
    
    self.CODE_INV=dict((v,k) for k,v in self.CODE.items())

 #Take a word and convert to Morse in a dictionary   
  def encode(self, morse_word):
    morse_out=[]
    for letter in morse_word:
      morse_out.append(self.CODE.get(letter.upper()))
    return morse_out
  
 #Take a morse string and convert into a word 
  def decode (self, morse_code):
    word_out=""
    morse_dict = morse_code.split()
    for chars in morse_dict:
        if (self.CODE_INV.get(chars)):
          word_out+=(self.CODE_INV.get(chars))
        else:
           word_out +="?"
    return word_out