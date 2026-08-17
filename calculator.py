import re
import tkinter as tk

class CalculadoraWindows:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5630F")

        # Variável para armazenar a expressão atual
        self.expressao = ""

        # --- PAINEL / DISPLAY ---
        self.display = tk.Entry(
            root,
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#000000",
            bd=0,
            justify="right"
        )
        self.display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=15)

        # --- GRADE DE BOTÕES ---
        container_botoes = tk.Frame(root, bg="#080808")
        container_botoes.pack(fill="both", expand=True, padx=5, pady=5)

        # Layout dos botões (Estilo Calculadora)
        botoes = [
            ('C', 0, 0), ('CE', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('+/-', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3)
        ]

        # Configurar colunas e linhas para expandirem igualmente
        for i in range(4):
            container_botoes.grid_columnconfigure(i, weight=1)
        for i in range(5):
            container_botoes.grid_rowconfigure(i, weight=1)

        # Criar os botões na tela
        for texto, linha, coluna in botoes:
            # Estilização parecida com o Windows 10
            cor_fundo = "#ffffff" if texto.isdigit() or texto == '.' else "#f9f9f9"
            if texto == '=':
                cor_fundo = "#0067c0"  # Destaque azul para o botão igual
                cor_texto = "#ffffff"
            else:
                cor_texto = "#000000"

            btn = tk.Button(
                container_botoes,
                text=texto,
                font=("Segoe UI", 12),
                bg=cor_fundo,
                fg=cor_texto,
                bd=1,
                relief="flat",
                command=lambda t=texto: self.ao_clicar_botao(t)
            )
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

        # Suporte para teclado físico
        self.root.bind("<Key>", self.pressionar_tecla)

    def formatar_inteiro_para_display(self, numero):
        if numero < 0:
            return "-" + f"{abs(numero):,}".replace(",", ".")
        return f"{numero:,}".replace(",", ".")

    def formatar_numero_para_display(self, valor):
        if isinstance(valor, bool):
            return str(valor)
        if isinstance(valor, int):
            return self.formatar_inteiro_para_display(valor)
        if isinstance(valor, float):
            if valor.is_integer():
                return self.formatar_inteiro_para_display(int(valor))
            return str(valor)
        return str(valor)

    def formatar_expressao_para_display(self, expressao):
        if not expressao:
            return ""

        tokens = re.findall(r"\d+(?:\.\d+)*|[+\-*/%]", expressao)
        if not tokens:
            return expressao

        formatado = []
        for token in tokens:
            if re.fullmatch(r"\d+(?:\.\d+)*", token):
                numero = token.replace(".", "")
                if numero.isdigit():
                    formatado.append(self.formatar_inteiro_para_display(int(numero)))
                else:
                    formatado.append(token)
            else:
                formatado.append(token)

        return "".join(formatado)

    def atualizar_display(self, valor):
        self.display.delete(0, tk.END)
        if isinstance(valor, (int, float)):
            texto = self.formatar_numero_para_display(valor)
        elif isinstance(valor, str):
            texto = self.formatar_expressao_para_display(valor)
        else:
            texto = str(valor)
        self.display.insert(tk.END, texto)

    def ao_clicar_botao(self, caractere):
        if caractere == "C" or caractere == "CE":
            self.expressao = ""
            self.atualizar_display("")
        elif caractere == "=":
            self.calcular()
        elif caractere == "+/-":
            if self.expressao:
                if self.expressao.startswith("-"):
                    self.expressao = self.expressao[1:]
                else:
                    self.expressao = "-" + self.expressao
                self.atualizar_display(self.expressao)
        else:
            self.expressao += str(caractere)
            self.atualizar_display(self.expressao)

    def calcular(self):
        try:
            if not self.expressao:
                return

           
            expressao_limpa = self.expressao.replace(".", "")

            # Avalia a expressão matemática com um contexto seguro
            resultado = eval(expressao_limpa, {"__builtins__": {}}, {})

            # Formatação caso o resultado seja número inteiro
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            self.atualizar_display(resultado)
            self.expressao = str(resultado)
        except ZeroDivisionError:
            self.atualizar_display("Erro: Divisão por 0")
            self.expressao = ""
        except Exception:
            self.atualizar_display("Erro")
            self.expressao = ""

    def pressionar_tecla(self, event):
        tecla = event.char
        if tecla in "0123456789+-*/.%":
            self.ao_clicar_botao(tecla)
        elif event.keysym == "Return" or event.keysym == "KP_Enter":
            self.calcular()
        elif event.keysym == "BackSpace":
            self.expressao = self.expressao[:-1]
            self.atualizar_display(self.expressao)
        elif event.keysym == "Escape":
            self.ao_clicar_botao("C")

# --- INICIALIZAÇÃO DA APLICAÇÃO ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraWindows(root)
    root.mainloop()