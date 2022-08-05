import pyautogui
import time
import datetime

"Automatiza o preenchimento da curva de carga nas boletas do Thunder via Bot"
"É necessário estar com a planilha com os imputs aberta e a boleta aberta com o campo inicial selecionado na 3a janela"

cab_ano = input('É cabeça de ano? [S/N]: ')
date_entry1 = input('Coloque a Data inicial no formato: MM/YYYY: ')
month1, year1 = map(int, date_entry1.split('/'))
day1 = int(1)
date1 = datetime.date(year1, month1, day1)
date_entry2 = input('Coloque a Data Final no formato MM/YYYY e posicione o mouse na planilha antes de dar enter: ')
day2 = int(1)
month2, year2 = map(int, date_entry2.split('/'))
date2 = datetime.date(year2, month2, day2)


# diff = date2-date1
# days = diff.days
# diff_m = days // 29

meses = (date2.year - date1.year) * 12 + date2.month - date1.month + 1
print(meses)



print(date1)
print(date2)

#print(pyautogui.position())
#pyautogui.moveTo(3500,10)

def it_duplo_tab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrlleft', 'c')
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrlleft', 'v')


def it_mono_tab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrlleft', 'c')
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrlleft', 'v')


pyautogui.click()
time.sleep(0.4)
pyautogui.click()
#print(pyautogui.KEYBOARD_KEYS)
pyautogui.hotkey('ctrlleft','c')
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
pyautogui.hotkey('ctrlleft', 'v')

if cab_ano == 'S':
    it_duplo_tab()

    if year2 > year1:
        i = 0
        while i < (12 - month1):
            it_mono_tab()
            i += 1

        it_duplo_tab()
        if meses > 24:
            print("nada")
        else:
            i = 1
            while i < month2-1:
                it_mono_tab()
                i += 1
    else:
        i = 1
        while i < (month2-month1):
            it_mono_tab()
            i += 1
else:
    print("nada")

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
pyautogui.press('esc')
print(i)







