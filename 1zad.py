

def Uscor():
    
    global A
    global t
    try:
        V = int(input())
        V0 = int(input())
        t = int(input())
        B = V - V0
        A = B/t
    except ValueError:
        print('Это не число. Выходим.')
    except ZeroDivisionError:
        print('Ноль нельзя.')    
    
        
    print(A)
def Dec(Uscor):
    def wrapper():    
        Uscor()
        S = (A * t *t)/2
        print(S)
    return wrapper

Uscor = Dec(Uscor)
Uscor()
