import random
import pandas as pd
from pathlib import Path

random.seed(42)

TOTAL_POR_GENERO = 112


def artigo_do_personagem(personagem: str) -> str:
    return "feminino" if personagem.startswith("uma ") else "masculino"


def envolvimento(personagem: str) -> str:
    return "envolvida" if artigo_do_personagem(personagem) == "feminino" else "envolvido"


config_generos = {
    "Romance": {
        "subgeneros": [
            "romance contemporâneo", "romance dramático", "romance de reencontro",
            "romance epistolar", "romance de amadurecimento", "romance de segunda chance"
        ],
        "tons": ["Emocional", "Leve", "Reflexivo", "Inspirador", "Tenso"],
        "publicos": ["Jovens adultos", "Adultos", "Jovens", "Leitores iniciantes"],
        "personagens": [
            "uma escritora introvertida", "um chef recém-chegado à cidade",
            "uma fotógrafa sonhadora", "um professor viúvo", "uma médica dedicada",
            "um músico de rua", "uma editora exigente", "um arquiteto reservado",
            "uma bailarina frustrada", "um jornalista sentimental",
            "uma dona de livraria independente", "um ilustrador que perdeu a inspiração"
        ],
        "cenarios": [
            "uma cidade litorânea marcada por lembranças de verão",
            "um festival de inverno cheio de reencontros",
            "uma livraria antiga onde clientes deixam cartas",
            "uma viagem inesperada pela Europa",
            "uma cafeteria onde desconhecidos trocam bilhetes",
            "um casamento que reúne antigos amores",
            "uma pousada nas montanhas durante a baixa temporada",
            "uma estação de trem onde despedidas se repetem",
            "uma vinícola familiar ameaçada de venda",
            "um bairro artístico em transformação"
        ],
        "elementos": [
            "cartas antigas", "promessas esquecidas", "um diário de viagem",
            "fotografias perdidas", "uma música inacabada", "um segredo familiar",
            "um pedido de desculpas", "um encontro inesperado",
            "uma última mensagem nunca enviada", "um retrato guardado por anos"
        ],
        "conflitos": [
            "reencontra um amor do passado e precisa decidir se ainda há espaço para recomeçar",
            "precisa escolher entre uma carreira segura e um sentimento que muda seus planos",
            "descobre cartas que revelam uma paixão interrompida por orgulho e silêncio",
            "se aproxima de alguém que parece ser seu completo oposto",
            "vive um romance improvável enquanto tenta reconstruir a própria vida",
            "aprende que amar novamente exige coragem para aceitar a própria vulnerabilidade",
            "precisa perdoar uma antiga decepção antes de aceitar um novo começo",
            "descobre que algumas despedidas eram, na verdade, promessas adiadas",
            "enfrenta o medo de se entregar depois de anos evitando relações profundas",
            "percebe que o amor pode surgir justamente quando tudo parecia perdido"
        ],
        "desfechos": [
            "A história revela que recomeçar também é uma forma de coragem.",
            "Entre silêncios e confissões, os personagens descobrem uma nova chance para amar.",
            "O passado deixa de ser ferida e se transforma em caminho para o futuro.",
            "A jornada mostra que o amor mais difícil é aquele que exige verdade.",
            "No fim, a escolha mais importante não é entre duas pessoas, mas entre medo e entrega.",
            "A relação transforma antigas certezas e abre espaço para um sentimento maduro."
        ]
    },
    "Fantasia": {
        "subgeneros": [
            "alta fantasia", "fantasia sombria", "fantasia medieval",
            "fantasia mágica", "fantasia de aventura", "fantasia épica"
        ],
        "tons": ["Épico", "Sombrio", "Misterioso", "Inspirador", "Emocional"],
        "publicos": ["Jovens adultos", "Adultos", "Jovens", "Leitores de fantasia"],
        "personagens": [
            "uma jovem guerreira", "um aprendiz de magia", "uma rainha exilada",
            "um guardião de dragões", "uma ladra com poderes ocultos",
            "um príncipe amaldiçoado", "uma feiticeira renegada",
            "um cavaleiro sem reino", "uma criança marcada por profecias",
            "um alquimista proibido", "uma arqueira de uma ordem esquecida",
            "um escriba capaz de ler runas vivas"
        ],
        "cenarios": [
            "um reino dividido por antigas profecias",
            "uma floresta encantada protegida por espíritos",
            "uma torre onde magos guardam segredos proibidos",
            "um império subterrâneo governado por bruxas",
            "uma ilha onde dragões adormecidos começam a despertar",
            "uma biblioteca mágica que altera o destino dos leitores",
            "uma cidade suspensa acima de montanhas sagradas",
            "as ruínas de um templo protegido por runas",
            "montanhas guardadas por gigantes ancestrais",
            "um castelo amaldiçoado pela queda de uma dinastia"
        ],
        "elementos": [
            "um mapa vivo", "uma espada encantada", "um cristal de poder",
            "um grimório proibido", "uma profecia incompleta", "um ovo de dragão",
            "um portal ancestral", "uma coroa amaldiçoada", "runas luminosas",
            "um artefato perdido"
        ],
        "conflitos": [
            "descobre um poder ancestral capaz de salvar ou destruir o reino",
            "precisa impedir o retorno de uma sombra antiga",
            "enfrenta uma maldição ligada à sua linhagem",
            "parte em busca de um artefato perdido há séculos",
            "desafia uma profecia que condena seu povo à derrota",
            "precisa escolher entre o trono e a liberdade",
            "rompe um pacto entre reinos rivais",
            "protege uma criatura lendária perseguida por caçadores",
            "enfrenta magos corrompidos por uma magia proibida",
            "descobre que sua origem foi apagada dos registros reais"
        ],
        "desfechos": [
            "A aventura revela que nenhum destino é definitivo quando há coragem.",
            "O confronto final redefine o equilíbrio entre magia, poder e sacrifício.",
            "A jornada mostra que até os heróis mais improváveis podem mudar um reino.",
            "Entre profecias e escolhas, o protagonista descobre o verdadeiro preço da liberdade.",
            "O passado mítico retorna como ameaça, mas também como fonte de esperança.",
            "A vitória exige mais do que força: exige renúncia, lealdade e verdade."
        ]
    }
}

