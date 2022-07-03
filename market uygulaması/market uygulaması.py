import pandas as pd
import datetime

envanter = {"kuşkonmaz": [6, 3], "brokoli": [20, 7], "havuç": [15, 5], "elmalar": [25, 15], "muz":
  [19, 18], "meyve": [23, 5], "yumurta": [44, 4], "karışık meyve suyu": [1, 19], "balık çubukları": [27, 10],
            "dondurma": [0, 4],
            "elma suyu": [33, 8], "portakal suyu": [32, 4], "üzüm suyu": [21, 16]}

dict_sifreler = {"ahmet": "İstinye123", "meryem": "4444"}  # KAYITLI KULLANICILAR

print("**** İstinye Online Market’e Hoşgeldiniz ****")
print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:")
kullanıcı = input("Kullanıcı adı:")
sifre = input("Şifre:")

while dict_sifreler.get(kullanıcı) != sifre:  # KULLANICI DOĞRULUĞU
  print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
  kullanıcı = input("Kullanıcı adı:")
  sifre = input("Şifre:")
else:
  print("Başarıyla giriş yapıldı!")
  print("Hoşgeldiniz", kullanıcı, "Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")

print(
  "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
ana_menu_secim = int(input("Seçiminizi girin:"))
prod_data = pd.DataFrame(envanter.keys()).rename(columns={0: 'products'})
sepet_bilgileri = {'ahmet': {}, 'meryem': {}}  # KULLANICI SEPETŞERİ

while ana_menu_secim != 5:
  if ana_menu_secim == 1:  # ÜRÜN ARAMA
    product_selection = str(input("Ürün Seçiminizi girin:").lower())
    selected_products = prod_data[prod_data['products'].str.contains(product_selection)].reset_index(drop=True)
    if len(selected_products) == 0:
      geri_ana_menu = int(
        input('Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin, tekrar denemek için herhangi bir sayıyı tuşlayın):'))
      if geri_ana_menu == 0:
        print(
          "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
        ana_menu_secim = int(input("Seçiminizi girin:"))
      continue
    else:
      for i, j in selected_products.iterrows():
        print(str(i + 1) + " " + (j[0]))
      ürün_secim_index = int(input('Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):'))
      if ürün_secim_index == 0:
        print(
          "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
        ana_menu_secim = int(input("Seçiminizi girin:"))
      elif ürün_secim_index > i:
        print("Tekrar deneyin")
      else:
        tutar_input = int(input("{production} ekleniyor. Tutarı Girin:".format(
          production=selected_products['products'].tolist()[ürün_secim_index - 1])))
        if tutar_input <= envanter[selected_products['products'].tolist()[ürün_secim_index - 1]][0]:
          ## sepete ekle
          sepet_bilgileri[kullanıcı].update({selected_products['products'].tolist()[ürün_secim_index - 1]: tutar_input})
          print('Sepetinize {} eklendi.'.format(selected_products['products'].tolist()[ürün_secim_index - 1]))
          print('Ana menüye geri dönülüyor ...')
          print(
            "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
          ana_menu_secim = int(input("Seçiminizi girin:"))
        else:
          while tutar_input > envanter[selected_products['products'].tolist()[ürün_secim_index - 1]][0]:
            tutar_input = int(input(
              'Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin Miktar (Ana menü için 0 girin):'))
            if tutar_input == 0:
              print(
                "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
              ana_menu_secim = int(input("Seçiminizi girin:"))
            elif tutar_input > envanter[selected_products['products'].tolist()[ürün_secim_index - 1]][0]:
              continue
            else:
              sepet_bilgileri[kullanıcı].update(
                {selected_products['products'].tolist()[ürün_secim_index - 1]: tutar_input})
              print('Sepetinize {} eklendi.'.format(selected_products['products'].tolist()[ürün_secim_index - 1]))
              print('Ana menüye geri dönülüyor ...')
              print(
                "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
              ana_menu_secim = int(input("Seçiminizi girin:"))

  elif ana_menu_secim == 2:  # SEPETE ERİŞİM
    if len(sepet_bilgileri[kullanıcı]) == 0:
      print('Sepetiniz boştur. Ana Menüye Yönlendiriliyorsunuz.')
      print("Toplam 0 $")
      print(
        "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
      ana_menu_secim = int(input("Seçiminizi girin:"))
    else:
      print('Sepetiniz şunları içerir:')
      my_number = 1
      toplam_tutarım = 0
      for i in sepet_bilgileri[kullanıcı]:
        print(str(my_number) + ". " + i + " fiyatı = " + str(envanter[i][1]) + " $ " +
              "miktar = " + str(sepet_bilgileri[kullanıcı][i]) + " toplam = " + str(
          envanter[i][1] * sepet_bilgileri[kullanıcı][i]) + " $")
        toplam_tutarım = toplam_tutarım + envanter[i][1] * sepet_bilgileri[kullanıcı][i]
        my_number = my_number + 1
      print("Toplam " + str(toplam_tutarım) + " $")
      print("Bir seçeneği seçiniz:", "\n", "1. Tutarı güncelleyin", "\n", "2. Bir öğeyi kaldırın", "\n", "3. Satın al",
            "\n", "4. ana menüye dön")
      sepet_ana_menu = int(input("Seçiminiz:"))
      if sepet_ana_menu == 4:  # SEPETTEN ÇIKIŞ İŞLEMİ
        print(
          "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
        ana_menu_secim = int(input("Seçiminizi girin:"))
      elif sepet_ana_menu == 1:  # SEPET İÇİ MİKTAR DEĞİŞTİRME İŞLEMİ
        for i in sepet_bilgileri[kullanıcı]:
          urun_degisim_input = int(input(i + " " + str(sepet_bilgileri[kullanıcı][i]) + ":"))
          # Ürün fazla ise güncelleme kontrol yapılacak.
          if envanter[i][0] > urun_degisim_input:
            sepet_bilgileri[kullanıcı][i] = urun_degisim_input
          else:
            print("Üzgünüm! Miktar sınırı aşıyor.")

      elif sepet_ana_menu == 2:  # SEPET İÇİ ÜRÜN KALDIRMA İŞLEMİ

        print("Ürünü kaldırmak istiyorsanız ürün geldiğinde 0 kaldırmak istemiyorsanız herhangi sayı giriniz.")
        silinecekler = []
        for i in sepet_bilgileri[kullanıcı]:
          urun_silme_input = int(input(i + " " + str(sepet_bilgileri[kullanıcı][i]) + ":"))
          if urun_silme_input == 0:
            silinecekler.append(i)
        if len(silinecekler) > 0:
          for i in silinecekler:
            del sepet_bilgileri[kullanıcı][i]

      elif sepet_ana_menu == 3:  # SEPET İÇİ SATIN ALMA İŞLEMİ
        print("Makbuzunuz işleniyor ...", "\n", "******* İstinye Online Market ********", "\n",
              "*************************************", "\n", "0850 283 6000", "\n", "istinye.edu.tr")
        print("-" * 30)
        my_number = 1
        toplam_tutarım = 0
        for i in sepet_bilgileri[kullanıcı]:
          print(str(my_number) + ". " + i + " fiyatı = " + str(envanter[i][1]) + " $ " +
                "miktar = " + str(sepet_bilgileri[kullanıcı][i]) + " toplam = " + str(
            envanter[i][1] * sepet_bilgileri[kullanıcı][i]) + " $")
          toplam_tutarım = toplam_tutarım + envanter[i][1] * sepet_bilgileri[kullanıcı][i]
          my_number = my_number + 1
          envanter[i][0] = envanter[i][0] - int(sepet_bilgileri[kullanıcı][i])
        print("-" * 30)
        print("Toplam " + str(toplam_tutarım) + " $")
        x = datetime.datetime.now()
        print(x)
        print("Online Market’imizi kullandığınız için teşekkür ederiz!")

  elif ana_menu_secim == 3:  # SATIN ALMA İŞLEMİ
    print("Makbuzunuz işleniyor ...", "\n", "******* İstinye Online Market ********", "\n",
          "*************************************", "\n", "0850 283 6000", "\n", "istinye.edu.tr")
    print("-" * 30)
    my_number = 1
    toplam_tutarım = 0
    for i in sepet_bilgileri[kullanıcı]:
      print(str(my_number) + ". " + i + " fiyatı = " + str(envanter[i][1]) + " $ " +
            "miktar = " + str(sepet_bilgileri[kullanıcı][i]) + " toplam = " + str(
        envanter[i][1] * sepet_bilgileri[kullanıcı][i]) + " $")
      toplam_tutarım = toplam_tutarım + envanter[i][1] * sepet_bilgileri[kullanıcı][i]
      my_number = my_number + 1
      envanter[i][0] = envanter[i][0] - int(sepet_bilgileri[kullanıcı][i])
    print("-" * 30)
    print("Toplam " + str(toplam_tutarım) + " $")
    x = datetime.datetime.now()
    print(x)
    print("Online Market’imizi kullandığınız için teşekkür ederiz!")
    print(
      "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
    ana_menu_secim = int(input("Seçiminizi girin:"))

  elif ana_menu_secim == 4:  # OTURUM KAPATMA
    print("OTURUM KAPATILIYOR.")
    print("**** İstinye Online Market’e Hoşgeldiniz ****")
    print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:")
    kullanıcı = input("Kullanıcı adı:")
    sifre = input("Şifre:")

    while dict_sifreler.get(kullanıcı) != sifre:  # KULLANICI DOĞRULUĞU
      print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
      kullanıcı = input("Kullanıcı adı:")
      sifre = input("Şifre:")
    else:
      print("Başarıyla giriş yapıldı!")
      print("Hoşgeldiniz", kullanıcı, "Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")

    print(
      "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
    ana_menu_secim = int(input("Seçiminizi girin:"))



  else:
    print("YANLIŞ BİR DEĞER GİRDİNİZ TEKRAR DENEYİN")
    print(
      "\n" "Lütfen aşağıdaki hizmetlerden birini seçin:" "\n" "1. Ürün ara" "\n" "2. Sepete git" "\n""3. Satın al" "\n" "4. Oturum Kapat" "\n" "5. Çıkış yap")
    ana_menu_secim = int(input("Seçiminizi girin:"))


