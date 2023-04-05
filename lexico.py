# ------------------------------------------------------------
# lexico.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'OPAD',
    'OPSUB',
    'OPMULT',
    'OPDIV',
    'ABPAR',
    'FPAR',
    'MENOR',
    'MAIOR',
    'MENIG',
    'MAIG',
    'IGUAL',
    'DIFER',
    'OR',
    'AND',
    'OPNEG',
    'PVIG',
    'PONTO',
    'DPONTOS',
    'VIG',
    'PROGRAM',
    'VAR',
    'INTEGER',
    'BOOLEAN',
    'BEGIN',
    'END',
    'IF',
    'ELSE',
    'WHILE',
    'DO',
    'WRITE',
    'READ',
    'THEN',
    'ATRIB',
    'TRUE',
    'FALSE',
    'NUMBER',
    'CADEIA',
    'CONST',
    'ID',
)

# Regular expression rules for simple tokens
t_OPAD = r'\+'
t_OPSUB = r'\-'
t_OPMULT = r'\*'
t_OPDIV = r'\/'
t_ABPAR = r'\('
t_FPAR = r'\)'
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MENIG = r'\<='
t_MAIG = r'\>='
t_IGUAL = r'\=='
t_DIFER = r'\<>'
t_OR = r'\&'
t_AND = r'AND'
t_OPNEG = r'\~'
t_PVIG = r'\;'
t_PONTO = r'\.'
t_DPONTOS = r'\:'
t_VIG = r'\,'
t_ATRIB = r'\:='
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'


# t_CADEIA = r'"[^("|\n)]*"'


# t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_PALAVRA_RESERVADA = r'PROGRAM|INTEGER|BOOLEAN|BEGIN|END|WHILE|DO|READ|VAR|FALSE|TRUE|WRITE'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    # CONST_INT = 32767  # valor máximo permitido em 2 bytes (2^15 - 1)

    # Exemplo de uso da constante
    # x = 100001
    # if t.value <= CONST_INT:
    #     print("O valor de x é válido.")
    #     return t
    # else:
    #     print("O valor de x é inválido, pois ultrapassa 2 bytes.")
    # return t


def t_CADEIA(t):
    r'"([^"\n]|(\\"))*"$'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Palavras reservadas
reserved = {
    'PROGRAM': 'PROGRAM',
    'INTEGER': 'INTEGER',
    'BOOLEAN': 'BOOLEAN',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'WHILE': 'WHILE',
    'DO': 'DO',
    'READ': 'READ',
    'VAR': 'VAR',
    'FALSE': 'FALSE',
    'TRUE': 'TRUE',
    'WRITE': 'WRITE',
    'CONST': 'CONST'
}


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    if len(t.value) > 16:
        t.value = t.value[:16]
    return t


# Error handling rule
def t_error(t):
    print(f"Caracter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)


def t_COMMENT(t):
    r'//.*\n'
    pass


# def t_string_any(t):
#     r'[^\n]'
#     pass


# def t_string_error(t):
#     print("illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)
#
#     t_string_ignore = ' \t'


# lexer = lex.lex()

# Build the lexer
lexer = lex.lex()

# Teste
data = '''
PROGRAM example;
VAR x : INTEGER; //rtreyyrty
BEGIN
    x := 5 * 10;
    WRITE(x);
END. "ret345?/:;>,]}[{~´_=+|!@#$%&*()"
'''.upper()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok.type, tok.value)