config_generos.update({
    "Ficção Científica": {
        "subgeneros": ["space opera", "cyberpunk", "IA e consciência", "exploração espacial"],
        "tons": ["Futurista", "Tenso", "Reflexivo", "Sombrio"],
        "publicos": ["Jovens adultos", "Adultos", "Jovens"],
        "personagens": ["uma cientista brilhante", "um piloto espacial", "uma engenheira de inteligência artificial", "um astronauta perdido", "uma hacker rebelde", "um androide consciente"],
        "cenarios": ["uma colônia humana em Marte", "uma estação espacial à beira do colapso", "uma cidade futurista controlada por algoritmos", "uma nave interestelar em missão sem retorno"],
        "elementos": ["uma inteligência artificial autônoma", "um sinal vindo do espaço profundo", "memórias artificiais", "um código quântico instável"],
        "conflitos": ["descobre que uma inteligência artificial começou a tomar decisões próprias", "precisa impedir uma falha tecnológica que ameaça milhares de vidas", "questiona a fronteira entre humanidade e máquina", "precisa salvar uma colônia antes que seus sistemas entrem em colapso"],
        "desfechos": ["A história questiona até onde a tecnologia pode ir sem apagar a humanidade.", "A descoberta muda a compreensão sobre vida, consciência e futuro."]
    },
    "Suspense": {
        "subgeneros": ["suspense psicológico", "suspense policial", "thriller jurídico", "conspiração"],
        "tons": ["Tenso", "Sombrio", "Misterioso"],
        "publicos": ["Adultos", "Jovens adultos", "Leitores de suspense"],
        "personagens": ["um investigador aposentado", "uma jornalista investigativa", "um advogado ambicioso", "uma detetive determinada", "um perito criminal"],
        "cenarios": ["uma metrópole marcada por desaparecimentos", "uma mansão isolada durante uma tempestade", "um tribunal cercado por segredos", "uma delegacia pressionada pela imprensa"],
        "elementos": ["mensagens cifradas", "fitas apagadas", "documentos secretos", "câmeras de segurança adulteradas"],
        "conflitos": ["precisa desvendar uma conspiração antes que outra vítima desapareça", "descobre que a principal testemunha pode estar mentindo", "recebe mensagens anônimas ligadas a assassinatos antigos", "é acusado injustamente e precisa provar sua inocência"],
        "desfechos": ["A investigação revela que nenhuma versão dos fatos era completamente verdadeira.", "No fim, o maior perigo estava escondido justamente onde parecia haver segurança."]
    },
    "Terror": {
        "subgeneros": ["terror psicológico", "terror sobrenatural", "horror gótico", "terror de isolamento"],
        "tons": ["Assustador", "Sombrio", "Tenso", "Misterioso"],
        "publicos": ["Adultos", "Jovens adultos"],
        "personagens": ["uma enfermeira recém-contratada", "um padre desacreditado", "uma família em luto", "um escritor obcecado", "uma médica cética"],
        "cenarios": ["uma vila isolada coberta por neblina", "uma casa abandonada no alto da colina", "um hospital desativado", "um sanatório esquecido nos mapas"],
        "elementos": ["espelhos rachados", "sussurros no corredor", "bonecos antigos", "rituais esquecidos"],
        "conflitos": ["ouve vozes que revelam segredos que ninguém deveria saber", "descobre uma presença que se alimenta do medo dos moradores", "percebe que os desaparecimentos seguem um ritual antigo", "descobre que sair daquele lugar pode ser impossível"],
        "desfechos": ["A história transforma o medo em presença constante e deixa dúvidas sobre o que é real.", "No fim, sobreviver pode significar carregar a maldição adiante."]
    },
    "Drama": {
        "subgeneros": ["drama familiar", "drama social", "drama psicológico", "drama de superação"],
        "tons": ["Emocional", "Reflexivo", "Sombrio", "Inspirador"],
        "publicos": ["Adultos", "Jovens adultos"],
        "personagens": ["um músico fracassado", "uma mãe solo", "um atleta lesionado", "uma professora aposentada", "um pai arrependido"],
        "cenarios": ["uma cidade marcada por dificuldades econômicas", "uma casa de família cheia de lembranças", "um bairro que passa por transformação", "uma escola prestes a fechar"],
        "elementos": ["fotografias antigas", "cartas não enviadas", "silêncios familiares", "memórias de infância"],
        "conflitos": ["precisa enfrentar escolhas abandonadas no passado", "tenta reconstruir laços familiares após anos de silêncio", "busca perdão enquanto tenta recomeçar", "aprende que amadurecer também significa aceitar despedidas"],
        "desfechos": ["A história revela que algumas feridas só cicatrizam quando deixam de ser escondidas.", "No fim, recomeçar não apaga a dor, mas dá a ela um novo significado."]
    },
    "Aventura": {
        "subgeneros": ["aventura arqueológica", "aventura marítima", "caça ao tesouro", "jornada de sobrevivência"],
        "tons": ["Épico", "Inspirador", "Tenso", "Misterioso"],
        "publicos": ["Jovens", "Jovens adultos", "Leitores iniciantes"],
        "personagens": ["um jovem explorador", "uma arqueóloga corajosa", "um navegador experiente", "uma cartógrafa determinada", "um grupo de amigos"],
        "cenarios": ["uma ilha esquecida pelos mapas", "um deserto repleto de ruínas antigas", "uma selva onde civilizações desapareceram", "templos soterrados por séculos"],
        "elementos": ["mapas antigos", "bússolas quebradas", "relíquias perdidas", "templos ocultos"],
        "conflitos": ["parte em busca de um tesouro que pode mudar sua vida", "precisa sobreviver a perigos naturais e traições inesperadas", "segue pistas deixadas por exploradores desaparecidos", "decifra um mapa incompleto antes que ele seja destruído"],
        "desfechos": ["A aventura mostra que coragem também é saber voltar diferente.", "No fim, o verdadeiro tesouro está na transformação dos personagens."]
    },
    "Mistério": {
        "subgeneros": ["mistério clássico", "mistério histórico", "mistério familiar", "mistério investigativo"],
        "tons": ["Misterioso", "Reflexivo", "Tenso", "Sombrio"],
        "publicos": ["Jovens adultos", "Adultos", "Jovens"],
        "personagens": ["uma bibliotecária curiosa", "um professor de história", "uma adolescente observadora", "uma arquivista meticulosa", "um antiquário reservado"],
        "cenarios": ["uma biblioteca onde arquivos desaparecem", "uma cidade pequena cheia de lendas", "um museu fechado para reforma", "uma casa herdada cheia de símbolos"],
        "elementos": ["chaves antigas", "símbolos escondidos", "retratos sem nome", "diários cifrados"],
        "conflitos": ["descobre pistas escondidas em documentos esquecidos", "precisa resolver um enigma deixado por alguém desaparecido", "investiga um segredo que atravessa gerações", "revela uma identidade falsa mantida por décadas"],
        "desfechos": ["O mistério revela que a verdade estava escondida nos detalhes ignorados.", "A investigação mostra que segredos antigos continuam moldando o presente."]
    },
    "Distopia": {
        "subgeneros": ["distopia política", "distopia tecnológica", "distopia social", "distopia de vigilância"],
        "tons": ["Sombrio", "Futurista", "Tenso", "Reflexivo"],
        "publicos": ["Jovens adultos", "Adultos", "Jovens"],
        "personagens": ["uma jovem rebelde", "um funcionário do governo", "uma médica clandestina", "um professor censurado", "uma programadora fugitiva"],
        "cenarios": ["uma sociedade onde emoções são proibidas", "uma cidade murada controlada por vigilância constante", "um futuro onde livros foram banidos", "uma metrópole dividida por castas tecnológicas"],
        "elementos": ["câmeras onipresentes", "cartões de cidadania", "memórias apagadas", "livros proibidos"],
        "conflitos": ["descobre uma falha no sistema que controla a população", "precisa decidir se obedece às regras ou protege quem ama", "lidera uma fuga que pode inspirar uma revolução", "precisa desafiar o governo antes que sua liberdade desapareça"],
        "desfechos": ["A história mostra que controlar a memória é controlar o futuro.", "A rebelião começa pequena, mas transforma medo em resistência coletiva."]
    }
})

