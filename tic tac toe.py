#tic tac toe

brett = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

user = True #skriver den x, hvis ikke o
runder = 0

def print_brett(brett):
    for rad in brett:
        for rute in rad:
            print(f"{rute} ", end="")
        print()      

def avslutt(user_input):
    if user_input == "q":
        print("Thanks for playing")
        return True
    else: return False
    
def check_input(user_input):
    #se etter om input er et tall
    if not isnumber(user_input): return False
    user_input = int(user_input)
    #se etter om input er mellom 1-9
    if not grense(user_input):return False
    
    return True
    
def isnumber(user_input):
    if not user_input.isnumeric():
        print("Detter er ikke et tall")
        return False
    else: return True

def grense(user_input):
    if user_input > 9 or user_input < 1:
        print("Dette nummeret er ikke riktig")
        return False
    else: return True
    
def opptatt(koord, brett):
    rad = koord [0]
    kolonne = koord [1]
    if brett [rad][kolonne] != "-":
        print("Denne ruta er allerde valgt")
        return True
    else: return False
   
def koordinater(user_input):
    rad = int(user_input /3)
    kolonne = user_input
    if kolonne > 2: kolonne = int(kolonne % 3)
    return (rad,kolonne)

def legg_til_brett(koord, brett, active_user):
    rad = koord[0]
    kolonne = koord[1]
    brett[rad][kolonne] = active_user
    
def current_user(user):
    if user: return "x"
    else: return "o" 
    
def vunnet(user, brett):
    if check_row(user, brett): return True
    if check_kolonne(user, brett): return True
    if check_diagonal(user, brett): return True
    return False
    
def check_row(user, brett):
    for rad in brett:
        complete_row = True
        for rute in rad:
            if rute != user:
                complete_row = False
                break
        if complete_row: return True
    return False
                
def check_kolonne(user, brett):
    for kolonne in range(3):
        complete_kolonne = True
        for rad in range(3):
            if brett[rad][kolonne] != user:
                complete_kolonne = False
                break
        if complete_kolonne: return True
    return False

def check_diagonal(user, brett):
    if brett[0][0] == user and brett[1][1] == user and brett[2][2] == user: return True
    elif brett[0][2] == user and brett[1][1] == user and brett[2][0] == user: return True
    else: return False
                
    
while runder < 9:
    active_user = current_user(user)
    print_brett(brett)
    user_input = input("vennligst velg er rute mellom 1-9 eller skriv \"q\" for å avslutte:")
    if avslutt(user_input):break
    if not check_input(user_input):
        print("Prøv igjen")
        continue
    user_input = int(user_input) -1
    koord = koordinater(user_input)
    if opptatt(koord, brett):
        print("Prøv  på nytt")
        continue
    legg_til_brett(koord, brett, active_user)
    if vunnet(active_user, brett):
        print_brett(brett)
        print(f"{active_user.upper()} won!")
        break
    runder = runder + 1
    if runder == 9: print("Uavgjort!")
    user = not user
    
    #Magnus
