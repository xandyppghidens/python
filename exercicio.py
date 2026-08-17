import math
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class PainelCalculadora:

  def __init__(self, root):
    self.root = root
    self.root.title("Painel de Operações Matemáticas & Geometria Interativa")
    self.root.geometry("1100x780")
    self.root.minsize(950, 700)

    self.configurar_estilo()

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill="both", expand=True)

    self.notebook = ttk.Notebook(main_frame)
    self.notebook.pack(fill="both", expand=True)

    # Abas da Aplicação
    self.criar_aba_equacao_1grau()
    self.criar_aba_pitagoras()
    self.criar_aba_trigonometria()
    self.criar_aba_areas()
    self.criar_aba_bhaskara()
    self.criar_aba_graficos()
    self.criar_aba_aritmetica()
    self.criar_aba_logica()

  def configurar_estilo(self):
    style = ttk.Style()
    try:
      style.theme_use("clam")
    except:
      pass

    self.root.configure(bg="#eef2f7")
    style.configure("TNotebook", background="#eef2f7", borderwidth=0)
    style.configure(
        "TNotebook.Tab", padding=(12, 8), font=("Segoe UI", 9, "bold")
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", "#4f46e5"), ("!selected", "#dbe4f0")],
        foreground=[("selected", "white"), ("!selected", "#1f2937")],
    )

    style.configure("TFrame", background="#ffffff")
    style.configure("Card.TFrame", background="#ffffff", relief="flat")
    style.configure(
        "Title.TLabel",
        font=("Segoe UI", 15, "bold"),
        background="#ffffff",
        foreground="#1f2937",
    )
    style.configure(
        "Subtitle.TLabel",
        font=("Segoe UI", 10),
        background="#ffffff",
        foreground="#374151",
    )
    style.configure(
        "Result.TLabel",
        font=("Segoe UI", 10, "bold"),
        background="#ffffff",
        foreground="#0f172a",
    )
    style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=6)
    style.configure(
        "TLabel", font=("Segoe UI", 9), background="#ffffff", foreground="#1f2937"
    )
    style.configure("TEntry", padding=5)

  def criar_layout_split(self, titulo, subtitulo):
    aba = ttk.Frame(self.notebook, padding=10)
    self.notebook.add(aba, text=titulo)

    aba.columnconfigure(0, weight=1)
    aba.columnconfigure(1, weight=1)
    aba.rowconfigure(0, weight=1)

    card_esq = ttk.Frame(aba, style="Card.TFrame", padding=15)
    card_esq.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

    card_dir = ttk.Frame(aba, style="Card.TFrame", padding=10)
    card_dir.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

    card_dir.columnconfigure(0, weight=1)
    card_dir.rowconfigure(0, weight=1)

    ttk.Label(card_esq, text=titulo, style="Title.TLabel").grid(
        row=0, column=0, columnspan=2, sticky="w", pady=(0, 2)
    )
    if subtitulo:
      ttk.Label(card_esq, text=subtitulo, style="Subtitle.TLabel").grid(
          row=1, column=0, columnspan=2, sticky="w", pady=(0, 10)
      )

    return card_esq, card_dir

  def renderizar_canvas(self, fig, container):
    for widget in container.winfo_children():
      widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    plt.close(fig)

  # --- 1. EQUAÇÃO DO 1º GRAU (NOVA ABA) ---
  def criar_aba_equacao_1grau(self):
    card_esq, card_dir = self.criar_layout_split(
        "Equação 1º Grau", "Resolução e análise de f(x) = ax + b"
    )

    ttk.Label(card_esq, text="Coeficiente a (inclinação):").grid(
        row=2, column=0, sticky="w"
    )
    e_a = ttk.Entry(card_esq)
    e_a.grid(row=3, column=0, sticky="ew", pady=(0, 8))
    e_a.insert(0, "2")

    ttk.Label(card_esq, text="Coeficiente b (termo independente):").grid(
        row=4, column=0, sticky="w"
    )
    e_b = ttk.Entry(card_esq)
    e_b.grid(row=5, column=0, sticky="ew", pady=(0, 12))
    e_b.insert(0, "-4")

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=7, column=0, sticky="w", pady=(10, 0))

    def resolver():
      try:
        a, b = float(e_a.get()), float(e_b.get())
        if a == 0:
          if b == 0:
            res_txt = "Equação indeterminada (0x = 0): infinitas soluções."
          else:
            res_txt = "Equação impossível (0x = b): sem solução."
        else:
          x_zero = -b / a
          sinal = "Crescente" if a > 0 else "Decrescente"
          res_txt = (
              f"Zero da Função (Raiz): x = {x_zero:.2f}\n"
              f"Ponto no eixo Y: (0, {b:.2f})\n"
              f"Comportamento: Função {sinal}"
          )

        lbl_res.config(text=res_txt)

        # Gráfico isolado da reta
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        x_vals = np.linspace(-10, 10, 200)
        y_vals = a * x_vals + b

        ax.plot(
            x_vals, y_vals, color="#4f46e5", linewidth=2, label=f"y = {a}x + {b}"
        )
        ax.axhline(0, color="black", linewidth=1, linestyle="--")
        ax.axvline(0, color="black", linewidth=1, linestyle="--")

        if a != 0:
          ax.plot(
              -b / a,
              0,
              "ro",
              label=f"Raiz ({-b/a:.2f}, 0)",
              markersize=7,
          )
        ax.plot(0, b, "go", label=f"Intercepto Y (0, {b:.2f})", markersize=7)

        ax.grid(True, linestyle=":", alpha=0.6)
        ax.set_title("Gráfico da Reta", fontsize=11, fontweight="bold")
        ax.legend(fontsize=8)
        self.renderizar_canvas(fig, card_dir)

      except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")

    ttk.Button(card_esq, text="Calcular e Gerar Gráfico", command=resolver).grid(
        row=6, column=0, sticky="w"
    )

  # --- 2. PITÁGORAS ---
  def criar_aba_pitagoras(self):
    card_esq, card_dir = self.criar_layout_split(
        "Pitágoras", "Cálculo e ilustração do Triângulo Retângulo."
    )

    ttk.Label(card_esq, text="Cateto A (base):").grid(row=2, column=0, sticky="w")
    entry_c1 = ttk.Entry(card_esq)
    entry_c1.grid(row=3, column=0, sticky="ew", pady=(0, 8))

    ttk.Label(card_esq, text="Cateto B / Hipotenusa:").grid(
        row=4, column=0, sticky="w"
    )
    entry_c2 = ttk.Entry(card_esq)
    entry_c2.grid(row=5, column=0, sticky="ew", pady=(0, 12))

    lbl_resultado = ttk.Label(
        card_esq, text="Resultado: -", style="Result.TLabel"
    )
    lbl_resultado.grid(row=7, column=0, sticky="w", pady=(10, 0))

    def desenhar_triangulo(a, b, c):
      fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
      # Desenha triângulo retângulo
      ax.plot([0, a, 0, 0], [0, 0, b, 0], color="#2563eb", linewidth=2.5)
      ax.fill([0, a, 0], [0, 0, b], color="#3b82f6", alpha=0.15)

      # Textos das medidas
      ax.text(a / 2, -0.2, f"Cateto A = {a:.2f}", ha="center", fontweight="bold")
      ax.text(
          -0.2,
          b / 2,
          f"Cateto B = {b:.2f}",
          va="center",
          rotation="vertical",
          fontweight="bold",
      )
      ax.text(
          a / 2,
          b / 2,
          f"Hipotenusa = {c:.2f}",
          ha="left",
          color="#dc2626",
          fontweight="bold",
      )

      # Indicador de ângulo reto (90°)
      tamanho_box = min(a, b) * 0.1
      ax.plot(
          [0, tamanho_box, tamanho_box],
          [tamanho_box, tamanho_box, 0],
          color="black",
          linewidth=1,
      )

      ax.set_aspect("equal", "datalim")
      ax.axis("off")
      ax.set_title("Triângulo Retângulo", fontsize=11, fontweight="bold")
      self.renderizar_canvas(fig, card_dir)

    def calc_hip():
      try:
        c1, c2 = float(entry_c1.get()), float(entry_c2.get())
        hip = math.hypot(c1, c2)
        lbl_resultado.config(text=f"Hipotenusa: {hip:.2f}")
        desenhar_triangulo(c1, c2, hip)
      except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")

    def calc_cat():
      try:
        cat, hip = float(entry_c1.get()), float(entry_c2.get())
        if hip <= cat:
          messagebox.showwarning(
              "Aviso", "A hipotenusa deve ser maior que o cateto."
          )
          return
        c2 = math.sqrt(hip**2 - cat**2)
        lbl_resultado.config(text=f"Cateto restante: {c2:.2f}")
        desenhar_triangulo(cat, c2, hip)
      except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")

    btn_frame = ttk.Frame(card_esq)
    btn_frame.grid(row=6, column=0, sticky="w")
    ttk.Button(
        btn_frame, text="Calcular Hipotenusa", command=calc_hip
    ).pack(side="left", padx=(0, 5))
    ttk.Button(btn_frame, text="Calcular Cateto", command=calc_cat).pack(
        side="left"
    )

  # --- 3. TRIGONOMETRIA COM ÂNGULO E CICLO ---
  def criar_aba_trigonometria(self):
    card_esq, card_dir = self.criar_layout_split(
        "Trigonometria", "Circunferência trigonométrica com projeções."
    )

    ttk.Label(card_esq, text="Ângulo em graus (°):").grid(
        row=2, column=0, sticky="w"
    )
    entry_ang = ttk.Entry(card_esq)
    entry_ang.grid(row=3, column=0, sticky="ew", pady=(0, 12))
    entry_ang.insert(0, "45")

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=5, column=0, sticky="w", pady=(10, 0))

    def calcular():
      try:
        ang = float(entry_ang.get())
        rad = math.radians(ang)
        sen, cos = math.sin(rad), math.cos(rad)
        tan_str = (
            "Indefinida" if abs(cos) < 1e-10 else f"{math.tan(rad):.4f}"
        )

        lbl_res.config(
            text=(
                f"Seno: {sen:.4f}\nCosseno:"
                f" {cos:.4f}\nTangente: {tan_str}"
            )
        )

        # Desenhar Ciclo Trigonométrico e Ângulo
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        circle = plt.Circle(
            (0, 0), 1, color="#94a3b8", fill=False, linewidth=1.5
        )
        ax.add_patch(circle)

        # Eixos e Ponto do Ângulo
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axvline(0, color="black", linewidth=0.8)

        px, py = cos, sen
        ax.plot([0, px], [0, py], color="#1e1b4b", linewidth=2)  # Raio
        ax.plot(
            [px, px],
            [0, py],
            color="#dc2626",
            linestyle="--",
            linewidth=1.5,
            label=f"Seno = {sen:.2f}",
        )
        ax.plot(
            [0, px],
            [0, 0],
            color="#16a34a",
            linestyle="--",
            linewidth=1.5,
            label=f"Cosseno = {cos:.2f}",
        )
        ax.plot(px, py, "ro")

        # Arco do ângulo
        arc_ang = np.linspace(0, rad, 50)
        ax.plot(0.25 * np.cos(arc_ang), 0.25 * np.sin(arc_ang), color="#f59e0b")
        ax.text(
            0.35 * np.cos(rad / 2),
            0.35 * np.sin(rad / 2),
            f"{ang}°",
            color="#b45309",
            fontweight="bold",
        )

        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect("equal")
        ax.legend(loc="upper right", fontsize=8)
        ax.set_title(
            f"Circunferência Trigonométrica ({ang}°)",
            fontsize=11,
            fontweight="bold",
        )
        self.renderizar_canvas(fig, card_dir)

      except ValueError:
        messagebox.showerror("Erro", "Insira um ângulo válido.")

    ttk.Button(card_esq, text="Calcular e Desenhar Ângulo", command=calcular).grid(
        row=4, column=0, sticky="w"
    )

  # --- 4. ÁREAS E FORMAS GEOMÉTRICAS ---
  def criar_aba_areas(self):
    card_esq, card_dir = self.criar_layout_split(
        "Áreas Geométricas", "Cálculo e desenho parametrizado das figuras."
    )

    ttk.Label(card_esq, text="Medida A (Base / Lado / Raio):").grid(
        row=2, column=0, sticky="w"
    )
    entry_a = ttk.Entry(card_esq)
    entry_a.grid(row=3, column=0, sticky="ew", pady=(0, 8))

    ttk.Label(card_esq, text="Medida B (Altura - para Triângulo):").grid(
        row=4, column=0, sticky="w"
    )
    entry_b = ttk.Entry(card_esq)
    entry_b.grid(row=5, column=0, sticky="ew", pady=(0, 12))

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=7, column=0, sticky="w", pady=(10, 0))

    def desenhar_figura(tipo, a, b=0):
      fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

      if tipo == "triangulo":
        ax.plot([0, a, a / 2, 0], [0, 0, b, 0], color="#0284c7", linewidth=2)
        ax.fill([0, a, a / 2], [0, 0, b], color="#38bdf8", alpha=0.3)
        ax.text(a / 2, -0.15 * b, f"Base = {a}", ha="center", fontweight="bold")
        ax.text(
            a / 2,
            b / 2,
            f"h = {b}",
            ha="center",
            color="#0369a1",
            fontweight="bold",
        )
      elif tipo == "quadrado":
        ax.plot([0, a, a, 0, 0], [0, 0, a, a, 0], color="#16a34a", linewidth=2)
        ax.fill([0, a, a, 0], [0, 0, a, a], color="#4ade80", alpha=0.3)
        ax.text(a / 2, -0.15 * a, f"Lado = {a}", ha="center", fontweight="bold")
      elif tipo == "circulo":
        circ = plt.Circle(
            (0, 0), a, color="#ea580c", fill=True, alpha=0.2, linewidth=2
        )
        circ_border = plt.Circle((0, 0), a, color="#ea580c", fill=False, lw=2)
        ax.add_patch(circ)
        ax.add_patch(circ_border)
        ax.plot([0, a], [0, 0], color="#c2410c", linestyle="--", linewidth=1.5)
        ax.text(a / 2, 0.05 * a, f"Raio = {a}", ha="center", fontweight="bold")
        ax.set_xlim(-a * 1.2, a * 1.2)
        ax.set_ylim(-a * 1.2, a * 1.2)

      ax.set_aspect("equal", "datalim")
      ax.axis("off")
      ax.set_title(
          f"Desenho do {tipo.capitalize()}", fontsize=11, fontweight="bold"
      )
      self.renderizar_canvas(fig, card_dir)

    def calc_tri():
      try:
        a, b = float(entry_a.get()), float(entry_b.get())
        lbl_res.config(text=f"Área do Triângulo: {(a*b)/2:.2f}")
        desenhar_figura("triangulo", a, b)
      except ValueError:
        messagebox.showerror("Erro", "Preencha Base e Altura.")

    def calc_quad():
      try:
        a = float(entry_a.get())
        lbl_res.config(text=f"Área do Quadrado: {a**2:.2f}")
        desenhar_figura("quadrado", a)
      except ValueError:
        messagebox.showerror("Erro", "Preencha a Medida A (Lado).")

    def calc_circ():
      try:
        r = float(entry_a.get())
        lbl_res.config(text=f"Área do Círculo: {math.pi * (r**2):.2f}")
        desenhar_figura("circulo", r)
      except ValueError:
        messagebox.showerror("Erro", "Preencha a Medida A (Raio).")

    btn_f = ttk.Frame(card_esq)
    btn_f.grid(row=6, column=0, sticky="w")
    ttk.Button(btn_f, text="Triângulo", command=calc_tri).pack(
        side="left", padx=(0, 4)
    )
    ttk.Button(btn_f, text="Quadrado", command=calc_quad).pack(
        side="left", padx=(0, 4)
    )
    ttk.Button(btn_f, text="Círculo", command=calc_circ).pack(side="left")

  # --- 5. BHASKARA ---
  def criar_aba_bhaskara(self):
    card_esq, card_dir = self.criar_layout_split(
        "Bhaskara (2º Grau)", "Resolução da equação ax² + bx + c = 0"
    )

    ttk.Label(card_esq, text="Coeficiente a:").grid(
        row=2, column=0, sticky="w"
    )
    e_a = ttk.Entry(card_esq)
    e_a.grid(row=3, column=0, sticky="ew", pady=(0, 5))
    e_a.insert(0, "1")

    ttk.Label(card_esq, text="Coeficiente b:").grid(
        row=4, column=0, sticky="w"
    )
    e_b = ttk.Entry(card_esq)
    e_b.grid(row=5, column=0, sticky="ew", pady=(0, 5))
    e_b.insert(0, "-5")

    ttk.Label(card_esq, text="Coeficiente c:").grid(
        row=6, column=0, sticky="w"
    )
    e_c = ttk.Entry(card_esq)
    e_c.grid(row=7, column=0, sticky="ew", pady=(0, 10))
    e_c.insert(0, "6")

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=9, column=0, sticky="w", pady=(10, 0))

    def resolver():
      try:
        a, b, c = float(e_a.get()), float(e_b.get()), float(e_c.get())
        if a == 0:
          messagebox.showwarning("Aviso", "O coeficiente 'a' não pode ser 0.")
          return

        delta = b**2 - 4 * a * c
        if delta < 0:
          res_txt = f"Delta = {delta:.2f}\nSem raízes reais."
        elif delta == 0:
          x = -b / (2 * a)
          res_txt = f"Delta = 0\nRaiz única: x = {x:.2f}"
        else:
          x1 = (-b + math.sqrt(delta)) / (2 * a)
          x2 = (-b - math.sqrt(delta)) / (2 * a)
          res_txt = f"Delta = {delta:.2f}\nx1 = {x1:.2f} | x2 = {x2:.2f}"

        lbl_res.config(text=res_txt)

        # Plot de parábola
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        xv = -b / (2 * a)
        x_vals = np.linspace(xv - 5, xv + 5, 200)
        y_vals = a * (x_vals**2) + b * x_vals + c

        ax.plot(
            x_vals,
            y_vals,
            color="#2563eb",
            linewidth=2,
            label=f"{a}x² + {b}x + {c}",
        )
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="--")

        if delta >= 0:
          x1_p = (-b + math.sqrt(max(0, delta))) / (2 * a)
          x2_p = (-b - math.sqrt(max(0, delta))) / (2 * a)
          ax.plot([x1_p, x2_p], [0, 0], "ro", label="Raízes")

        ax.grid(True, linestyle=":", alpha=0.6)
        ax.set_title("Parábola da Equação", fontsize=11, fontweight="bold")
        ax.legend(fontsize=8)
        self.renderizar_canvas(fig, card_dir)

      except ValueError:
        messagebox.showerror("Erro", "Insira coeficientes válidos.")

    ttk.Button(card_esq, text="Calcular e Gerar Gráfico", command=resolver).grid(
        row=8, column=0, sticky="w"
    )

  # --- 6. GERADOR DE GRÁFICOS GERAIS ---
  def criar_aba_graficos(self):
    card_esq, card_dir = self.criar_layout_split(
        "Comparador de Gráficos", "Plote e compare funções lineares e quadráticas."
    )

    ttk.Label(card_esq, text="Coeficiente a:").grid(
        row=2, column=0, sticky="w"
    )
    e_a = ttk.Entry(card_esq)
    e_a.grid(row=3, column=0, sticky="ew", pady=(0, 5))
    e_a.insert(0, "1")

    ttk.Label(card_esq, text="Coeficiente b:").grid(
        row=4, column=0, sticky="w"
    )
    e_b = ttk.Entry(card_esq)
    e_b.grid(row=5, column=0, sticky="ew", pady=(0, 5))
    e_b.insert(0, "0")

    ttk.Label(card_esq, text="Coeficiente c:").grid(
        row=6, column=0, sticky="w"
    )
    e_c = ttk.Entry(card_esq)
    e_c.grid(row=7, column=0, sticky="ew", pady=(0, 10))
    e_c.insert(0, "0")

    def plotar(grau):
      try:
        a, b = float(e_a.get()), float(e_b.get())
        c = float(e_c.get()) if grau == 2 else 0

        x = np.linspace(-10, 10, 300)
        y = a * x + b if grau == 1 else a * (x**2) + b * x + c

        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.plot(x, y, color="#4f46e5", linewidth=2, label="f(x)")
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend()
        ax.set_title(f"Função do {grau}º Grau", fontsize=11, fontweight="bold")
        self.renderizar_canvas(fig, card_dir)

      except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")

    btn_f = ttk.Frame(card_esq)
    btn_f.grid(row=8, column=0, sticky="w")
    ttk.Button(
        btn_f, text="Gerar 1º Grau", command=lambda: plotar(1)
    ).pack(side="left", padx=(0, 5))
    ttk.Button(
        btn_f, text="Gerar 2º Grau", command=lambda: plotar(2)
    ).pack(side="left")

  # --- 7. ARITMÉTICA ---
  def criar_aba_aritmetica(self):
    card_esq, _ = self.criar_layout_split(
        "Aritmética", "Operações fundamentais da matemática."
    )

    ttk.Label(card_esq, text="Primeiro Número:").grid(
        row=2, column=0, sticky="w"
    )
    e1 = ttk.Entry(card_esq)
    e1.grid(row=3, column=0, sticky="ew", pady=(0, 8))

    ttk.Label(card_esq, text="Segundo Número:").grid(
        row=4, column=0, sticky="w"
    )
    e2 = ttk.Entry(card_esq)
    e2.grid(row=5, column=0, sticky="ew", pady=(0, 12))

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=7, column=0, sticky="w", pady=(10, 0))

    def calc(op):
      try:
        n1, n2 = float(e1.get()), float(e2.get())
        if op == "+":
          res = n1 + n2
        elif op == "-":
          res = n1 - n2
        elif op == "*":
          res = n1 * n2
        elif op == "/":
          if n2 == 0:
            messagebox.showwarning("Aviso", "Divisão por zero não permitida.")
            return
          res = n1 / n2
        lbl_res.config(text=f"Resultado: {res:.4f}")
      except ValueError:
        messagebox.showerror("Erro", "Insira dois números válidos.")

    btn_f = ttk.Frame(card_esq)
    btn_f.grid(row=6, column=0, sticky="w")
    for op in ["+", "-", "*", "/"]:
      ttk.Button(btn_f, text=op, width=5, command=lambda o=op: calc(o)).pack(
          side="left", padx=(0, 5)
      )

  # --- 8. LÓGICA ---
  def criar_aba_logica(self):
    card_esq, _ = self.criar_layout_split(
        "Operadores Lógicos", "Avaliação de algebra booleana."
    )

    v1, v2 = tk.BooleanVar(), tk.BooleanVar()

    ttk.Checkbutton(card_esq, text="Entrada A (True/False)", variable=v1).grid(
        row=2, column=0, sticky="w", pady=4
    )
    ttk.Checkbutton(card_esq, text="Entrada B (True/False)", variable=v2).grid(
        row=3, column=0, sticky="w", pady=4
    )

    lbl_res = ttk.Label(card_esq, text="Resultado: -", style="Result.TLabel")
    lbl_res.grid(row=5, column=0, sticky="w", pady=(10, 0))

    def avaliar(op):
      a, b = v1.get(), v2.get()
      if op == "NOT":
        res = f"NOT A = {not a} | NOT B = {not b}"
      elif op == "AND":
        res = f"A AND B = {a and b}"
      elif op == "OR":
        res = f"A OR B = {a or b}"
      elif op == "XOR":
        res = f"A XOR B = {a ^ b}"
      lbl_res.config(text=f"Resultado: {res}")

    btn_f = ttk.Frame(card_esq)
    btn_f.grid(row=4, column=0, sticky="w", pady=(10, 0))
    for op in ["AND", "OR", "XOR", "NOT"]:
      ttk.Button(btn_f, text=op, command=lambda o=op: avaliar(o)).pack(
          side="left", padx=(0, 5)
      )


if __name__ == "__main__":
  root = tk.Tk()
  app = PainelCalculadora(root)
  root.mainloop()