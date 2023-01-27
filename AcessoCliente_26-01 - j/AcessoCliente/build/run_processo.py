# v1.0.23.1h
import subprocess

def subprocesso(nome, ano, base):
    startzie = "C:\\" + base
    match nome:
        case "Acesso":
            path = startzie + "\Acesso\Acesso.exe"
            subprocess.call(path)

        case "Agua":
            path = startzie + "\Agua\Agua.exe"
            subprocess.call(path)

        case "Almoxarifado":
            path = startzie + "\Almoxarifado_" + str(ano) + "\Almoxarifado.exe"
            subprocess.call(path)

        case "Cemiterio":
            path = startzie + "\Cemiterio_" + str(ano) + "\Cemiterio.exe"
            subprocess.call(path)

        case "Compras":
            path = startzie + "\Compras_" + str(ano) + "\Compras.exe"
            subprocess.call(path)

        case "Contabilidade":
            path = startzie + "\Contabilidade_" + str(ano) + "\Contabilidade.exe"
            subprocess.call(path)

        case "Controle Interno":
            path = startzie + "\ControleInterno\CInterno.exe"
            subprocess.call(path)

        case "Folha":
            path = startzie + "\Folha_" + str(ano) + "\Folha.exe"
            subprocess.call(path)

        case "Frota":
            path = startzie + "\Frota\Frota.exe"
            subprocess.call(path)

        case "IPTU":
            path = startzie + "\IPTU\Iptu.exe"
            subprocess.call(path)

        case "ISS":
            path = startzie + "\ISS\Iss.exe"
            subprocess.call(path)

        case "Legislativo":
            path = startzie + "\Legislativo_" + str(ano) + "\Legislativo.exe"
            subprocess.call(path)

        case "Procuradoria":
            path = startzie + "\Procuradoria\Procuradoria.exe"
            subprocess.call(path)

        case "Protocolo":
            path = startzie + "\Protocolo_" + str(ano) + "\Protocolo.exe"
            subprocess.call(path)

        case "Ponto":
            path = startzie + "\Ponto_" + str(ano) + "\Ponto.exe"
            subprocess.call(path)

        case "Social":
            path = startzie + "\Social\Prefeitura.exe"
            subprocess.call(path)

        case "Tesouraria":
            path = startzie + "\Tesouraria_" + str(ano) + "\Tesouraria.exe"
            subprocess.call(path)

#subprocesso("Compras", 2023, "JLSOFT")