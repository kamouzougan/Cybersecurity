'''
message = ' Three can keep a secret, if two of them are dead.'
translated = ' '
i = len(message) - 1 
while i >=0 : 
  translated = translated + message[i] 
  i = i - 1 
print(translated)
'''
'''
#Caeser Cipher 
import pyperclip
while True : 
    message = input("Please enter your message")
    key = 13 
    mode = input("Please enter your mode ~encrypt or ~decrypt~" )
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ' '
    for element  in message: 
       if  element  in SYMBOLS : 
           synbolIndex = SYMBOLS.find(element) 
           if   mode == 'encrypt':
               translatedIndex = synbolIndex + key 
           elif mode == 'decrypt':
               translatedIndex = synbolIndex - key 

           if translatedIndex >= len(SYMBOLS):
               translatedIndex = translatedIndex - len(SYMBOLS)
           elif translatedIndex < 0:
               translatedIndex = translatedIndex + len(SYMBOLS)
           translated = translated + SYMBOLS[translatedIndex]
       else :
           translated = translated + element
    print(translated)
    pyperclip.copy(translated)
# New ceaser cipher
'''
message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
   print('Hacking key #%s: %s' % (key, translated))        
