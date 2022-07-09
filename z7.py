print("Программа может перевести:")
print("1. Дюймы в сантиметры \n2. Сантиметры в дюймы\n3. Мили в километры\n4. Километры в мили\n5. Фунты в килограммы\n6. Килограммы в фунты\n7. Унции в граммы\n8. Граммы в унции\n9. Галлон в литры\n10. Литры в галлоны\n11. Пинты в литры\n12. Литры в пинты ")

while True:
    ch = float(input("Выберите пункт:"))
    vxod = float(input("Ввдети значение для конвертации:"))
    def d_in_cm():
        res1 = vxod * 2.54
        print(res1)

    def cm_in_d():
        res2 = vxod * 0.6
        print(res2)

    def m_in_km():
        res3 = vxod * 1.6
        print(res3)

    def km_in_m():
        res4 = vxod / 1.6
        print(res4)

    def lb_in_kg():
        res5 = vxod * 0.4535
        print(res5)

    def kg_in_lb():
        res6 = vxod * 2.2046226
        print(res6)

    def ou_in_g():
        res7 = vxod * 28.35
        print(res7)

    def g_in_ou():
        res8 = vxod / 28.35
        print(res8)

    def ga_in_li():
        res9 = vxod * 3.78541
        print(res9)

    def li_in_ga():
        res10 = vxod / 3.78541
        print(res10)

    def pi_in_li():
        res11 = vxod * 0.4731
        print(res11)

    def li_in_pi():
        res12 = vxod / 0.4731
        print(res12)



    if ch == 0:
        break

    if ch == 1:
        d_in_cm()

    if ch == 2:
        cm_in_d()

    if ch == 3:
        m_in_km()

    if ch == 4:
        km_in_m()

    if ch == 5:
        lb_in_kg()

    if ch == 6:
        kg_in_lb()

    if ch == 7:
        ou_in_g()

    if ch == 8:
        g_in_ou()

    if ch == 9:
        ga_in_li()

    if ch == 10:
        li_in_ga()
        
    if ch == 11:
        pi_in_li()

    if ch == 12:
        li_in_pi()
    else:
        print("Вы ввели неверный номер!")
        
    
        
        
       






