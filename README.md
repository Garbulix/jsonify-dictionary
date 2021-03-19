# jsonify-dictionary
![banner](https://user-images.githubusercontent.com/22769121/111780843-3cc78200-88b8-11eb-940f-e03bb024551e.png)

Script made for converting my dictionary word lists from [passphrase generator](https://github.com/Garbulix/word-password-generator) into JSON that has small number of internal objects but with a lot of content.

## how it works
Data that are intended to JSONify need to be between curly braces (everything that is before **{** and after **}** is ignored).  
String that starts with the **#** is assumed as internat object variable name. Every line that is below that *hashed one* is assumed as separate element of an array (or just as the string if there is only one line below).
No need to put strings in quotation marks. 
  
Example of use is in "example directory"

## early stage limitations
- there is no number validation -> only strings are created  
- program is not validating syntax
