from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()

mensagens = []
modelo="gpt-5.1"
#modelo="gpt-4o-mini"

enc = tiktoken.encoding_for_model("gpt-5")
cliente = OpenAI(api_key=os.getenv("API_KEY"))


def executarPrompt():
    print("executarPrompt")
    total = 0

    for msg in mensagens:
        total += len(enc.encode(msg["content"]))

    print("Quantidade de tokens:", total)
    
    texto_final = ""

    print(mensagens)

    resp = cliente.chat.completions.create(
        model=modelo,
        messages=mensagens,
        stream=True
    )

    for chunk in resp:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, flush=True)
            texto_final += delta
    #print(texto_final)
    return texto_final

    '''return cliente.chat.completions.create(
        messages = mensagens,
        model = modelo,
        stream=True
    )'''

def atv1Prompt():
    atv1_msgmSistema = """Olá, Chat! Quando eu te solicitar uma ação considere que estou conduzindo uma dinâmica de descoberta 
    de um produto de software.
    """

    atv1_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar.
    """

    mensagens.append(
        {
            "role":"system",
            "content" : atv1_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv1_msgmUsuario
        }
    )

    #return executarPrompt(atv1_msgmSistema, atv1_msgmUsuario)

def atv2Prompt(apresentacao):
    atv2_msgmSistema = """A partir de agora vou lhe fornecer dados que foram coletados com base em entrevistas ou conversas informais com o cliente. 
    Considere que o software que estou construindo possui a seguinte visão de produto:""" + apresentacao + """.
    """

    atv2_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar.
    """

    mensagens.append(
        {
            "role":"system",
            "content" : atv2_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv2_msgmUsuario
        }
    )

    #return executarPrompt(atv2_msgmSistema, atv2_msgmUsuario)

def atv3Prompt(usuarios, requisitos):
    atv3_msgmSistema = """Considere que coletei as seguintes informações sobre os principais usuários e as principais ações desejadas para este sistema:
    """ 
    atv3_msgmSistema += """Usuários:
    """

    #Usuarios e Responsabilidades
    for i in range(len(usuarios)):
        
       atv3_msgmSistema += usuarios[i][0] + """ 
        """ + usuarios[i][1] + """ 
        
        """ 
    atv3_msgmSistema += """Ações:
    """

    #ações
    for i in range(len(usuarios)):
        atv3_msgmSistema += usuarios[i][0] + """ 
        """ + usuarios[i][2] + """ 
        
        """ 
    
    atv3_msgmSistema += """Requisitos Funcionais:
        """ + requisitos + """ 
        
        """ 

    atv3_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar."""

    mensagens.append(
        {
            "role":"system",
            "content" : atv3_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv3_msgmUsuario
        }
    )
    #return executarPrompt(atv3_msgmSistema, atv3_msgmUsuario)

def atv4Prompt():
    atv4_msgmSistema = """Eu vou lhe fornecer um template para a criação de histórias de usuário. Utilize-o para estruturar sua resposta,
    sempre que for solicitado a gerar o máximo de histórias de usuário possíveis.

    Tudo que está em CAPS é um placeholder. Toda vez que você gerar um texto tente encaixar em um dos placeholders 
    que eu listei. Por favor, preserve o formato exato do template geral e ao final responda com “Entendido”.

    História de Usuário X : NOME DA HISTÓRIA DE USUÁRIO 
    - História de Usuário: Como um {TIPO DE USUÁRIO},
    Eu quero {REALIZAR UMA AÇÃO},
    Para que {RESULTADO ESPERADO}."""

    atv4_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar."""
    
    mensagens.append(
        {
            "role":"system",
            "content" : atv4_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv4_msgmUsuario
        }
    )
    #return executarPrompt(atv4_msgmSistema, atv4_msgmUsuario)

