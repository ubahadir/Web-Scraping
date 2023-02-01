from gmail_api_json import numaralar, isimler
import pywhatkit


# print (len(numaralar))
# print (len(isimler))

smmm_isimler = []
smmm_numaralar = []
smmm_numaralar_son = []
smmm_isim_index = []

#içinde smmm ifadesi geçen isimleri bir listeye ekliyor
for isim in isimler:

    if "smmm" in isim.lower():

        smmm_isimler.append(isim)
        index = isimler.index(isim)
        smmm_isim_index.append(index)

#+90 ekliyor numaraların başına
for numara in numaralar:

    if numara[0] == "0":

        numara = "+9" + numara
        

for index in smmm_isim_index:

    smmm_numaralar.append(numaralar[index])

for numara in smmm_numaralar:

    if numara[0] == "0" and len(numara) == 11:
        
        numara = "+9" + numara
        smmm_numaralar_son.append(numara)


# print (len(smmm_numaralar_son))

# yunus ozhan
# devrim karadag
# berkay gokce
# suleyman turan


# #smmm numaraları ve isimleri doğru eşleşti
# print(smmm_isimler[100] + " " + smmm_numaralar[100])
# print(smmm_isimler[5] + " " + smmm_numaralar[5])
# print(smmm_isimler[123] + " " + smmm_numaralar[123])
# print(smmm_isimler[253] + " " + smmm_numaralar[253])

# pywhatkit.sendwhatmsg("+905556277992", "Geeks For Geeks!", 15,30)