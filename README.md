# WhatsappBot
A bot to send repetitive messages to that one person you really wanna irritate.<br>

### Prerequisites
Selenium - `pip install selenium` (windows)<br>
Chrome driver - https://chromedriver.chromium.org/downloads<br><br>

### How to use
1. Change the title area to the name of the contact you wish to spam. Ensure the name is spelled the same as how you've saved their contact. <br>
```python:
person = driver.find_element_by_css_selector('span[title="CHANGE THIS"]')
```
2. Change the message to a unique message you wish to send <br>
```python:
textarea.send_keys('Your Unique Message')
```
3. 'n' represents the number of times your unique messages are going to be sent.
```python:
i=0
n=50
```
4. Run it using Powershell (windows)
5. A chrome tab should open up with whatsapp QR code.
6. Scan the code with your phone.
7. Press any key in the shell.
8. You're done!
<br><br>
___I'm sorry for the people who are going to suffer from this.___
