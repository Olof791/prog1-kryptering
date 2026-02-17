alabete = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","å", "ä", "ö"] 
x = input("Skriv ett ord")
ord = x


for bokstav in ord:
        plats = alabete.index(bokstav)
        print(alabete[(plats+3)%29])
      