# Defanger
A GUI application to defang text, rendering otherwise-potentially malicious IP addresses and URLs harmless. Built using standard Python libraries.

## Usage

Simply run the Defanger.py script (requires Python 3) to be presented with the GUI. You can then enter or paste the text you wish to defang.

By default, defanger will ignore (not defang) private IP addresses, although you can uncheck this option to defang all IP addresses.

Once you have defanged the input text, you can copy it to the clipboard, clear the defanger, or close using the buttons at the bottom.

## Example
Before defanging:
![alt text](https://github.com/mbabinski/Defanger/blob/main/Images/BeforeDefang.PNG?raw=true)

After defanging:
![alt text](https://github.com/mbabinski/Defanger/blob/main/Images/AfterDefang.PNG?raw=true)