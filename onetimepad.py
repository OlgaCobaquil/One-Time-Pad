"""
    Olga Cobaquil, 13020
    One time pad
"""
import random
import binascii


def string_to_bits(message):
    """ ord -> unicode
        format -> binario
   
    return "".join(seven_bits(format(ord(x), 'b')) for x in message)
    """
    encoding = 'utf8'
    enc_msj = message.encode(encoding)
    #mensaje a hexadecimal 
    int_hex = int(binascii.hexlify(enc_msj),16)
    #binario del string
    str_bin = bin(int_hex)[2:]
    return str_bin.zfill(8 * ((len(str_bin) + 7) // 8))

def bits_to_string(message):
    """return ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))"""
    encoding = 'utf8'
    n = int(message, 2)
    hex_string = '%x' % n
    k = len(hex_string)
    sol = binascii.unhexlify(hex_string.zfill(k + (k & 1)))
    return sol.decode(encoding)

"""ln -> largo de la cadena"""
def one_time_pad(ln):
    return bin(random.getrandbits(ln))[2:].zfill(ln)

def xor(lista1, lista2,ln):
    result = []
    for i in range(ln):
        if (lista1[i] == lista2[i]):
            result.append('0')
        else:
            result.append('1')
    cadena = ''.join(result)
    return cadena
    
def main():
    print(" 1. Cifrar ")
    print(" 2. Descifrar")
    print(" 3. Salir")
    op = input("Ingrese la opcion que desea realizar: ")
    
    if (op == 1):
        print("\n+-----------Cifrar-----------+")
        msj = raw_input("Ingrese el mensaje a cifrar: ")
        """ Cadena en binario """
        cadena_binario = string_to_bits(msj)
        print("\nCadena Binaria: \n" + cadena_binario)
        len_binario = len(cadena_binario)   
        #print("Largo de la cadena " + str(len_binario))
        #hacer one-time-pad
        cadena_random = one_time_pad(len_binario)
        print("\nOne time pad: \n" + str(cadena_random))
        result = xor(cadena_binario, cadena_random, len_binario)
        print("\nCifrado: \n" + str(result))
        
    elif (op == 2):
        print("\n+-----------Descifrar-----------+")
        cfr = raw_input("Ingresar la cadena cifrada: ")
        in_key = raw_input("Key: ")
        tm = len(cfr)
        result = xor(cfr, in_key,tm)
        final_msj = bits_to_string(result) 
        print("\nEl mensaje es: "+ final_msj)
        
        
    elif (op == 3):
        print("Salir... adios")

main()

