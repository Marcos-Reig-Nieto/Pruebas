import utilities as util
import utilitiesB as utilB

def main():
    a = 7
    b = 5

    c = util.SumaA(a,b)

    print(f"El valor de la suma de a y b es: {c}")



    d = utilB.restaB(a,b)
    print(f"El valor de la resta de a y b es: {d}")

    #=========
    print("Hola mundo desde A")
    print("Hola mundo somos el equipo AB")

if __name__ == "__main__":
    main()

