alabete = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","å", "ä", "ö"] 
x = input("Skriv ett ord")
ord = x


for bokstav in ord:
        if bokstav =="ö":
            print(alabete[0])
        else: 
            plats = alabete.index(bokstav)
            print(alabete[plats+1])
      