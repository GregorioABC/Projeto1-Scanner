import sys

# equivalente para os tokens
class TOKEN:
    MAIN = 'MAIN'
    TIPO_INT = 'TIPO_INT'
    TIPO_FLOAT = 'TIPO_FLOAT'
    TIPO_CHAR = 'TIPO_CHAR'
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    DO = 'DO'
    FOR = 'FOR'
    ID = 'ID'
    VALOR_INT = 'VALOR_INT'
    VALOR_FLOAT = 'VALOR_FLOAT'
    VALOR_CHAR = 'VALOR_CHAR'
    SOMA = 'SOMA'
    SUBTRACAO = 'SUBTRACAO'
    MULT = 'MULT'
    DIVISAO = 'DIVISAO'
    MAIOR = 'MAIOR'
    MAIOR_IGUAL = 'MAIOR_IGUAL'
    MENOR = 'MENOR'
    MENOR_IGUAL = 'MENOR_IGUAL'
    IGUALDADE = 'IGUALDADE'
    DIFERENCA = 'DIFERENCA'
    ATRIBUIR = 'ATRIBUIR'
    ABRE_PARENTESES = 'ABRE_PARENTESES'
    FECHA_PARENTESES = 'FECHA_PARENTESES'
    ABRE_CHAVES = 'ABRE_CHAVES'
    FECHA_CHAVES = 'FECHA_CHAVES'
    VIRGULA = 'VIRGULA'
    PONTO_E_VIRGULA = 'PONTO_E_VIRGULA'
    FIM_DE_ARQUIVO = 'EOF'

# Classe TNo equivalente
class TNo:
    def __init__(self, lexema, token):
        self.lexema = lexema
        self.token = token

# Variáveis globais
linha = 1
coluna = 0

# Função para exibir error
def exibirErro(msg, lexema):
    global linha, coluna
    print(f"Erro na linha {linha} coluna {coluna} último lexema lido '{lexema}': {msg}")
    sys.exit(1)

# Lista de palavras reservadas
palavras_reservadas = {
    'main': TOKEN.MAIN,
    'int': TOKEN.TIPO_INT,
    'float': TOKEN.TIPO_FLOAT,
    'char': TOKEN.TIPO_CHAR,
    'if': TOKEN.IF,
    'else': TOKEN.ELSE,
    'while': TOKEN.WHILE,
    'do': TOKEN.DO,
    'for': TOKEN.FOR
}

# Função principal do scanner
def SCANNER(f):
    global linha, coluna
    ch = ' '
    lexema = ''

    def next_char():
        nonlocal ch
        ch = f.read(1)
        return ch

    def preencher_lexema():
        nonlocal lexema
        lexema += ch

    while True:
        if ch == '':
            return TNo('', TOKEN.FIM_DE_ARQUIVO)

        # Ignorar espaços em branco
        while ch.isspace():
            if ch == ' ':
                coluna += 1
            elif ch == '\t':
                coluna += 4
            elif ch == '\n':
                linha += 1
                coluna = 0
            next_char()

        lexema = ''
        if ch == '':
            return TNo('', TOKEN.FIM_DE_ARQUIVO)

        # Operadores simples e marcadores
        operadores_simples = {
            '+': TOKEN.SOMA, '-': TOKEN.SUBTRACAO, '*': TOKEN.MULT,
            '(': TOKEN.ABRE_PARENTESES, ')': TOKEN.FECHA_PARENTESES,
            '{': TOKEN.ABRE_CHAVES, '}': TOKEN.FECHA_CHAVES,
            ',': TOKEN.VIRGULA, ';': TOKEN.PONTO_E_VIRGULA
        }

        if ch in operadores_simples:
            preencher_lexema()
            token = operadores_simples[ch]
            next_char()
            return TNo(lexema, token)

        # Operadores compostos e relacionais
        if ch in ['<', '>', '=', '!']:
            preencher_lexema()
            first = ch
            next_char()
            if ch == '=':
                preencher_lexema()
                comp_ops = {
                    '<=': TOKEN.MENOR_IGUAL,
                    '>=': TOKEN.MAIOR_IGUAL,
                    '==': TOKEN.IGUALDADE,
                    '!=': TOKEN.DIFERENCA
                }
                return TNo(lexema, comp_ops.get(lexema, TOKEN.DIFERENCA))
            elif first == '!':
                exibirErro("exclamação isolada", lexema)
            return TNo(lexema, {
                '<': TOKEN.MENOR,
                '>': TOKEN.MAIOR,
                '=': TOKEN.ATRIBUIR
            }[first])

        # Identificadores ou palavras reservadas
        if ch.isalpha() or ch == '_':
            while ch.isalnum() or ch == '_':
                preencher_lexema()
                next_char()
            return TNo(lexema, palavras_reservadas.get(lexema, TOKEN.ID))

        # Constantes numéricas
        if ch.isdigit():
            while ch.isdigit():
                preencher_lexema()
                next_char()
            if ch == '.':
                preencher_lexema()
                next_char()
                if not ch.isdigit():
                    exibirErro("float mal formado", lexema)
                while ch.isdigit():
                    preencher_lexema()
                    next_char()
                return TNo(lexema, TOKEN.VALOR_FLOAT)
            return TNo(lexema, TOKEN.VALOR_INT)

        # Constantes de caractere
        if ch == "'":
            preencher_lexema()
            next_char()
            if ch.isalnum():
                preencher_lexema()
                next_char()
                if ch == "'":
                    preencher_lexema()
                    next_char()
                    return TNo(lexema, TOKEN.VALOR_CHAR)
            exibirErro("char mal formado", lexema)

        
        if ch == '/':
            next_char()
            if ch == '/':
                while ch != '\n' and ch != '':
                    next_char()
                ch = ' '
                continue
            elif ch == '*':
                while True:
                    ch = f.read(1)
                    if ch == '':
                        exibirErro("comentário de bloco não encerrado", '/*')
                    if ch == '*':
                        ch = f.read(1)
                        if ch == '/':
                            next_char()
                            break
                continue
            else:
                return TNo('/', TOKEN.DIVISAO)

        # Caracter inválido
        preencher_lexema()
        exibirErro("caracter inválido", lexema)

# Função que chama o scanner
def main():
    if len(sys.argv) < 2:
        print("Uso: python scanner.py <arquivo>")
        return
    try:
        with open(sys.argv[1], 'r') as f:
            token = None
            while True:
                token = SCANNER(f)
                if token.token == TOKEN.FIM_DE_ARQUIVO:
                    print("Compilação realizada com sucesso.")
                    break
                print(f"{token.token:20} -> {token.lexema}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()
