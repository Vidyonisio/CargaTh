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
print("meses = " + str(meses))


print("M1 = " + str(month1))
print("M2 = " + str(month2))
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

def run_anos(Ref, M1):  #Função para iterar ao longo de vários anos de contrato
    j = 1
    while j <((Ref - M1)/12):
        for i in range(11):
            it_mono_tab()
        it_duplo_tab()
        j+=1

def ult_ano(M2):  #Função para preencher o último ano ajustadamente
    for i in range(M2 - 2):
        it_mono_tab()

        # if meses > 121 - month1:
        #     j = 1
        #     while j < ((121 - month1) / 12):
        #         i = 1
        #         while i < 12:
        #             it_mono_tab()
        #             i += 1
        #         it_duplo_tab()
        #         j += 1
        #     i = 1
        #     while i < month2 - 1:
        #         it_mono_tab()
        #         i += 1
        # elif meses > 109 - month1:
        #     j = 1
        #     while j < ((109 - month1) / 12):
        #         i = 1
        #         while i < 12:
        #             it_mono_tab()
        #             i += 1
        #         it_duplo_tab()
        #         j += 1
        #     i = 1
        # else:           #Caso em que o segundo ano já é o último, itera até finalizar ele
        #     i = 1
        #     while i < month2-1:
        #         it_mono_tab()
        #         i += 1



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
        for i in range(12 - month1):   #Peenchimento do primeiro ano até o final
            it_mono_tab()
            i += 1
        it_duplo_tab()    #Roda o segundo duplo tab pra entrar no ano seguinte

        if meses+month1 <= 25: # Caso em que o segundo ano já é o último, itera até finalizar ele
            ult_ano(month2)
        else:             #Itera até varrer tudo
            k = 121
            while k > 24:
                if meses > k-month1:
                    run_anos(k,month1)
                    ult_ano(month2)
                    break
                k -= 12

    else:  #Caso em que não pula pra outro ano
        i = 1
        while i < (month2-month1):
            it_mono_tab()
            i += 1

if cab_ano == 'N':
    it_mono_tab() #Iteração simples inicial por ser cabeça
    if year2 > year1:
        for i in range(12 - month1):   #Peenchimento do primeiro ano até o final
            it_mono_tab()
            i += 1
        it_duplo_tab()    #Roda o segundo duplo tab pra entrar no ano seguinte

        if meses+month1 <= 25: # Caso em que o segundo ano já é o último, itera até finalizar ele
            ult_ano(month2)
        else:             #Itera até varrer tudo
            k = 121
            while k > 24:
                if meses > k-month1:
                    run_anos(k,month1)
                    ult_ano(month2)
                    break
                k -= 12

    else:  #Caso em que não pula pra outro ano
        i = 1
        while i < (month2-month1):
            it_mono_tab()
            i += 1
else:
    print("Escreve S ou N k#$*#")

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
pyautogui.press('esc')







