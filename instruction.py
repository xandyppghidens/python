import math
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ================================================================
# XANDY ACADEMY
# T.I. + MATEMÁTICA + CYBER SECURITY
# ================================================================

plt.style.use("dark_background")


class XandyAcademy:

    def __init__(self, root):
        self.root = root
        self.root.title("Xandy Academy — T.I. + Matemática + Cyber Security")
        self.root.geometry("1320x880")
        self.root.minsize(1000, 750)

        # XP: cada ferramenta/aba pode conceder XP somente uma vez.
        self.xp = 0
        self.atividades_xp = set()

        self.configurar_estilo()

        main_frame = ttk.Frame(root, padding=12)
        main_frame.pack(fill="both", expand=True)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True)

        self.notebook.bind("<<NotebookTabChanged>>", self._registrar_aba)
        self.notebook.bind("<MouseWheel>", self._rolar_abas)
        self.root.bind("<Control-Tab>", self._navegar_aba_teclado)
        self.root.bind("<Control-Shift-Tab>", self._navegar_aba_teclado)

        barra = ttk.Frame(root, style="DarkBG.TFrame")
        barra.pack(fill="x", side="bottom")

        self.xp_label = ttk.Label(
            barra,
            text="XP: 0",
            style="Subtitle.TLabel"
        )
        self.xp_label.pack(side="right", padx=15, pady=5)

        # ============================================================
        # ABAS DE T.I.
        # ============================================================

        self.criar_aba_hardware()
        self.criar_aba_redes()
        self.criar_aba_programacao()
        self.criar_aba_simulador_logica()
        self.criar_aba_poo()
        self.criar_aba_camadas_seguranca()
        self.criar_aba_ataques_defesa()
        self.criar_aba_office_bi()
        self.criar_aba_conversor_binario()
        self.criar_aba_criptografia()

        # ============================================================
        # ABAS DE MATEMÁTICA
        # ============================================================

        self.criar_aba_equacao_1grau()
        self.criar_aba_pitagoras()
        self.criar_aba_trigonometria()
        self.criar_aba_areas()
        self.criar_aba_bhaskara()
        self.criar_aba_graficos()
        self.criar_aba_aritmetica()
        self.criar_aba_logica()

        # Certificado sempre por último.
        self.criar_aba_certificado()

        # A primeira aba também conta como visitada.
        self._registrar_aba()

    # ================================================================
    # ESTILO
    # ================================================================

    def configurar_estilo(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        self.bg_dark = "#0f172a"
        self.card_bg = "#1e293b"
        self.accent_purple = "#6366f1"
        self.accent_green = "#10b981"
        self.text_light = "#f8fafc"
        self.text_muted = "#94a3b8"

        self.root.configure(bg=self.bg_dark)

        style.configure(
            "TNotebook",
            background=self.bg_dark,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            padding=(8, 7),
            font=("Segoe UI", 8, "bold")
        )

        style.map(
            "TNotebook.Tab",
            background=[
                ("selected", self.accent_purple),
                ("!selected", "#334155"),
            ],
            foreground=[
                ("selected", "#ffffff"),
                ("!selected", self.text_muted),
            ],
        )

        style.configure(
            "TFrame",
            background=self.card_bg
        )

        style.configure(
            "Card.TFrame",
            background=self.card_bg,
            relief="flat"
        )

        style.configure(
            "DarkBG.TFrame",
            background=self.bg_dark
        )

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 15, "bold"),
            background=self.card_bg,
            foreground=self.text_light,
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 9, "italic"),
            background=self.card_bg,
            foreground=self.text_muted,
        )

        style.configure(
            "Result.TLabel",
            font=("Segoe UI", 10, "bold"),
            background=self.card_bg,
            foreground=self.accent_green,
        )

        style.configure(
            "TLabel",
            font=("Segoe UI", 9.5),
            background=self.card_bg,
            foreground="#e2e8f0",
        )

        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 9, "bold"),
            background=self.accent_purple,
            foreground="#ffffff",
            padding=6,
        )

        style.map(
            "Accent.TButton",
            background=[("active", "#4f46e5")]
        )

    # ================================================================
    # LAYOUT / COMPONENTES AUXILIARES
    # ================================================================

    def criar_layout_split(self, titulo, subtitulo):
        aba = ttk.Frame(
            self.notebook,
            padding=12,
            style="DarkBG.TFrame"
        )
        self.notebook.add(aba, text=titulo)

        aba.columnconfigure(0, weight=1)
        aba.columnconfigure(1, weight=1)
        aba.rowconfigure(0, weight=1)

        card_esq = ttk.Frame(
            aba,
            style="Card.TFrame",
            padding=16
        )
        card_esq.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 6)
        )

        card_dir = ttk.Frame(
            aba,
            style="Card.TFrame",
            padding=16
        )
        card_dir.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(6, 0)
        )

        card_dir.columnconfigure(0, weight=1)
        card_dir.rowconfigure(0, weight=1)

        ttk.Label(
            card_esq,
            text=titulo,
            style="Title.TLabel"
        ).pack(
            anchor="w",
            pady=(0, 2)
        )

        if subtitulo:
            ttk.Label(
                card_esq,
                text=subtitulo,
                style="Subtitle.TLabel"
            ).pack(
                anchor="w",
                pady=(0, 12)
            )

        return card_esq, card_dir

    def renderizar_canvas(self, fig, container):
        for widget in container.winfo_children():
            widget.destroy()

        fig.patch.set_facecolor(self.card_bg)

        canvas = FigureCanvasTkAgg(
            fig,
            master=container
        )

        canvas.draw()

        canvas.get_tk_widget().grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        plt.close(fig)

    def adicionar_explicacao(self, card, texto):
        """
        Adiciona um bloco de teoria antes da parte interativa.
        """

        box = tk.Frame(
            card,
            bg=self.card_bg
        )

        box.pack(
            fill="x",
            pady=(0, 12)
        )

        tk.Label(
            box,
            text="O que você aprende",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_bg,
            fg="#38bdf8",
            anchor="w",
        ).pack(
            fill="x",
            pady=(0, 4)
        )

        tk.Label(
            box,
            text=texto,
            font=("Segoe UI", 9),
            bg=self.card_bg,
            fg=self.text_light,
            justify="left",
            anchor="w",
            wraplength=500,
        ).pack(
            fill="x"
        )

    def adicionar_separador(self, card):
        ttk.Separator(
            card,
            orient="horizontal"
        ).pack(
            fill="x",
            pady=(0, 12)
        )

    # ================================================================
    # XP E NAVEGAÇÃO
    # ================================================================

    def _registrar_aba(self, event=None):
        """
        Cada aba de conteúdo visitada pela primeira vez vale 25 XP.
        """

        try:
            indice = self.notebook.index(
                self.notebook.select()
            )

            nome = str(
                self.notebook.tab(
                    indice,
                    "text"
                )
            )

            if "Certificado" not in nome:
                self.ganhar_xp(
                    f"aba:{indice}",
                    25
                )

        except tk.TclError:
            pass

    def ganhar_xp(self, atividade, pontos=25):
        """
        Concede XP somente na primeira utilização de cada atividade.
        """

        if atividade not in self.atividades_xp:
            self.atividades_xp.add(atividade)
            self.xp += pontos

            if hasattr(self, "xp_label"):
                self.xp_label.config(
                    text=f"XP: {self.xp}"
                )

    def atualizar_xp_label(self):
        if hasattr(self, "xp_label"):
            self.xp_label.config(
                text=f"XP: {self.xp}"
            )

    def _rolar_abas(self, event):
        """
        Navegação das abas usando a roda do mouse.
        """

        try:
            atual = self.notebook.index(
                self.notebook.select()
            )

            total = len(
                self.notebook.tabs()
            )

            if event.delta < 0:
                atual = min(
                    atual + 1,
                    total - 1
                )
            else:
                atual = max(
                    atual - 1,
                    0
                )

            self.notebook.select(atual)

        except tk.TclError:
            pass

    def _navegar_aba_teclado(self, event):
        """
        Ctrl+Tab e Ctrl+Shift+Tab trocam de aba rapidamente.
        """

        try:
            atual = self.notebook.index(
                self.notebook.select()
            )

            total = len(
                self.notebook.tabs()
            )

            if event.state & 0x1:
                atual = (atual - 1) % total
            else:
                atual = (atual + 1) % total

            self.notebook.select(atual)

            return "break"

        except tk.TclError:
            return None

    # ================================================================
    # 1. HARDWARE
    # ================================================================

    def criar_aba_hardware(self):
        card, chart = self.criar_layout_split(
            "Hardware",
            "Arquitetura von Neumann e hierarquia de memória"
        )

        self.adicionar_explicacao(
            card,
            "Hardware é a parte física do computador. "
            "Nesta aba você aprende como CPU, registradores, cache, RAM, "
            "SSD, HD, placa-mãe e barramentos trabalham juntos. "
            "A CPU executa instruções e usa diferentes níveis de memória "
            "para reduzir o tempo de acesso aos dados.\n\n"
            "Na prática: quando você abre um programa, seus dados saem "
            "do armazenamento, são carregados na RAM e partes usadas com "
            "frequência podem ser mantidas em cache para acesso mais rápido."
        )

        self.adicionar_separador(card)

        txt = (
            "• CPU (Unidade Central de Processamento):\n"
            "  Executa o ciclo Busca-Decodificação-Execução. "
            "Contém ULA, unidade de controle e registradores.\n\n"

            "• Registradores:\n"
            "  Pequenas áreas de armazenamento dentro da CPU, "
            "extremamente rápidas e usadas durante a execução das instruções.\n\n"

            "• Memória Cache (L1, L2, L3):\n"
            "  Memória muito rápida usada para manter dados e instruções "
            "que podem ser necessários novamente pela CPU.\n\n"

            "• Memória RAM (DRAM):\n"
            "  Memória volátil onde ficam programas e dados em uso.\n\n"

            "• SSD / NVMe / HD:\n"
            "  Armazenamento não volátil. SSDs usam memória Flash; "
            "NVMe normalmente utiliza PCIe; HD usa discos magnéticos.\n\n"

            "• Placa-Mãe e Chipset:\n"
            "  Interligam CPU, memória, armazenamento e periféricos."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        componentes = [
            "HD SATA",
            "SSD SATA",
            "SSD NVMe",
            "RAM DDR5",
            "Cache L1",
        ]

        velocidade = [
            120,
            550,
            7000,
            64000,
            900000
        ]

        ax.barh(
            componentes,
            velocidade,
            color=[
                "#ef4444",
                "#f97316",
                "#3b82f6",
                "#10b981",
                "#6366f1"
            ]
        )

        ax.set_xscale("log")
        ax.set_xlabel(
            "Taxa de Transferência Aproximada (MB/s) - Escala Log"
        )

        ax.set_title(
            "Hierarquia de Desempenho da Memória",
            fontsize=11,
            fontweight="bold",
            color="white",
        )

        ax.grid(
            True,
            linestyle=":",
            alpha=0.3,
            color="#64748b"
        )

        ax.set_facecolor(self.card_bg)

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 2. REDES
    # ================================================================

    def criar_aba_redes(self):
        card, chart = self.criar_layout_split(
            "Redes & Protocolos",
            "Endereçamento IP, sub-redes e modelos de comunicação"
        )

        self.adicionar_explicacao(
            card,
            "Redes de computadores permitem que dispositivos troquem dados. "
            "Você vai aprender como um endereço IP identifica um dispositivo "
            "em uma rede, como máscaras separam rede e host e por que "
            "protocolos como TCP, UDP e DNS são importantes.\n\n"
            "Na prática: quando você acessa um site, o DNS ajuda a descobrir "
            "o IP do servidor, o protocolo de transporte organiza a comunicação "
            "e os equipamentos de rede encaminham os pacotes até o destino."
        )

        self.adicionar_separador(card)

        txt = (
            "• IPv4:\n"
            "  Possui 32 bits divididos em quatro octetos, como 192.168.1.15.\n\n"

            "• Máscara de Sub-rede:\n"
            "  Determina quais bits representam a rede e quais representam hosts.\n\n"

            "• TCP:\n"
            "  Protocolo orientado à conexão, com controle de entrega e "
            "Three-Way Handshake.\n\n"

            "• UDP:\n"
            "  Protocolo sem conexão, com menor sobrecarga e baixa latência.\n\n"

            "• DNS:\n"
            "  Traduz nomes de domínio em endereços IP.\n\n"

            "• OSI e TCP/IP:\n"
            "  Modelos de referência usados para organizar e compreender "
            "a comunicação em redes."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        ttk.Label(
            card,
            text="Digite um IPv4 para analisar:"
        ).pack(anchor="w")

        ent_ip = ttk.Entry(card)
        ent_ip.pack(
            fill="x",
            pady=5
        )

        ent_ip.insert(
            0,
            "192.168.1.15"
        )

        lbl_res = ttk.Label(
            card,
            text="",
            style="Result.TLabel",
            wraplength=500
        )

        lbl_res.pack(
            anchor="w",
            pady=10
        )

        def converter_ip():
            try:
                partes = ent_ip.get().strip().split(".")

                if len(partes) != 4:
                    raise ValueError

                if not all(
                    0 <= int(p) <= 255
                    for p in partes
                ):
                    raise ValueError

                bin_partes = [
                    bin(int(p))[2:].zfill(8)
                    for p in partes
                ]

                primeiro_octeto = int(
                    partes[0]
                )

                if primeiro_octeto < 128:
                    classe = "A"
                elif primeiro_octeto < 192:
                    classe = "B"
                elif primeiro_octeto < 224:
                    classe = "C"
                elif primeiro_octeto < 240:
                    classe = "D"
                else:
                    classe = "E"

                lbl_res.config(
                    text=(
                        f"Binário: {'.'.join(bin_partes)}\n"
                        f"Classe tradicional: {classe}\n"
                        f"Total: 32 bits"
                    )
                )

                self.ganhar_xp(
                    "ti:analise_ip",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Formato IPv4 inválido! "
                    "Use quatro octetos entre 0 e 255."
                )

        ttk.Button(
            card,
            text="Analisar Estrutura de IP",
            style="Accent.TButton",
            command=converter_ip,
        ).pack(anchor="w")

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.set_facecolor(self.card_bg)

        ax.scatter(
            [0],
            [0],
            color="#6366f1",
            s=800,
            zorder=3
        )

        ax.text(
            0,
            0,
            "Switch",
            color="white",
            ha="center",
            va="center",
            fontweight="bold",
            fontsize=8,
        )

        angles = np.linspace(
            0,
            2 * np.pi,
            5,
            endpoint=False
        )

        x = np.cos(angles) * 0.7
        y = np.sin(angles) * 0.7

        for i, (xi, yi) in enumerate(
            zip(x, y)
        ):
            ax.plot(
                [0, xi],
                [0, yi],
                color="#38bdf8",
                linestyle="--",
                alpha=0.7
            )

            ax.scatter(
                [xi],
                [yi],
                color="#10b981",
                s=400,
                zorder=3
            )

            ax.text(
                xi,
                yi,
                f"PC-{i + 1}",
                color="black",
                ha="center",
                va="center",
                fontweight="bold",
                fontsize=7,
            )

        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.axis("off")

        ax.set_title(
            "Topologia Física em Estrela",
            fontsize=10,
            fontweight="bold",
            color="white",
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 3. PROGRAMAÇÃO
    # ================================================================

    def criar_aba_programacao(self):
        card, chart = self.criar_layout_split(
            "Programação",
            "Algoritmos, estruturas de dados e complexidade"
        )

        self.adicionar_explicacao(
            card,
            "Programação é o processo de transformar um problema em "
            "instruções que um computador consegue executar. "
            "Você aprende conceitos que aparecem em Python, Java, C#, "
            "JavaScript, PHP e praticamente qualquer linguagem.\n\n"
            "Algoritmos descrevem os passos para resolver um problema. "
            "Estruturas de dados organizam as informações. A notação Big-O "
            "ajuda a analisar como o custo de um algoritmo cresce conforme "
            "a quantidade de dados aumenta."
        )

        self.adicionar_separador(card)

        txt = (
            "1. Variáveis e Tipagem:\n"
            "   Guardam dados que podem ser utilizados durante a execução.\n\n"

            "2. Estruturas de Dados:\n"
            "   • Listas/Vetores: coleção ordenada de elementos.\n"
            "   • Pilhas (LIFO): o último elemento inserido é o primeiro a sair.\n"
            "   • Filas (FIFO): o primeiro elemento inserido é o primeiro a sair.\n"
            "   • Dicionários/Hash: associação entre chave e valor.\n\n"

            "3. Algoritmos de Busca:\n"
            "   Busca linear: O(n).\n"
            "   Busca binária: O(log n), quando os dados estão ordenados.\n\n"

            "4. Complexidade:\n"
            "   Big-O descreve o crescimento aproximado do custo "
            "de tempo ou espaço de um algoritmo."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        n = np.linspace(
            1,
            100,
            100
        )

        ax.plot(
            n,
            np.ones_like(n),
            label="O(1)",
            color="#10b981"
        )

        ax.plot(
            n,
            np.log2(n),
            label="O(log n)",
            color="#38bdf8"
        )

        ax.plot(
            n,
            n,
            label="O(n)",
            color="#f59e0b"
        )

        ax.plot(
            n,
            n**2,
            label="O(n²)",
            color="#ef4444"
        )

        ax.set_ylim(
            0,
            100
        )

        ax.set_title(
            "Complexidade de Algoritmos (Big-O)",
            color="white"
        )

        ax.set_xlabel(
            "Tamanho da Entrada (n)"
        )

        ax.set_ylabel(
            "Operações"
        )

        ax.legend()
        ax.set_facecolor(self.card_bg)

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 4. PLAYGROUND LÓGICO
    # ================================================================

    def criar_aba_simulador_logica(self):
        card, chart = self.criar_layout_split(
            "Playground Lógico",
            "Simulação de portas lógicas"
        )

        self.adicionar_explicacao(
            card,
            "Portas lógicas são fundamentais para a eletrônica digital. "
            "Elas recebem entradas binárias e produzem uma saída de acordo "
            "com uma regra lógica. Computadores usam bilhões de operações "
            "desse tipo para processar informações.\n\n"
            "AND exige que as duas entradas sejam verdadeiras. OR exige "
            "pelo menos uma. XOR retorna verdadeiro quando as entradas são "
            "diferentes."
        )

        self.adicionar_separador(card)

        var_a = tk.BooleanVar(value=True)
        var_b = tk.BooleanVar(value=False)

        ttk.Checkbutton(
            card,
            text="Entrada A (TRUE/FALSE)",
            variable=var_a
        ).pack(
            anchor="w",
            pady=2
        )

        combo_op = ttk.Combobox(
            card,
            values=[
                "AND",
                "OR",
                "XOR"
            ],
            state="readonly"
        )

        combo_op.pack(
            anchor="w",
            pady=5
        )

        combo_op.current(0)

        ttk.Checkbutton(
            card,
            text="Entrada B (TRUE/FALSE)",
            variable=var_b
        ).pack(
            anchor="w",
            pady=2
        )

        lbl_res = ttk.Label(
            card,
            text="",
            style="Result.TLabel"
        )

        lbl_res.pack(
            anchor="w",
            pady=10
        )

        def avaliar():
            a = var_a.get()
            b = var_b.get()
            op = combo_op.get()

            if op == "AND":
                res = a and b
            elif op == "OR":
                res = a or b
            else:
                res = a ^ b

            lbl_res.config(
                text=f"Resultado: {res}"
            )

            self.ganhar_xp(
                "ti:playground_logico",
                25
            )

        ttk.Button(
            card,
            text="Avaliar Lógica",
            style="Accent.TButton",
            command=avaliar
        ).pack(anchor="w")

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.set_facecolor(
            self.card_bg
        )

        table_data = [
            ["0", "0", "0", "0"],
            ["0", "1", "0", "1"],
            ["1", "0", "0", "1"],
            ["1", "1", "1", "1"],
        ]

        t = ax.table(
            cellText=table_data,
            colLabels=[
                "A",
                "B",
                "A AND B",
                "A OR B"
            ],
            loc="center",
            cellLoc="center",
        )

        t.scale(
            1.2,
            1.8
        )

        for key, cell in t.get_celld().items():
            cell.set_facecolor("#334155")
            cell.set_text_props(
                color="white",
                fontweight="bold"
            )

        ax.axis("off")

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 5. POO
    # ================================================================

    def criar_aba_poo(self):
        card, chart = self.criar_layout_split(
            "POO",
            "Os 4 pilares da Orientação a Objetos"
        )

        self.adicionar_explicacao(
            card,
            "Programação Orientada a Objetos organiza sistemas usando "
            "classes e objetos. Um objeto representa uma entidade com "
            "estado e comportamento.\n\n"
            "Os quatro pilares são encapsulamento, herança, polimorfismo "
            "e abstração. Eles ajudam a construir sistemas maiores com "
            "mais organização, reutilização e separação de responsabilidades."
        )

        self.adicionar_separador(card)

        txt = (
            "• Encapsulamento:\n"
            "  Protege e organiza o estado interno de um objeto.\n\n"

            "• Herança:\n"
            "  Permite criar classes especializadas a partir de outra classe.\n\n"

            "• Polimorfismo:\n"
            "  Permite tratar objetos diferentes por uma interface comum, "
            "com comportamentos específicos.\n\n"

            "• Abstração:\n"
            "  Esconde detalhes desnecessários e apresenta uma interface "
            "mais simples para utilização."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.set_facecolor(
            self.card_bg
        )

        ax.text(
            0.5,
            0.8,
            "Classe Pai: Veiculo\n[acelerar()]",
            ha="center",
            bbox=dict(
                boxstyle="round",
                facecolor="#6366f1",
                alpha=0.8
            ),
            color="white",
            fontweight="bold",
        )

        ax.text(
            0.2,
            0.3,
            "Carro\n[acelerar()]",
            ha="center",
            bbox=dict(
                boxstyle="round",
                facecolor="#10b981",
                alpha=0.8
            ),
            color="white",
            fontweight="bold",
        )

        ax.text(
            0.8,
            0.3,
            "Moto\n[acelerar()]",
            ha="center",
            bbox=dict(
                boxstyle="round",
                facecolor="#10b981",
                alpha=0.8
            ),
            color="white",
            fontweight="bold",
        )

        ax.annotate(
            "",
            xy=(0.5, 0.72),
            xytext=(0.2, 0.42),
            arrowprops=dict(
                arrowstyle="<-",
                color="white",
                lw=2
            ),
        )

        ax.annotate(
            "",
            xy=(0.5, 0.72),
            xytext=(0.8, 0.42),
            arrowprops=dict(
                arrowstyle="<-",
                color="white",
                lw=2
            ),
        )

        ax.set_xlim(
            0,
            1
        )

        ax.set_ylim(
            0,
            1
        )

        ax.axis("off")

        ax.set_title(
            "Diagrama de Herança & Polimorfismo",
            color="white"
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 6. SEGURANÇA
    # ================================================================

    def criar_aba_camadas_seguranca(self):
        card, chart = self.criar_layout_split(
            "Segurança",
            "Defesa em Profundidade"
        )

        self.adicionar_explicacao(
            card,
            "Cyber Security não depende de uma única barreira. "
            "A ideia de Defesa em Profundidade é utilizar controles "
            "em diferentes níveis para dificultar um ataque e reduzir "
            "o impacto caso uma camada seja comprometida.\n\n"
            "Uma estratégia pode combinar segurança física, controle de "
            "acesso, firewall, segmentação de rede, proteção de endpoints, "
            "segurança de aplicações, criptografia, backups e monitoramento."
        )

        self.adicionar_separador(card)

        txt = (
            "Camadas de proteção:\n\n"
            "• Física: protege equipamentos e instalações.\n"
            "• Perímetro: controla conexões externas.\n"
            "• Rede: segmentação, firewall e monitoramento.\n"
            "• Host: proteção do sistema operacional e endpoint.\n"
            "• Aplicação: validação, autenticação e correção de vulnerabilidades.\n"
            "• Dados: controle de acesso, criptografia e backup.\n"
            "• Humano: treinamento e conscientização."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.pie(
            [1, 2, 3, 4, 5, 6],
            labels=[
                "Humano",
                "Dados",
                "Aplicação",
                "Host",
                "Rede",
                "Física"
            ],
            colors=[
                "#ef4444",
                "#f97316",
                "#f59e0b",
                "#10b981",
                "#06b6d4",
                "#6366f1",
            ],
            startangle=90,
            wedgeprops=dict(
                width=0.4,
                edgecolor=self.card_bg
            ),
        )

        ax.set_title(
            "Defesa em Camadas",
            color="white"
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 7. ATAQUES E DEFESA
    # ================================================================

    def criar_aba_ataques_defesa(self):
        card, chart = self.criar_layout_split(
            "Ataques & Defesa",
            "Análise de ameaças e medidas defensivas"
        )

        self.adicionar_explicacao(
            card,
            "Nesta área você conhece categorias comuns de ameaças "
            "e entende, de forma defensiva, como elas podem ser reduzidas. "
            "O objetivo é aprender a reconhecer riscos e aplicar controles "
            "de segurança.\n\n"
            "Phishing explora engenharia social; ransomware tenta impedir "
            "o acesso aos dados; brute-force testa muitas combinações; "
            "SQL Injection explora entradas não tratadas em aplicações; "
            "XSS envolve a execução de conteúdo não confiável no navegador."
        )

        self.adicionar_separador(card)

        txt = (
            "Ameaças comuns:\n\n"
            "• Phishing: engenharia social para induzir a vítima ao erro.\n"
            "• Ransomware: malware que pode bloquear ou criptografar dados.\n"
            "• Brute-Force: tentativa sistemática de credenciais.\n"
            "• SQL Injection: exploração de entradas para manipular consultas.\n"
            "• XSS: injeção de conteúdo que pode ser interpretado pelo navegador.\n\n"
            "Defesas importantes incluem MFA, senhas fortes, atualização de "
            "sistemas, validação de entradas, parametrização de consultas, "
            "backup, monitoramento e conscientização."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.plot(
            [4, 6, 8, 10, 12, 14],
            [0.0001, 0.01, 2.5, 300, 31000, 3000000],
            marker="o",
            color="#ef4444",
        )

        ax.set_yscale("log")

        ax.set_xlabel(
            "Comprimento da Senha"
        )

        ax.set_ylabel(
            "Tempo de Quebra Estimado (Log)"
        )

        ax.set_title(
            "Impacto do Tamanho da Senha",
            color="white"
        )

        ax.set_facecolor(
            self.card_bg
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 8. OFFICE & BI
    # ================================================================

    def criar_aba_office_bi(self):
        card, chart = self.criar_layout_split(
            "Office & BI",
            "Produtividade e análise de dados"
        )

        self.adicionar_explicacao(
            card,
            "Ferramentas de Office e Business Intelligence são muito usadas "
            "em ambientes administrativos, financeiros e corporativos. "
            "Excel pode ser usado para fórmulas, tabelas, Power Query e "
            "modelos de dados. Power BI transforma dados em relatórios "
            "e dashboards interativos.\n\n"
            "O objetivo não é apenas criar planilhas bonitas: é transformar "
            "dados brutos em informação útil para análise e tomada de decisão."
        )

        self.adicionar_separador(card)

        txt = (
            "• Excel:\n"
            "  Fórmulas, tabelas, gráficos, Power Query e análise de dados.\n\n"

            "• Power Query:\n"
            "  Importação, limpeza e transformação de dados.\n\n"

            "• DAX:\n"
            "  Linguagem utilizada para medidas e cálculos em modelos de dados.\n\n"

            "• Power BI:\n"
            "  Criação de dashboards, relatórios e visualizações interativas.\n\n"

            "• Word e PowerPoint:\n"
            "  Produção e apresentação de documentos e informações."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        meses = [
            "Jan",
            "Fev",
            "Mar",
            "Abr",
            "Mai"
        ]

        vendas = [
            15,
            24,
            30,
            45,
            60
        ]

        ax.bar(
            meses,
            vendas,
            color="#38bdf8"
        )

        ax.set_title(
            "Dashboard de Vendas - BI",
            color="white"
        )

        ax.set_ylabel(
            "Vendas"
        )

        ax.set_facecolor(
            self.card_bg
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 9. LABORATÓRIO BINÁRIO
    # ================================================================

    def criar_aba_conversor_binario(self):
        card, chart = self.criar_layout_split(
            "Laboratório Binário",
            "Conversor bidirecional Texto <-> Binário"
        )

        self.adicionar_explicacao(
            card,
            "Computadores trabalham internamente com informação representada "
            "em bits, normalmente 0 e 1. Um byte possui 8 bits. "
            "Nesta ferramenta você pode observar uma representação binária "
            "de caracteres usando seus valores numéricos.\n\n"
            "Exemplo: na tabela ASCII, a letra A corresponde ao decimal 65 "
            "e pode ser representada por 01000001 em 8 bits."
        )

        self.adicionar_separador(card)

        ttk.Label(
            card,
            text="Digite a entrada (Texto claro ou código Binário):"
        ).pack(
            anchor="w"
        )

        ent_input = ttk.Entry(card)
        ent_input.pack(
            fill="x",
            pady=6
        )

        ent_input.insert(
            0,
            "Texto Exemplo"
        )

        txt_resultado = tk.Text(
            card,
            height=8,
            bg="#0f172a",
            fg="#10b981",
            font=("Consolas", 10),
            wrap="word",
        )

        txt_resultado.pack(
            fill="x",
            pady=5
        )

        def texto_para_binario():
            texto = ent_input.get()

            if not texto:
                return

            res = " ".join(
                format(
                    ord(char),
                    "08b"
                )
                for char in texto
            )

            txt_resultado.delete(
                "1.0",
                tk.END
            )

            txt_resultado.insert(
                tk.END,
                res
            )

            self.ganhar_xp(
                "ti:texto_binario",
                25
            )

        def binario_para_texto():
            bin_str = ent_input.get().strip()

            if not bin_str:
                return

            try:
                if " " in bin_str:
                    lista_bytes = bin_str.split()
                else:
                    if len(bin_str) % 8 != 0:
                        raise ValueError

                    lista_bytes = [
                        bin_str[i:i + 8]
                        for i in range(
                            0,
                            len(bin_str),
                            8
                        )
                    ]

                if not all(
                    len(b) == 8 and
                    set(b) <= {"0", "1"}
                    for b in lista_bytes
                ):
                    raise ValueError

                res = "".join(
                    chr(int(b, 2))
                    for b in lista_bytes
                )

                txt_resultado.delete(
                    "1.0",
                    tk.END
                )

                txt_resultado.insert(
                    tk.END,
                    res
                )

                self.ganhar_xp(
                    "ti:binario_texto",
                    25
                )

            except Exception:
                messagebox.showerror(
                    "Erro de Formatação",
                    "Insira bytes binários válidos de 8 bits."
                )

        btn_frame = ttk.Frame(card)
        btn_frame.pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            btn_frame,
            text="Texto -> Binário",
            style="Accent.TButton",
            command=texto_para_binario,
        ).pack(
            side="left",
            padx=(0, 5)
        )

        ttk.Button(
            btn_frame,
            text="Binário -> Texto",
            style="Accent.TButton",
            command=binario_para_texto,
        ).pack(
            side="left"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.set_facecolor(
            self.card_bg
        )

        ascii_data = [
            ["A", "65", "01000001"],
            ["B", "66", "01000010"],
            ["a", "97", "01100001"],
            ["0", "48", "00110000"],
        ]

        t = ax.table(
            cellText=ascii_data,
            colLabels=[
                "Char",
                "Dec",
                "Binário"
            ],
            loc="center",
            cellLoc="center",
        )

        t.scale(
            1.2,
            1.8
        )

        for key, cell in t.get_celld().items():
            cell.set_facecolor("#334155")
            cell.set_text_props(
                color="white",
                fontweight="bold"
            )

        ax.axis("off")

        ax.set_title(
            "Exemplos ASCII",
            color="white"
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # 10. CRIPTOGRAFIA
    # ================================================================

    def criar_aba_criptografia(self):
        card, chart = self.criar_layout_split(
            "Criptografia",
            "Simétrica, assimétrica e hashing"
        )

        self.adicionar_explicacao(
            card,
            "Criptografia protege informações usando algoritmos matemáticos "
            "e chaves. Na criptografia simétrica, a mesma chave é usada "
            "para cifrar e decifrar. Na assimétrica, existe um par de "
            "chaves relacionadas. Hashing é diferente: uma função hash "
            "produz uma representação de tamanho fixo e não deve ser "
            "tratada como um método reversível de criptografia.\n\n"
            "Na prática, sistemas reais combinam essas técnicas. "
            "Por exemplo, conexões seguras podem usar criptografia assimétrica "
            "durante a negociação e criptografia simétrica para os dados."
        )

        self.adicionar_separador(card)

        txt = (
            "• Criptografia Simétrica:\n"
            "  Usa a mesma chave para cifrar e decifrar.\n"
            "  Exemplo: AES.\n\n"

            "• Criptografia Assimétrica:\n"
            "  Usa um par de chaves, normalmente pública e privada.\n"
            "  Exemplos: RSA e criptografia baseada em curvas elípticas.\n\n"

            "• Hash:\n"
            "  Função unidirecional usada para integridade e outros fins.\n"
            "  Exemplo: SHA-256.\n\n"

            "• Senhas:\n"
            "  Sistemas modernos devem armazenar senhas com funções de "
            "derivação de chave apropriadas e salt, em vez de texto puro."
        )

        ttk.Label(
            card,
            text=txt,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 4),
            dpi=100
        )

        ax.bar(
            [
                "Hash",
                "Simétrica",
                "Assimétrica"
            ],
            [
                1,
                3,
                85
            ],
            color=[
                "#10b981",
                "#3b82f6",
                "#ef4444"
            ]
        )

        ax.set_ylabel(
            "Custo Computacional"
        )

        ax.set_title(
            "Comparação Conceitual de Custo",
            color="white"
        )

        ax.set_facecolor(
            self.card_bg
        )

        self.renderizar_canvas(
            fig,
            chart
        )

    # ================================================================
    # MATEMÁTICA — EQUAÇÃO DE 1º GRAU
    # ================================================================

    def criar_aba_equacao_1grau(self):
        card, chart = self.criar_layout_split(
            "Equação 1º Grau",
            "Entenda f(x) = ax + b e veja a reta mudar."
        )

        self.adicionar_explicacao(
            card,
            "Uma equação do 1º grau pode ser escrita como f(x) = ax + b. "
            "O coeficiente a controla a inclinação da reta e b indica "
            "onde ela cruza o eixo Y. A raiz é o valor de x para o qual "
            "f(x) = 0."
        )

        self.adicionar_separador(card)

        tk.Label(
            card,
            text="Coeficiente a (inclinação):",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        e_a = ttk.Entry(card)
        e_a.pack(
            fill="x",
            pady=(3, 8)
        )
        e_a.insert(
            0,
            "2"
        )

        tk.Label(
            card,
            text="Coeficiente b (termo independente):",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        e_b = ttk.Entry(card)
        e_b.pack(
            fill="x",
            pady=(3, 10)
        )
        e_b.insert(
            0,
            "-4"
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def resolver():
            try:
                a = float(e_a.get())
                b = float(e_b.get())

                if a == 0:
                    resultado.config(
                        text="Se a = 0, não temos uma função de 1º grau."
                    )
                    return

                raiz = -b / a

                comportamento = (
                    "crescente"
                    if a > 0
                    else "decrescente"
                )

                resultado.config(
                    text=(
                        f"Raiz: x = {raiz:.2f}\n"
                        f"Intercepto Y: (0, {b:.2f})\n"
                        f"A função é {comportamento}."
                    )
                )

                x = np.linspace(
                    -10,
                    10,
                    300
                )

                y = a * x + b

                fig, ax = plt.subplots(
                    figsize=(5, 4),
                    dpi=100
                )

                ax.plot(
                    x,
                    y,
                    linewidth=2,
                    label=f"f(x) = {a:g}x + {b:g}"
                )

                ax.axhline(
                    0,
                    color="black",
                    linewidth=1,
                    linestyle="--"
                )

                ax.axvline(
                    0,
                    color="black",
                    linewidth=1,
                    linestyle="--"
                )

                ax.scatter(
                    [raiz],
                    [0],
                    label=f"Raiz = {raiz:.2f}"
                )

                ax.scatter(
                    [0],
                    [b],
                    label=f"Y = {b:.2f}"
                )

                ax.grid(
                    True,
                    linestyle=":",
                    alpha=.5
                )

                ax.legend(
                    fontsize=8
                )

                ax.set_title(
                    "Gráfico da função de 1º grau"
                )

                self.renderizar_canvas(
                    fig,
                    chart
                )

                self.ganhar_xp(
                    "matematica:equacao",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite números válidos."
                )

        ttk.Button(
            card,
            text="Calcular e gerar gráfico",
            style="Accent.TButton",
            command=resolver
        ).pack(anchor="w")

    # ================================================================
    # MATEMÁTICA — PITÁGORAS
    # ================================================================

    def criar_aba_pitagoras(self):
        card, chart = self.criar_layout_split(
            "Pitágoras",
            "Triângulo retângulo: a² + b² = c²."
        )

        self.adicionar_explicacao(
            card,
            "No Teorema de Pitágoras, a soma dos quadrados dos catetos "
            "é igual ao quadrado da hipotenusa: a² + b² = c². "
            "A hipotenusa é o lado oposto ao ângulo de 90° e é sempre "
            "o maior lado do triângulo."
        )

        self.adicionar_separador(card)

        tk.Label(
            card,
            text="Cateto A:",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        a = ttk.Entry(card)
        a.pack(
            fill="x",
            pady=(3, 8)
        )
        a.insert(
            0,
            "3"
        )

        tk.Label(
            card,
            text="Cateto B / Hipotenusa:",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        b = ttk.Entry(card)
        b.pack(
            fill="x",
            pady=(3, 10)
        )
        b.insert(
            0,
            "4"
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def desenhar(x, y, h):
            fig, ax = plt.subplots(
                figsize=(5, 4),
                dpi=100
            )

            ax.plot(
                [0, x, 0, 0],
                [0, 0, y, 0],
                linewidth=2.5
            )

            ax.fill(
                [0, x, 0],
                [0, 0, y],
                alpha=.15
            )

            ax.text(
                x / 2,
                -max(y * .05, .1),
                f"A = {x:.2f}",
                ha="center",
                fontweight="bold"
            )

            ax.text(
                -max(x * .05, .1),
                y / 2,
                f"B = {y:.2f}",
                va="center",
                rotation="vertical",
                fontweight="bold"
            )

            ax.text(
                x * .55,
                y * .55,
                f"C = {h:.2f}",
                fontweight="bold"
            )

            ax.set_aspect(
                "equal",
                "datalim"
            )

            ax.axis("off")

            ax.set_title(
                "Triângulo Retângulo"
            )

            self.renderizar_canvas(
                fig,
                chart
            )

        def calc_hip():
            try:
                x = float(a.get())
                y = float(b.get())

                if x <= 0 or y <= 0:
                    raise ValueError

                h = math.hypot(
                    x,
                    y
                )

                resultado.config(
                    text=(
                        f"Hipotenusa = {h:.2f}\n"
                        f"Fórmula: √({x:g}² + {y:g}²)"
                    )
                )

                desenhar(
                    x,
                    y,
                    h
                )

                self.ganhar_xp(
                    "matematica:pitagoras",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite dois catetos positivos."
                )

        def calc_cat():
            try:
                x = float(a.get())
                h = float(b.get())

                if x <= 0 or h <= x:
                    raise ValueError

                y = math.sqrt(
                    h * h - x * x
                )

                resultado.config(
                    text=(
                        f"Cateto restante = {y:.2f}\n"
                        f"Fórmula: √({h:g}² - {x:g}²)"
                    )
                )

                desenhar(
                    x,
                    y,
                    h
                )

                self.ganhar_xp(
                    "matematica:pitagoras",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "A hipotenusa deve ser maior que o cateto."
                )

        f = ttk.Frame(card)
        f.pack(
            anchor="w",
            pady=4
        )

        ttk.Button(
            f,
            text="Calcular Hipotenusa",
            command=calc_hip
        ).pack(
            side="left",
            padx=(0, 5)
        )

        ttk.Button(
            f,
            text="Calcular Cateto",
            command=calc_cat
        ).pack(
            side="left"
        )

    # ================================================================
    # MATEMÁTICA — TRIGONOMETRIA
    # ================================================================

    def criar_aba_trigonometria(self):
        card, chart = self.criar_layout_split(
            "Trigonometria",
            "Seno, cosseno, tangente e circunferência trigonométrica."
        )

        self.adicionar_explicacao(
            card,
            "Na circunferência unitária, para um ângulo θ, o ponto "
            "possui coordenadas (cos θ, sen θ). A tangente é sen θ / cos θ "
            "quando cos θ não é zero. O gráfico ajuda a visualizar "
            "essas relações geometricamente."
        )

        self.adicionar_separador(card)

        tk.Label(
            card,
            text="Ângulo em graus:",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        ang = ttk.Entry(card)
        ang.pack(
            fill="x",
            pady=(3, 10)
        )
        ang.insert(
            0,
            "45"
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def calcular():
            try:
                graus = float(
                    ang.get()
                )

                rad = math.radians(
                    graus
                )

                sen = math.sin(rad)
                cos = math.cos(rad)

                tang = (
                    "indefinida"
                    if abs(cos) < 1e-10
                    else f"{math.tan(rad):.4f}"
                )

                resultado.config(
                    text=(
                        f"sen = {sen:.4f}\n"
                        f"cos = {cos:.4f}\n"
                        f"tan = {tang}"
                    )
                )

                fig, ax = plt.subplots(
                    figsize=(5, 4),
                    dpi=100
                )

                circle = plt.Circle(
                    (0, 0),
                    1,
                    fill=False,
                    linewidth=1.5
                )

                ax.add_patch(circle)

                ax.axhline(
                    0,
                    color="black",
                    linewidth=.8
                )

                ax.axvline(
                    0,
                    color="black",
                    linewidth=.8
                )

                px = cos
                py = sen

                ax.plot(
                    [0, px],
                    [0, py],
                    linewidth=2,
                    label="raio"
                )

                ax.plot(
                    [px, px],
                    [0, py],
                    "--",
                    linewidth=1.5,
                    label=f"sen = {sen:.2f}"
                )

                ax.plot(
                    [0, px],
                    [0, 0],
                    "--",
                    linewidth=1.5,
                    label=f"cos = {cos:.2f}"
                )

                ax.scatter(
                    [px],
                    [py]
                )

                ax.text(
                    px,
                    py,
                    f"  {graus:g}°"
                )

                arc = np.linspace(
                    0,
                    rad,
                    80
                )

                ax.plot(
                    .25 * np.cos(arc),
                    .25 * np.sin(arc),
                    linewidth=1.5
                )

                ax.set_xlim(
                    -1.3,
                    1.3
                )

                ax.set_ylim(
                    -1.3,
                    1.3
                )

                ax.set_aspect(
                    "equal"
                )

                ax.legend(
                    fontsize=8
                )

                ax.set_title(
                    f"Circunferência — {graus:g}°"
                )

                self.renderizar_canvas(
                    fig,
                    chart
                )

                self.ganhar_xp(
                    "matematica:trigonometria",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite um ângulo válido."
                )

        ttk.Button(
            card,
            text="Calcular e desenhar",
            style="Accent.TButton",
            command=calcular
        ).pack(
            anchor="w"
        )

    # ================================================================
    # MATEMÁTICA — ÁREAS
    # ================================================================

    def criar_aba_areas(self):
        card, chart = self.criar_layout_split(
            "Áreas",
            "Triângulo, quadrado e círculo com desenho automático."
        )

        self.adicionar_explicacao(
            card,
            "Área mede a superfície ocupada por uma figura. "
            "Triângulo: A = base × altura / 2. "
            "Quadrado: A = lado². "
            "Círculo: A = πr².\n\n"
            "A ferramenta calcula o valor e desenha a figura correspondente "
            "para relacionar a fórmula com sua representação geométrica."
        )

        self.adicionar_separador(card)

        tk.Label(
            card,
            text="Medida A (base, lado ou raio):",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        ea = ttk.Entry(card)
        ea.pack(
            fill="x",
            pady=(3, 8)
        )
        ea.insert(
            0,
            "5"
        )

        tk.Label(
            card,
            text="Medida B (altura do triângulo):",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        eb = ttk.Entry(card)
        eb.pack(
            fill="x",
            pady=(3, 10)
        )
        eb.insert(
            0,
            "3"
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold")
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def desenhar(tipo, x, y=0):
            fig, ax = plt.subplots(
                figsize=(5, 4),
                dpi=100
            )

            if tipo == "triangulo":
                ax.fill(
                    [0, x, x / 2],
                    [0, 0, y],
                    alpha=.25
                )

                ax.plot(
                    [0, x, x / 2, 0],
                    [0, 0, y, 0],
                    linewidth=2
                )

                ax.text(
                    x / 2,
                    y / 2,
                    f"h = {y:g}",
                    ha="center",
                    fontweight="bold"
                )

            elif tipo == "quadrado":
                ax.fill(
                    [0, x, x, 0],
                    [0, 0, x, x],
                    alpha=.25
                )

                ax.plot(
                    [0, x, x, 0, 0],
                    [0, 0, x, x, 0],
                    linewidth=2
                )

                ax.text(
                    x / 2,
                    x / 2,
                    f"lado = {x:g}",
                    ha="center"
                )

            else:
                circ = plt.Circle(
                    (0, 0),
                    x,
                    fill=True,
                    alpha=.2
                )

                ax.add_patch(circ)

                ax.add_patch(
                    plt.Circle(
                        (0, 0),
                        x,
                        fill=False,
                        linewidth=2
                    )
                )

                ax.plot(
                    [0, x],
                    [0, 0],
                    "--",
                    linewidth=1.5
                )

                ax.text(
                    x / 2,
                    .1,
                    f"r = {x:g}",
                    ha="center"
                )

            ax.set_aspect(
                "equal",
                "datalim"
            )

            ax.axis("off")

            ax.set_title(
                "Figura e medidas"
            )

            self.renderizar_canvas(
                fig,
                chart
            )

        def tri():
            try:
                x = float(ea.get())
                y = float(eb.get())

                if x <= 0 or y <= 0:
                    raise ValueError

                resultado.config(
                    text=f"Área do triângulo = {(x * y / 2):.2f}"
                )

                desenhar(
                    "triangulo",
                    x,
                    y
                )

                self.ganhar_xp(
                    "matematica:areas",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Base e altura devem ser positivas."
                )

        def quad():
            try:
                x = float(
                    ea.get()
                )

                if x <= 0:
                    raise ValueError

                resultado.config(
                    text=f"Área do quadrado = {x * x:.2f}"
                )

                desenhar(
                    "quadrado",
                    x
                )

                self.ganhar_xp(
                    "matematica:areas",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Informe um lado positivo."
                )

        def circ():
            try:
                x = float(
                    ea.get()
                )

                if x <= 0:
                    raise ValueError

                resultado.config(
                    text=f"Área do círculo = {math.pi * x * x:.2f}"
                )

                desenhar(
                    "circulo",
                    x
                )

                self.ganhar_xp(
                    "matematica:areas",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Informe um raio positivo."
                )

        f = ttk.Frame(card)
        f.pack(
            anchor="w",
            pady=4
        )

        ttk.Button(
            f,
            text="Triângulo",
            command=tri
        ).pack(
            side="left",
            padx=(0, 4)
        )

        ttk.Button(
            f,
            text="Quadrado",
            command=quad
        ).pack(
            side="left",
            padx=(0, 4)
        )

        ttk.Button(
            f,
            text="Círculo",
            command=circ
        ).pack(
            side="left"
        )

    # ================================================================
    # MATEMÁTICA — BHASKARA
    # ================================================================

    def criar_aba_bhaskara(self):
        card, chart = self.criar_layout_split(
            "Bhaskara",
            "Equação do 2º grau: ax² + bx + c = 0."
        )

        self.adicionar_explicacao(
            card,
            "A fórmula de Bhaskara usa o discriminante Δ = b² − 4ac. "
            "Se Δ > 0 existem duas raízes reais; se Δ = 0 existe uma "
            "raiz real; se Δ < 0 não existem raízes reais.\n\n"
            "A representação gráfica da equação é uma parábola, "
            "e as raízes correspondem aos pontos onde ela cruza o eixo X."
        )

        self.adicionar_separador(card)

        entradas = []

        for rotulo, valor in [
            ("Coeficiente a", "1"),
            ("Coeficiente b", "-5"),
            ("Coeficiente c", "6")
        ]:
            tk.Label(
                card,
                text=rotulo,
                bg=self.card_bg,
                fg=self.text_light
            ).pack(anchor="w")

            e = ttk.Entry(card)
            e.pack(
                fill="x",
                pady=(3, 7)
            )

            e.insert(
                0,
                valor
            )

            entradas.append(e)

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def resolver():
            try:
                a, b, c = [
                    float(e.get())
                    for e in entradas
                ]

                if a == 0:
                    raise ValueError

                delta = (
                    b * b
                    - 4 * a * c
                )

                if delta < 0:
                    texto = (
                        f"Δ = {delta:.2f}\n"
                        "Não há raízes reais."
                    )
                    raizes = []

                elif delta == 0:
                    x = -b / (2 * a)

                    texto = (
                        "Δ = 0\n"
                        f"Raiz única: x = {x:.2f}"
                    )

                    raizes = [x]

                else:
                    x1 = (
                        -b
                        + math.sqrt(delta)
                    ) / (2 * a)

                    x2 = (
                        -b
                        - math.sqrt(delta)
                    ) / (2 * a)

                    texto = (
                        f"Δ = {delta:.2f}\n"
                        f"x₁ = {x1:.2f}\n"
                        f"x₂ = {x2:.2f}"
                    )

                    raizes = [
                        x1,
                        x2
                    ]

                resultado.config(
                    text=texto
                )

                xv = -b / (2 * a)

                x = np.linspace(
                    xv - 6,
                    xv + 6,
                    350
                )

                y = (
                    a * x * x
                    + b * x
                    + c
                )

                fig, ax = plt.subplots(
                    figsize=(5, 4),
                    dpi=100
                )

                ax.plot(
                    x,
                    y,
                    linewidth=2,
                    label=(
                        f"{a:g}x² + "
                        f"{b:g}x + "
                        f"{c:g}"
                    )
                )

                ax.axhline(
                    0,
                    color="black",
                    linewidth=.8,
                    linestyle="--"
                )

                ax.axvline(
                    0,
                    color="black",
                    linewidth=.8,
                    linestyle="--"
                )

                if raizes:
                    ax.scatter(
                        raizes,
                        [0] * len(raizes),
                        label="raízes"
                    )

                ax.grid(
                    True,
                    linestyle=":",
                    alpha=.5
                )

                ax.legend(
                    fontsize=8
                )

                ax.set_title(
                    "Parábola"
                )

                self.renderizar_canvas(
                    fig,
                    chart
                )

                self.ganhar_xp(
                    "matematica:bhaskara",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Informe a, b e c válidos; a não pode ser 0."
                )

        ttk.Button(
            card,
            text="Calcular e gerar parábola",
            style="Accent.TButton",
            command=resolver
        ).pack(
            anchor="w"
        )

    # ================================================================
    # MATEMÁTICA — GRÁFICOS
    # ================================================================

    def criar_aba_graficos(self):
        card, chart = self.criar_layout_split(
            "Gráficos",
            "Compare funções de 1º e 2º grau."
        )

        self.adicionar_explicacao(
            card,
            "Gráficos transformam uma expressão matemática em uma "
            "representação visual. No 1º grau, f(x)=ax+b forma uma reta. "
            "No 2º grau, f(x)=ax²+bx+c forma uma parábola.\n\n"
            "Alterando os coeficientes você pode observar como inclinação, "
            "posição e curvatura mudam."
        )

        self.adicionar_separador(card)

        es = []

        for rotulo, valor in [
            ("a", "1"),
            ("b", "0"),
            ("c", "0")
        ]:
            tk.Label(
                card,
                text=f"Coeficiente {rotulo}:",
                bg=self.card_bg,
                fg=self.text_light
            ).pack(anchor="w")

            e = ttk.Entry(card)
            e.pack(
                fill="x",
                pady=(3, 7)
            )

            e.insert(
                0,
                valor
            )

            es.append(e)

        def plotar(grau):
            try:
                a = float(
                    es[0].get()
                )

                b = float(
                    es[1].get()
                )

                c = float(
                    es[2].get()
                )

                x = np.linspace(
                    -10,
                    10,
                    350
                )

                if grau == 1:
                    y = a * x + b
                else:
                    y = (
                        a * x * x
                        + b * x
                        + c
                    )

                fig, ax = plt.subplots(
                    figsize=(5, 4),
                    dpi=100
                )

                ax.plot(
                    x,
                    y,
                    linewidth=2,
                    label="f(x)"
                )

                ax.axhline(
                    0,
                    color="black",
                    linewidth=.8,
                    linestyle="--"
                )

                ax.axvline(
                    0,
                    color="black",
                    linewidth=.8,
                    linestyle="--"
                )

                ax.grid(
                    True,
                    linestyle=":",
                    alpha=.5
                )

                ax.legend()

                ax.set_title(
                    f"Função do {grau}º grau"
                )

                self.renderizar_canvas(
                    fig,
                    chart
                )

                self.ganhar_xp(
                    f"matematica:grafico:{grau}",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Use apenas valores numéricos."
                )

        f = ttk.Frame(card)
        f.pack(
            anchor="w",
            pady=5
        )

        ttk.Button(
            f,
            text="Gerar 1º grau",
            command=lambda: plotar(1)
        ).pack(
            side="left",
            padx=(0, 5)
        )

        ttk.Button(
            f,
            text="Gerar 2º grau",
            command=lambda: plotar(2)
        ).pack(
            side="left"
        )

    # ================================================================
    # MATEMÁTICA — ARITMÉTICA
    # ================================================================

    def criar_aba_aritmetica(self):
        card, chart = self.criar_layout_split(
            "Aritmética",
            "Operações fundamentais com explicação do cálculo."
        )

        self.adicionar_explicacao(
            card,
            "Aritmética trabalha com as operações básicas: adição, "
            "subtração, multiplicação e divisão. Elas são a base de "
            "praticamente todos os cálculos usados em programação, "
            "engenharia, estatística e ciência de dados."
        )

        self.adicionar_separador(card)

        tk.Label(
            card,
            text="Primeiro número:",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        e1 = ttk.Entry(card)
        e1.pack(
            fill="x",
            pady=(3, 8)
        )
        e1.insert(
            0,
            "10"
        )

        tk.Label(
            card,
            text="Segundo número:",
            bg=self.card_bg,
            fg=self.text_light
        ).pack(anchor="w")

        e2 = ttk.Entry(card)
        e2.pack(
            fill="x",
            pady=(3, 10)
        )
        e2.insert(
            0,
            "2"
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=8
        )

        def calc(op):
            try:
                n1 = float(
                    e1.get()
                )

                n2 = float(
                    e2.get()
                )

                if op == "+":
                    r = n1 + n2
                    formula = (
                        f"{n1:g} + "
                        f"{n2:g} = "
                        f"{r:g}"
                    )

                elif op == "-":
                    r = n1 - n2
                    formula = (
                        f"{n1:g} - "
                        f"{n2:g} = "
                        f"{r:g}"
                    )

                elif op == "*":
                    r = n1 * n2
                    formula = (
                        f"{n1:g} × "
                        f"{n2:g} = "
                        f"{r:g}"
                    )

                else:
                    if n2 == 0:
                        messagebox.showwarning(
                            "Aviso",
                            "Divisão por zero não é permitida."
                        )
                        return

                    r = n1 / n2
                    formula = (
                        f"{n1:g} ÷ "
                        f"{n2:g} = "
                        f"{r:g}"
                    )

                resultado.config(
                    text=f"Resultado: {formula}"
                )

                self.ganhar_xp(
                    "matematica:aritmetica",
                    25
                )

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite dois números válidos."
                )

        f = ttk.Frame(card)
        f.pack(
            anchor="w",
            pady=4
        )

        for op in [
            "+",
            "−",
            "×",
            "÷"
        ]:
            real = {
                "+": "+",
                "−": "-",
                "×": "*",
                "÷": "/"
            }[op]

            ttk.Button(
                f,
                text=op,
                width=5,
                command=lambda o=real: calc(o)
            ).pack(
                side="left",
                padx=(0, 5)
            )

    # ================================================================
    # MATEMÁTICA — LÓGICA
    # ================================================================

    def criar_aba_logica(self):
        card, chart = self.criar_layout_split(
            "Lógica",
            "Operadores booleanos: AND, OR, XOR e NOT."
        )

        self.adicionar_explicacao(
            card,
            "Na lógica booleana, cada entrada pode ser verdadeira (True) "
            "ou falsa (False). AND exige duas entradas verdadeiras; "
            "OR exige pelo menos uma; XOR é verdadeiro quando exatamente "
            "uma é verdadeira; NOT inverte o valor.\n\n"
            "Esse tipo de lógica é usado em programação para decisões, "
            "validações, filtros e controle de fluxo."
        )

        self.adicionar_separador(card)

        a = tk.BooleanVar(
            value=False
        )

        b = tk.BooleanVar(
            value=False
        )

        ttk.Checkbutton(
            card,
            text="Entrada A = True",
            variable=a
        ).pack(
            anchor="w",
            pady=3
        )

        ttk.Checkbutton(
            card,
            text="Entrada B = True",
            variable=b
        ).pack(
            anchor="w",
            pady=3
        )

        resultado = tk.Label(
            card,
            text="Resultado: -",
            bg=self.card_bg,
            fg=self.accent_green,
            font=("Segoe UI", 10, "bold"),
            justify="left"
        )

        resultado.pack(
            anchor="w",
            pady=10
        )

        def avaliar(op):
            av = a.get()
            bv = b.get()

            if op == "AND":
                r = av and bv
                formula = (
                    f"A AND B = {r}"
                )

            elif op == "OR":
                r = av or bv
                formula = (
                    f"A OR B = {r}"
                )

            elif op == "XOR":
                r = av ^ bv
                formula = (
                    f"A XOR B = {r}"
                )

            else:
                formula = (
                    f"NOT A = {not av}\n"
                    f"NOT B = {not bv}"
                )

            resultado.config(
                text=f"Resultado:\n{formula}"
            )

            self.ganhar_xp(
                "matematica:logica",
                25
            )

        f = ttk.Frame(card)
        f.pack(
            anchor="w"
        )

        for op in [
            "AND",
            "OR",
            "XOR",
            "NOT"
        ]:
            ttk.Button(
                f,
                text=op,
                command=lambda o=op: avaliar(o)
            ).pack(
                side="left",
                padx=(0, 5)
            )

    # ================================================================
    # CERTIFICADO
    # ================================================================

    def criar_aba_certificado(self):
        aba = ttk.Frame(
            self.notebook,
            padding=18,
            style="DarkBG.TFrame"
        )

        self.notebook.add(
            aba,
            text="Certificado"
        )

        card = tk.Frame(
            aba,
            bg=self.card_bg,
            highlightbackground=self.accent_purple,
            highlightthickness=2
        )

        card.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            card,
            text="CERTIFICADO DE CONCLUSÃO",
            font=("Georgia", 24, "bold"),
            bg=self.card_bg,
            fg="#38bdf8"
        ).pack(
            pady=(45, 8)
        )

        tk.Label(
            card,
            text="Curso Interativo de T.I. + Matemática + Cyber Security",
            font=("Segoe UI", 13, "italic"),
            bg=self.card_bg,
            fg=self.text_muted
        ).pack(
            pady=(0, 22)
        )

        tk.Label(
            card,
            text="Nome do aluno",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_bg,
            fg=self.text_light
        ).pack()

        nome = ttk.Entry(
            card,
            font=("Segoe UI", 13),
            justify="center",
            width=42
        )

        nome.pack(
            pady=8
        )

        nome.insert(
            0,
            "Aluno"
        )

        xp_var = tk.StringVar(
            value=f"XP acumulado: {self.xp}"
        )

        tk.Label(
            card,
            textvariable=xp_var,
            font=("Segoe UI", 12, "bold"),
            bg=self.card_bg,
            fg=self.accent_green
        ).pack(
            pady=8
        )

        tk.Label(
            card,
            text=(
                "O certificado é gerado com o XP atual. "
                "Você pode gerar novamente a qualquer momento."
            ),
            font=("Segoe UI", 9),
            bg=self.card_bg,
            fg=self.text_muted
        ).pack(
            pady=5
        )

        def atualizar():
            xp_var.set(
                f"XP acumulado: {self.xp}"
            )

            self.atualizar_xp_label()

        def salvar_pdf():
            from tkinter import filedialog
            from datetime import datetime

            aluno = (
                nome.get().strip()
                or "Aluno"
            )

            atualizar()

            caminho = filedialog.asksaveasfilename(
                title="Salvar certificado",
                defaultextension=".pdf",
                filetypes=[
                    ("PDF", "*.pdf")
                ],
                initialfile=(
                    "certificado_xandy_academy.pdf"
                )
            )

            if not caminho:
                return

            try:
                fig = plt.figure(
                    figsize=(11.69, 8.27),
                    facecolor="#0f172a"
                )

                ax = fig.add_axes(
                    [0.04, 0.05, 0.92, 0.90]
                )

                ax.set_facecolor(
                    "#1e293b"
                )

                ax.set_xticks([])
                ax.set_yticks([])

                for spine in ax.spines.values():
                    spine.set_visible(True)
                    spine.set_linewidth(3)
                    spine.set_edgecolor("#38bdf8")

                ax.text(
                    .5,
                    .80,
                    "CERTIFICADO",
                    ha="center",
                    va="center",
                    fontsize=28,
                    fontweight="bold",
                    color="#38bdf8",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .73,
                    "DE CONCLUSÃO",
                    ha="center",
                    va="center",
                    fontsize=14,
                    fontweight="bold",
                    color="white",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .56,
                    aluno,
                    ha="center",
                    va="center",
                    fontsize=25,
                    fontweight="bold",
                    color="white",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .47,
                    "concluiu a experiência interativa de",
                    ha="center",
                    fontsize=12,
                    color="#94a3b8",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .39,
                    "T.I. • MATEMÁTICA • CYBER SECURITY",
                    ha="center",
                    fontsize=17,
                    fontweight="bold",
                    color="#10b981",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .29,
                    f"XP acumulado: {self.xp}",
                    ha="center",
                    fontsize=12,
                    fontweight="bold",
                    color="#38bdf8",
                    transform=ax.transAxes
                )

                ax.text(
                    .5,
                    .12,
                    f"Xandy Academy • {datetime.now().year}",
                    ha="center",
                    fontsize=10,
                    color="#64748b",
                    transform=ax.transAxes
                )

                fig.savefig(
                    caminho,
                    format="pdf",
                    bbox_inches="tight",
                    facecolor=fig.get_facecolor()
                )

                plt.close(fig)

                messagebox.showinfo(
                    "Certificado",
                    "Certificado salvo com sucesso em:\n"
                    f"{caminho}"
                )

            except Exception as erro:
                messagebox.showerror(
                    "Erro ao gerar certificado",
                    "Não foi possível salvar o PDF.\n\n"
                    f"{erro}"
                )

        ttk.Button(
            card,
            text="Atualizar XP",
            command=atualizar
        ).pack(
            pady=4
        )

        ttk.Button(
            card,
            text="GERAR E SALVAR CERTIFICADO PDF",
            style="Accent.TButton",
            command=salvar_pdf
        ).pack(
            pady=10
        )


# ================================================================
# EXECUÇÃO
# ================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = XandyAcademy(root)
    root.mainloop()