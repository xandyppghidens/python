import turtle
import math
import random
import time

# --- CONFIGURAÇÃO DA TELA ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cartinha Especial")
screen.setup(width=850, height=750)
screen.tracer(0)

# Turtle para o fundo (estrelas)
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed(0)
star_turtle.penup()

# Turtle para escrever o texto
writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.color("white")
writer.penup()

# Turtle para o contorno do coração (pontos)
heart_turtle = turtle.Turtle()
heart_turtle.hideturtle()
heart_turtle.speed(0)
heart_turtle.penup()

# Turtle exclusiva para traçar a linha da rachadura
crack_turtle = turtle.Turtle()
crack_turtle.hideturtle()
crack_turtle.speed(0)
crack_turtle.color("white")
crack_turtle.pensize(2)

# --- GERAR ESTRELAS NO FUNDO ---
fundo_estrelas = []
num_estrelas_fundo = 80

for _ in range(num_estrelas_fundo):
    ex = random.randint(-400, 400)
    ey = random.randint(-600, 600)
    tamanho = random.choice([1, 2, 3])
    brilho = random.choice(["#333333", "#666666", "#999999", "#CCCCCC", "#FFFFFF"])
    fundo_estrelas.append([ex, ey, tamanho, brilho])

def desenhar_fundo(scroll_offset=0):
    """Desenha as estrelas de fundo com deslocamento do scroll."""
    star_turtle.clear()
    for x, y, tam, cor in fundo_estrelas:
        star_turtle.goto(x, y + scroll_offset)
        star_turtle.color(cor)
        star_turtle.dot(tam)

def piscar_estrelas_aleatorias():
    """Altera aleatoriamente o brilho de algumas estrelas para simular o piscar."""
    for _ in range(5):
        idx = random.randint(0, len(fundo_estrelas) - 1)
        fundo_estrelas[idx][3] = random.choice(["#222222", "#555555", "#888888", "#BBBBBB", "#FFFFFF"])

# Texto formatado sem espaços nas extremidades das quebras para perfeita centralização
texto = (
    "O destino foi cruel com a gente, pois não fomos feitos para ficar juntos\n"
    "e isso me dói saber, pois não há um dia sequer que eu não pense em você...\n"
    "Sei que é estranho dizer isso, mas tudo o que vejo quando fecho os olhos\n"
    "é uma realidade feliz onde possamos ficar juntos, sabe?...\n"
    "Eu sei que você não me ama e nunca vai amar, e está tudo bem,\n"
    "pois eu entendo cada motivo seu.\n\n"
    "Não sou o mais bonito, nem o mais forte e muito menos o mais rico,\n"
    "pois você queria um príncipe... porém a vida me fez guerreiro.\n"
    "Eu posso quebrar maldições, matar dragões,\n"
    "mas nunca carregar o peso das suas obrigações...\n"
    "Meu amor é puro como aço, fiel como a um rei,\n"
    "mas não posso ser o príncipe que sua coroa deseja,\n"
    "pois em minhas mãos há os calos da luta contra o mal do destino,\n"
    "sendo incapaz de segurar suas delicadas mãos...\n\n"
    "Te admiro de longe enquanto tenho a espada e o escudo pra te proteger,\n"
    "mas sempre me faltou a coroa para te ter. 💔\n\n"
    "Assinado: Um guerreiro que te ama, mas não pode te ter\n\n"
    "- xandy_vilela."
)

# Posições ajustadas para alinhamento e enquadramento exato
Y_TOPO_INICIAL = 260
Y_CORACAO_BASE = -260

# Rachadura ajustada ao coração
rachadura_pts = [
    (0, 30), (-6, 10), (6, -10), (-6, -30), (4, -45), (0, -60)
]

# Limitadores de Scroll ajustados (scroll_min ampliado para permitir ver tudo)
scroll_y = 0
scroll_step = 35
scroll_min = -520  # Permite rolar até o fim completo da mensagem e coração
scroll_max = 0     # Impede rolar para cima do topo inicial

estrelas_coracao = []

