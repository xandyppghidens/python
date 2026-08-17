import turtle 
import math 
import random
import time

# Configuração da tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cartinha Especial")
screen.setup(width=800, height=700)
screen.tracer(0) # Controle total da animação

# Turtle para escrever o texto
writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.color("white")
writer.penup()

# Turtle para desenhar o coração
t = turtle.Turtle()
t.speed(0) 
t.hideturtle()
t.pensize(1)

colors = [
    "red", "blue", "lime", "yellow", "magenta", 
    "orange", "pink", "cyan", "purple", "white", 
    "gold", "silver", "teal", "navy", "maroon"
]

# --- 1. EFEITO DE DIGITAÇÃO DO TEXTO ---
texto = (
    "Você sempre foi muito especial pra mim\n"
    "e vai viver pra sempre em meu coração,\n"
    "pois seja como for tudo o que vivemos e sentimos foi real,\n"
    "onde a alegria estava em todos os momentos e em todos os sorrisos.\n\n"
    "Com carinho, te dedico essa cartinha especial ❤️"
)

# Posição inicial do texto (no topo da tela)
writer.goto(0, 160)

texto_acumulado = ""
for caracter in texto:
    texto_acumulado += caracter
    writer.clear()
    writer.write(
        texto_acumulado, 
        align="center", 
        font=("Segoe UI", 13, "italic")
    )
    screen.update()
    
    # Velocidade da digitação (ajuste se quiser mais rápido ou mais lento)
    if caracter in [".", ",", "\n"]:
        time.sleep(0.2) # Pausa maior em pontuações
    else:
        time.sleep(0.03)

time.sleep(0.5) # Pausa antes de começar a desenhar o coração

# --- 2. DESENHO DO CORAÇÃO ABAIXO DO TEXTO ---

escala = 9
y_offset = -120

for i in range(120):
    t.penup()
    t.goto(0, y_offset) 
    
    angle = i * (math.pi * 2) / 120
    
    x = 16 * (math.sin(angle) ** 3) * escala
    y = ((13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * escala) + y_offset
    
    c = random.choice(colors) 
    t.color(c)
    
    t.pendown()
    t.goto(x, y)
    
    for _ in range(8):
        t.forward(5)
        t.backward(5)
        t.right(45)
        
    screen.update()
    time.sleep(0.02) 
turtle.done()