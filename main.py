import pyautogui
import time
import datetime

"Automatiza o preenchimento da curva de carga nas boletas do Thunder via Bot"


print("IMPORTANTE: É necessário estar com a planilha com os imputs aberta e a boleta aberta com o campo inicial selecionado na 3a janela e todos os anos já abertos")

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

"print(pyautogui.position())" #Comandos auxiliares não utilizados
"pyautogui.moveTo(3500,10)"

def it_duplo_tab():  #Função de copiar e colar com duplo tab
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


def it_mono_tab():  #Função de copiar e colar com um tab
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


pyautogui.click()        #Rodada inicial de copiar do campo com mouse no excel e colar no primeiro campo pre-selecionado do thunders
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
    it_duplo_tab()    #Iteração dupla inicial por ser cabeça

    if year2 > year1:
        i = 0
        while i < (12 - month1):   #Peenchimento do primeiro ano até o final
            it_mono_tab()
            i += 1

        it_duplo_tab()    #Roda o segundo duplo tab pra entrar no ano seguinte
        if meses > 121 - month1:
            print("caiu 121")
        elif meses > 25 - month1:
            i = 1
            while i < 12:
                it_mono_tab()
                i += 1
            it_duplo_tab()
            i = 1
            while i < month2 - 1:
                it_mono_tab()
                i += 1
        else:           #Caso em que o segundo ano já é o último, itera até finalizar ele
            i = 1
            while i < month2-1:
                it_mono_tab()
                i += 1
    else:  #Caso em que não pula pra outro ano
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