def redesenhar_tudo():
    """Redesenha o fundo, o texto, o coração e a rachadura em linha."""
    desenhar_fundo(scroll_y)
    
    # Redesenha texto
    writer.clear()
    writer.goto(0, Y_TOPO_INICIAL + scroll_y)
    writer.write(texto, align="center", font=("Segoe UI", 12, "italic"))
    
    # Redesenha contorno do coração P&B
    heart_turtle.clear()
    if estrelas_coracao:
        for x, y, tam, c in estrelas_coracao:
            heart_turtle.goto(x, y + Y_CORACAO_BASE + scroll_y)
            heart_turtle.color(c)
            heart_turtle.dot(tam)

    # Redesenha a linha de rachadura
    crack_turtle.clear()
    if estrelas_coracao:
        crack_turtle.penup()
        prim_x, prim_y = rachadura_pts[0]
        crack_turtle.goto(prim_x, prim_y + Y_CORACAO_BASE + scroll_y)
        crack_turtle.pendown()
        for rx, ry in rachadura_pts[1:]:
            crack_turtle.goto(rx, ry + Y_CORACAO_BASE + scroll_y)
        crack_turtle.penup()

    screen.update()

# --- 1. ANIMAR TEXTO DIGITANDO ---
texto_acumulado = ""
y_auto_scroll = 0

for caracter in texto:
    texto_acumulado += caracter
    piscar_estrelas_aleatorias()
    
    if caracter == "\n":
        y_auto_scroll -= 20 
    
    desenhar_fundo(y_auto_scroll)
    
    writer.clear()
    writer.goto(0, Y_TOPO_INICIAL + y_auto_scroll)
    writer.write(texto_acumulado, align="center", font=("Segoe UI", 12, "italic"))
    screen.update()
    
    if caracter in [".", ",", "\n", "?"]:
        time.sleep(0.08)
    else:
        time.sleep(0.015)

time.sleep(0.8)

# --- 2. GERAR CONTORNO DO CORAÇÃO ---
escala_coracao = 5
colors_pb = ["#FFFFFF", "#DDDDDD", "#AAAAAA", "#777777", "#444444"]

for i in range(100):
    angle = i * (math.pi * 2) / 100
    x = 16 * (math.sin(angle) ** 3) * escala_coracao
    y = ((13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * escala_coracao)
    
    c = random.choice(colors_pb)
    tam = random.choice([3, 4, 5])
    estrelas_coracao.append((x, y, tam, c))

# Desenha animação do contorno em pontos
for x, y, tam, c in estrelas_coracao:
    heart_turtle.goto(x, y + Y_CORACAO_BASE + y_auto_scroll)
    heart_turtle.color(c)
    heart_turtle.dot(tam)
    screen.update()
    time.sleep(0.005)

# Traça a rachadura em linha branca contínua
crack_turtle.penup()
px, py = rachadura_pts[0]
crack_turtle.goto(px, py + Y_CORACAO_BASE + y_auto_scroll)
crack_turtle.pendown()

for rx, ry in rachadura_pts[1:]:
    crack_turtle.goto(rx, ry + Y_CORACAO_BASE + y_auto_scroll)
    screen.update()
    time.sleep(0.05)

crack_turtle.penup()
time.sleep(1.0)

# --- 3. RETORNO SUAVE PARA O TOPO (Y = 0) ---
posicao_alvo = 0
passos = 30
incremento = (posicao_alvo - y_auto_scroll) / passos

for _ in range(passos):
    y_auto_scroll += incremento
    piscar_estrelas_aleatorias()
    scroll_y = y_auto_scroll
    redesenhar_tudo()
    time.sleep(0.015)

scroll_y = posicao_alvo
redesenhar_tudo()

# --- 4. LOOP INFINITO DAS ESTRELAS PISCANDO ---
def loop_infinito_estrelas():
    piscar_estrelas_aleatorias()
    redesenhar_tudo()
    screen.ontimer(loop_infinito_estrelas, 100)

# --- 5. CONTROLES DE SCROLL ---
def ajustar_scroll(delta):
    global scroll_y
    scroll_y += delta
    scroll_y = max(scroll_min, min(scroll_max, scroll_y))
    redesenhar_tudo()

def rolar_cima():
    ajustar_scroll(scroll_step)

def rolar_baixo():
    ajustar_scroll(-scroll_step)

def rolar_wheel_win10(event):
    if event.delta < 0 or event.num == 5:
        ajustar_scroll(-scroll_step)
    elif event.delta > 0 or event.num == 4:
        ajustar_scroll(scroll_step)

screen.listen()

screen.onkey(rolar_cima, "Up")
screen.onkey(rolar_baixo, "Down")
screen.onkey(rolar_cima, "w")
screen.onkey(rolar_baixo, "s")

canvas = screen.getcanvas()
canvas.bind("<MouseWheel>", rolar_wheel_win10)
canvas.bind("<Button-4>", rolar_wheel_win10)
canvas.bind("<Button-5>", rolar_wheel_win10)

loop_infinito_estrelas()

turtle.done()