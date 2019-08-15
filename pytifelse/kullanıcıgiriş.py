print("**********Kullanıcı Girişi***********\n ")
sys_nickname = "hasan"
sys_password = "12345"

nickname = input("Kullanıcı Adı : ")
password = input("Şifre : ")

if(nickname != sys_nickname and password == sys_password):
    print("Kullanıcı Adı Hatalı")
elif(nickname == sys_nickname and password != sys_password):
    print("Şifre Hatalı")
elif(nickname != sys_nickname and password != sys_password):
    print("Hepsi Hatalı")
else:
    print("Giriş onaylandı")
 