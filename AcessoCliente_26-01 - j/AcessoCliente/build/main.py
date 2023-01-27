# v1.0.23.1h
import os
import json
from urllib.request import urlopen

# def getIp():
#     ip = str(input("Insira o IP de destino: "))
#     return ip

# ----- IP DOS JSON | https://www.npoint.io/docs/a5fb1c4c89523f3fb24f

def getKey(akey):
    skey = akey
    KEY = akey.upper()

    match str(KEY):
        case 'CM BAURU':
            tkey = pegaChave("CMBAURU")
            return tkey
            

        case 'CM IGARATA':
            tkey = pegaChave("CMIGARATA")
            return tkey
            

        case 'CM IPERO':
            tkey = pegaChave("CMIPERO")
            return tkey

        case 'CM ITAPETININGA':
            tkey = pegaChave("CMITAPE")
            return tkey
        
        case 'CM LUCELIA':
            tkey = pegaChave("CMLUCELIA")
            return tkey

        case 'CM MANDURI':
            tkey = pegaChave("CMMANDURI")
            return tkey

        case 'CM PARANAPANEMA':
            tkey = pegaChave("CMPARANAP")
            return tkey

        case 'IPESPEN PARANAPANEMA':
            tkey = pegaChave("IPPARANAP")
            return tkey

        case 'PM IGARATA':
            tkey = pegaChave("PMIGARATA")
            return tkey

        case 'PM ILHA COMPRIDA':
            tkey = pegaChave("PMILHA")
            return tkey

        case 'PM IPERO':
            tkey = pegaChave("PMIPERO")
            return tkey

        case 'PM ITAPETININGA':
            tkey = pegaChave("PMITAPE")
            return tkey
            

        case 'PM NOVA INDEPENDENCIA':
            tkey = pegaChave("PMNOVA")
            return tkey

        case 'PM UCHOA':
            tkey = pegaChave("PMUCHOA")
            return tkey
            
        case other:
            return skey

    # return key


def pegaChave(url):
    urla = "https://api.npoint.io/a5fb1c4c89523f3fb24f/" + url
    resposta = urlopen(urla)
    tkeya = json.loads(resposta.read())

    return tkeya


