import pyautogui

# alert
# it has only one button
btn_1 = pyautogui.alert(text='warning !', title='title', button='OK')
print(btn_1)
print(type(btn_1))

# confirm 
# it can make multiple buttons
btn_2 = pyautogui.confirm(text='check ?', title='title', buttons=['OK', 'cancel'])
print(btn_2)

# prompt
# it can input text message
btn_3 = pyautogui.prompt(text='input', title='title', default='message')
print(btn_3)

# password
btn_4 = pyautogui.password(text='password', title='title', mask='$')
print(type(btn_4))
if btn_4 == '12345':
    print('corrent !')
else:
    print('wrong !')