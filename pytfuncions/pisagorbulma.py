def pisagor_bul():
    pisagor_list = []
    for i in range(1,101):
        for j in range(1,101):
            c = (i ** 2 + j ** 2) ** 0.5

            if(c == int(c)):
                pisagor_list.append((i,j,int(c)))
    
    return pisagor_list

for i in pisagor_bul():
    print(i)