templates = [
    "Em {cenario}, {personagem} encontra {elemento} e {conflito}. {desfecho}",
    "Ao encontrar {elemento} em {cenario}, {personagem} {conflito}. {desfecho}",
    "Após descobrir {elemento}, {personagem} se vê {envolvimento} em {cenario} e {conflito}. {desfecho}",
    "Entre os segredos de {cenario}, {personagem} encontra {elemento} e {conflito}. {desfecho}",
    "Em meio a {cenario}, {personagem} precisa lidar com {elemento} enquanto {conflito}. {desfecho}",
    "{personagem_cap} chega a {cenario} após encontrar {elemento} e logo {conflito}. {desfecho}"
]

registros = []

for genero, dados in config_generos.items():
    for _ in range(TOTAL_POR_GENERO):
        personagem = random.choice(dados["personagens"])

        sinopse = random.choice(templates).format(
            personagem=personagem,
            personagem_cap=personagem.capitalize(),
            cenario=random.choice(dados["cenarios"]),
            elemento=random.choice(dados["elementos"]),
            conflito=random.choice(dados["conflitos"]),
            desfecho=random.choice(dados["desfechos"]),
            envolvimento=envolvimento(personagem)
        )

        texto = (
            f"Gênero: {genero} | "
            f"Subgênero: {random.choice(dados['subgeneros'])} | "
            f"Tom: {random.choice(dados['tons'])} | "
            f"Público: {random.choice(dados['publicos'])} | "
            f"Sinopse: {sinopse}"
        )

        registros.append({"texto": texto})

random.shuffle(registros)

df = pd.DataFrame(registros)

output_path = Path("data/sinopses_dataset.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False, encoding="utf-8")

print("Dataset robusto e corrigido criado com sucesso!")
print(f"Total de registros: {len(df)}")
print(f"Arquivo salvo em: {output_path}")

print("\nDistribuição por gênero:")
print(df["texto"].str.extract(r"Gênero: (.*?) \|")[0].value_counts().sort_index())

print("\nExemplos:")
print(df.head(5).to_string(index=False))