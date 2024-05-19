while True: 
    
    # Validador de CPF
    def validar_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            print("CPF inválido. Deve conter 11 dígitos.")
            return False

        array = list(cpf)
        print("\033[1;36m", array, "\033[m")

        soma1 = 0
        k = 10

        for i in range(9):
            soma1 += int(array[i]) * k
            k -= 1

        soma2 = 0
        k = 11

        for i in range(10):
            soma2 += int(array[i]) * k
            k -= 1

        result1 = (soma1 * 10) % 11
        print(f"\033[1;35m O resultado do primeiro dígito é: {result1} \033[m")
        result2 = (soma2 * 10) % 11
        print(f"\033[1;34m O resultado do segundo dígito é: {result2} \033[m")

        if int(cpf[9]) == result1 and int(cpf[10]) == result2:
            print("\033[1;32;40m CPF é válido. \033[m")
            return True
        else:
            print("\033[1;31;40m CPF é inválido. \033[m")
            return False

    cpf1 = str(input("Digite o CPF: "))
    validar_cpf(cpf1)
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;35m Quer Continuar? [S/N]: \033[m')).strip().upper()[0]
    if resp == 'N':
        print(' \033[1;30;41m Saindo do programa.... \033[m')
        break