def atv5Prompt():
    atv5_msgmSistema = """Eu vou lhe fornecer sete critérios de qualidade e suas definições, baseadas no framework Quality User Story (QUS) de Lucassen et al. (2016).
    O objetivo é orientar a criação de histórias de usuários bem definidas e aderentes a esses critérios. 
    Observe que as histórias devem seguir rigorosamente cada critério e é importante revisar cada uma delas para 
    garantir que estejam claramente definidas e em conformidade com todas as definições antes de considerá-las concluídas. 
    Antes de finalizar, faça uma nova revisão de cada história para assegurar a qualidade e aderência aos critérios das histórias 
    de usuários geradas.

    Critérios de Qualidade:

    1- Bem Formada: Se a história inclui pelo menos um papel (persona), que define quem está solicitando a funcionalidade e um meio (ação), que é a atividade ou funcionalidade específica que o sistema deve permitir.
    2- Atômica: Se cada história aborda uma única funcionalidade específica.
    3- Mínima: Se a história contém apenas um papel, um meio (ex: “quero abrir o mapa interativo”), e um ou mais fins, que são os objetivos que o usuário pretende alcançar usando a funcionalidade (ex: “para localizar facilmente destinos turísticos”), sem informações desnecessárias.
    4- Conceitualmente Sólida: Se o meio expressa uma funcionalidade, e os fins explicam a razão dessa funcionalidade.
    5- Não Ambígua: Se ela evita termos ou abstrações que possam gerar múltiplas interpretações.
    6- Frase Completa: Se a história é completa, bem formada e fornece contexto suficiente para ser claramente compreendida.
    7- Estimável: Se a história não denota um requisito de granulação grossa que seja difícil de planejar e priorizar.

    Orientações Adicionais: 

    Identificação de Funcionalidades: Identifique claramente qual é a tarefa ou recurso que está sendo solicitado. Certifique-se de que cada funcionalidade seja isolada e clara.
    Criação de Histórias Atômicas: Cada história deve tratar de uma única ação específica. Isso facilita o planejamento, a implementação e a estimativa.
    Ajuste da Estrutura: Se uma história inclui duas ou mais funcionalidades distintas, haverá dois ou mais verbos de ação ligados por um “e”, se houver, você pode separá-la em duas ou mais histórias separadas. Por exemplo, a história composta “Como um cliente, eu quero consultar meu saldo e sacar dinheiro, para que eu possa saber quanto tenho disponível e retirar o valor necessário”. Deverá ser divididas em:
    História Atômica 1: Como um cliente, eu quero consultar meu saldo, para que eu possa saber quanto tenho disponível.
    História Atômica 2: Como um cliente, eu quero sacar dinheiro, para que eu possa retirar o valor necessário.
    Porém outros verbos de ação podem ser considerados como fins, quando não descrevem a ação principal da história. Eles geralmente vêm após um “para” e descrevem o benefício ou propósito da ação. Por exemplo, no exemplo abaixo, “visualizar” é o verbo principal e “verificar” e “repetir” são os resultados esperados.
    História Atômica 3: Como um cliente, eu quero visualizar meu histórico de pedidos para que eu possa verificar compras passadas e repetir pedidos facilmente.
    Validação dos Critérios: Verifique se cada história atende a todos os critérios: bem-formado, atomicidade, minimalidade, solidez conceitual, não ambiguidade, frase completa e estimabilidade. Se não atender, ajuste a história até que todos os critérios sejam satisfeitos.
    Revisão e Refinamento: Após criar as histórias, revise cada uma para garantir que atenda a todos os critérios, especialmente a atomicidade. Se uma história ainda aborda múltiplas funcionalidades, divida-a em partes menores.

    """
    
    atv5_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar."""
    
    mensagens.append(
        {
            "role":"system",
            "content" : atv5_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv5_msgmUsuario
        }
    )

    #return executarPrompt(atv5_msgmSistema, atv5_msgmUsuario)

def atv6Prompt():
    atv6_msgmSistema = """Eu vou lhe fornecer alguns exemplos de histórias de usuários bem formadas para lhe auxiliar na criação das histórias. 
    Utilize-os para estruturar sua resposta, sempre que for solicitado a gerar o máximo de histórias de usuário possíveis.

    Exemplos de Histórias Bem Definidas:

    - História de Usuário Atômica 4: Criar Tarefas
    Como um gerente,
    Eu quero criar tarefas,
    Para que eu possa adicionar atividades e distribuí-las para a equipe.

    - História de Usuário Atômica 5: Atualizar Tarefas
    Como um gerente,
    Eu quero atualizar tarefas,
    Para que eu possa modificar detalhes das atividades existentes conforme necessário."""

    atv6_msgmUsuario = """Para toda e qualquer informação que eu lhe fornecer, estude, guarde e me responda única e exclusivamente:
    "Entendido" quando terminar."""
    
    mensagens.append(
        {
            "role":"system",
            "content" : atv6_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv6_msgmUsuario
        }
    )

    #return executarPrompt(atv6_msgmSistema, atv6_msgmUsuario)

def atv7Prompt():
    atv7_msgmSistema = """ Atuando como um Engenheiro de RA, com muita experiência em elicitação de requisitos. 
    Considere todas as informações que te concedi previamente sobre o produto de software 
    que estou construindo, sobre o template, critérios, orientações e exemplos que te forneci 
    para a criação de histórias de usuário."""

    atv7_msgmUsuario = """Gere de 10 a 20 histórias de usuários, por favor gere também mais histórias que considerem 
                    os aspectos adicionais que possam melhorar a experiência do usuário e a eficiência do sistema, 
                    sinalize que essas são histórias adicionais."""
    
    mensagens.append(
        {
            "role":"system",
            "content" : atv7_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv7_msgmUsuario
        }
    )

def atv8Prompt():
    atv8_msgmSistema = """ """

    atv8_msgmUsuario = """Quero que retorne as histórias de usuários 
                        no formato JSON seguindo exatamente o exemplo abaixo, retorne **somente** o JSON 
                        com as histórias de usuário, sem nenhuma explicação, frase introdutória ou comentário.

                        {
                            "historias": [
                                {
                                "id": 1,
                                "titulo": "Pesquisa de produtos",
                                "como": "um cliente",
                                "eu_quero": "realizar uma pesquisa de produtos",
                                "para_que": "eu possa encontrar o que estou procurando facilmente"
                                },
                                {
                                "id": 2,
                                "titulo": "Adicionar produtos ao carrinho",
                                "como": "um cliente",
                                "eu_quero": "adicionar produtos ao meu carrinho",
                                "para_que": "eu possa definir os itens desejados para futura compra"
                                },
                                {
                                "id": 3,
                                "titulo": "Realizar checkout",
                                "como": "um cliente",
                                "eu_quero": "realizar o checkout de minha compra",
                                "para_que": "Garantir que comprei os itens que foram adicionados ao meu carrinho"
                                },
                                ...
                            ]
                        }
                """
    
    mensagens.append(
        {
            "role":"system",
            "content" : atv8_msgmSistema
        }
    )
    mensagens.append(    
        {
            "role":"user",
            "content": atv8_msgmUsuario
        }
    )

    #return executarPrompt(atv7_msgmSistema, atv7_msgmUsuario)


def prepararPrompt(dados_form):
    mensagens.clear()
    
    print("prepararPrompt")
    apresentacao   = dados_form['apresentacao']
    usuarios       = dados_form['usuarios']
    requisitos     = dados_form['requisitos']

    atv1Prompt()
    atv2Prompt(apresentacao)
    atv3Prompt(usuarios, requisitos)
    atv4Prompt()
    atv5Prompt()
    atv6Prompt()
    atv7Prompt()
    atv8Prompt()

    res = executarPrompt()

    return res

