endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]
    # A FUNCTION QUE VERIFICA SE UM CÓDIGO HTTP É SUCESSO OU NÃO
    # 200 ----> TRUE
    # 400 ----> FALSE

def sucesso(codigo):
    return codigo >= 200 and codigo <= 299

    # A FUNCTION QUE VERIFICA SE TEM DOIS ERROS SEGUIDOS
    # NA LISTA DE REQUISIÇÕES(codigo http) DE UM ENDPOINT
    # [200, 200, 401, 200, 500] ----> FALSE
    # [201, 500, 502, 201, 500] ----> TRUE

def erros_seguidos(lista_req):
    for i in range(len(lista_req) - 1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i + 1]
        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

    # A FUNCTION QUE ANALISA OS ENDPOINTS
    # [200, 200, 401, 200, 500] ----> FALSE
    # [201, 500, 502, 201, 500] ----> TRUE

def analise_endpoint(lista_req):
    qtd_sucessos = 0
    for codigo in lista_req:
        if sucesso(codigo):
            qtd_sucessos += 1
    qtd_total_req = len(lista_req)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucesso = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(lista_req)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucesso > 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"
    return (qtd_sucessos, qtd_erros, percentual_sucesso , classificacao)

    # PERCORRENDO TODA A MATRIZ
qtd_maior_erro = -1
endpoint_maior_erro = ""


for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    requisicoes_endpoint = status[i]

    sucessos, erros, percentual, classicacao = analise_endpoint(requisicoes_endpoint)

    print(f"ENDPOINT: {nome_endpoint}")
    print(f"REQUISIÇÕES: {requisicoes_endpoint}")
    print(f"SUCESSO: {sucessos}")
    print(f"ERROS: {erros}")
    print(f"PERCENTUAL: {percentual}")
    print(f"CLASSIFICAÇÃO: {classicacao}")
    print("-" * 30)
    print()

    if erros > qtd_maior_erro:
        qtd_maior_erro = erros
        endpoint_maior_erro = nome_endpoint
    print(f"ENDPOINT MAIOR ERRO: {endpoint_maior_erro} ({qtd_maior_erro})")