def main(ip, key, anoz, base):
    print("Iniciando a Manutenção...\n\n")
    startz = "C:\\" + base

    for dirpath, dirnames, filenames in os.walk(startz):
        for dirname in dirnames:
            if dirname == "Acesso":
                clear = lambda: os.system('cls')
                clear()
                print("Módulo de Acesso Encontrado!\n")
                path = startz + "\Acesso\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[ACESSOSISTEMA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =ACESSOSISTEMAS")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Agua":
                path = startz + "\Agua\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Água Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[AGUA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =AGUA")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            
            elif dirname == "Almoxarifado_" + str(anoz):
                print("Módulo de Almoxarifado Encontrado!\n")
                path = startz + "\Almoxarifado_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[ALMOXARIFADO]")
                    elif start == 2:
                        if dirname == "Almoxarifado_2023":
                            f.write("\n\nNomeBD =GESPUBLI2023")
                        else:
                            f.write("\n\nNomeBD =4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Agua":
                path = startz + "\Agua\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Água Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[AGUA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =AGUA")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Cemiterio_" + str(anoz):
                path = startz + "\Cemiterio_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Cemitério Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[CEMITERIO]")
                    elif start == 2:
                        f.write("\n\nNomeBD =TRIBUTOS")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")


            elif dirname == "ControleInterno_" + str(anoz):
                path = startz + "\ControleInterno_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Controle Interno Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[CINTERNO]")
                    elif start == 2:
                        if dirname == "ControleInterno_2023":
                            f.write("\n\nNomeBD =GESPUBLI2023")
                        else:
                            f.write("\n\nNomeBD =4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Frota":
                path = startz + "\Frota\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Frota Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[FROTA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =FROTA2005")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")

            elif dirname == "Tesouraria_" + str(anoz):
                path = startz + "\Tesouraria_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Tesouraria Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[TESOURARIA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =TRIBUTOS")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "ISS":
                path = startz + "\ISS\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de ISS Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[ISS]")
                    elif start == 2:
                        f.write("\n\nNomeBD =TRIBUTOS")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Patrimonio_" + str(anoz):
                path = startz + "\patrimonio_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Patrimônio Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[PATRIMONIO]")
                    elif start == 2:
                        if dirname == "Patrimonio_2023":
                            f.write("\n\nNomeBD =GESPUBLI2023")
                        else:
                            f.write("\n\nNomeBD =4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Ponto_" + str(anoz):
                path = startz + "\Ponto_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Ponto Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[PONTO]")
                    elif start == 2:
                        if dirname == "Ponto_2023":
                            f.write("\n\nNomeBD =FOLHA_PM_2023")
                        else:
                            f.write("\n\nNomeBD =4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Previdencia_" + str(anoz):
                path = startz + "\Previdencia_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Previdência Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[Previdencia]")
                    elif start == 2:
                        f.write("\n\nNomeBD =PREV" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Procuradoria":
                path = startz + "\Procuradoria\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Procuradoria Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[PROCURADORIA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =PROCURADORIA" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "Social":
                path = startz + "\Social\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Social Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[MEDICO]")
                    elif start == 2:
                        f.write("\n\nNomeBD =SOCIAL2005")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            
            

            elif dirname == "Procuradoria":
                path = startz + "\Procuradoria\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Procuradoria Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[PROCURADORIA]")
                    elif start == 2:
                        f.write("\n\nNomeBD =PROCURADORIA" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

            elif dirname == "ProntuarioEletronico":
                path = startz + "\ProntuarioEletronico\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Prontuário Eletrônico Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[MEDICO]")
                    elif start == 2:
                        f.write("\n\nNomeBD =SOCIAL2005")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            


            elif dirname == "Compras_" + str(anoz):
                path = startz + "\Compras_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Compras Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[COMPRAS]")
                    elif start == 2:
                        if dirname == "Compras_2023":
                            f.write("\n\nNomeBD =GESPUBLI2023")
                        else:
                            f.write("\n\nNomeBD =4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            
            
            elif dirname == "Contabilidade_" + str(anoz):
                path = startz + "\Contabilidade_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Contabilidade Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[CONTABILIDADE]")
                    elif start == 2:
                        if dirname == "Contabilidade_2023":
                            f.write("\n\nNomeBD =GESPUBLI2023")
                        else:
                            f.write("\n\nNomeBD = 4RSIST" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            
            
            elif dirname == "Folha_" + str(anoz):
                path = startz + "\Folha_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Folha Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[FOLHA]")
                    elif start == 2:
                        if dirname == "Folha_2023":
                            f.write("\n\nNomeBD =FOLHA_PM_2023")
                        else:
                            f.write("\n\nNomeBD =FOLHA" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")

            
            elif dirname == "IPTU":
                path = startz + "\IPTU\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de IPTU Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[IPTU]")
                    elif start == 2:
                        f.write("\n\nNomeBD =TRIBUTOS")
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            
            elif dirname == "Legislativo_" + str(anoz):
                path = startz + "\Legislativo_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Legislativo Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[LEGISLATIVO]")
                    elif start == 2:
                        f.write("\n\nNomeBD =LEGISLATIVO" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")


            elif dirname == "Protocolo_" + str(anoz):
                path = startz + "\Protocolo_" + str(anoz) + "\parametro.ini"
                os.remove(path)

                sfile = open(path, "x")
                f = open(path, "a")
                print("Módulo de Protocolo Encontrado!\n")
                
                start = 1
                end = 5

                while (start <= end):
                    if start == 1:
                        f.write("[PROTOCOLO]")
                    elif start == 2:
                        f.write("\n\nNomeBD =PROTOCOLO" + str(anoz))
                    elif start == 3:
                        f.write("\nServer =" + str(ip))
                    elif start == 4:
                        f.write("\n\nTpBD   = SQLSERVER")
                    elif start == 5:
                        f.write("\nKEY      =" + str(key))
                    start = start + 1
                f.close()
                print("Parâmetro completo.\n")
            

# if __name__ == '__main__':
#     main()
    # 832885006