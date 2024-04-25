import ply.lex as lex


reserved = {
    'IF': 'IF',
    'ELSE': 'ELSE',
    'THEN': 'THEN',
    'WHILE': 'WHILE',
    'DO': 'DO',
    'LOOP': 'LOOP',
    'BEGIN': 'BEGIN',
    'REPEAT': 'REPEAT',
    'EXIT': 'EXIT',
    'DROP': 'DROP',
    'SWAP': 'SWAP',
    'ROT': 'ROT',
    'OVER': 'OVER',
    'CONCAT': 'CONCAT',
    'DUP': 'DUP',
    'EMIT': 'EMIT',
    'CR': 'CR'
}
# Lista de tokens
tokens = [
    'VARIABLE',
    'STRING',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'NOT',
    'INF',
    'SUP',
    'INFEQ',
    'SUPEQ',
    'EXCLAMATION',
    'AT',
    'DOT',
    'COLON',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'STDOUT',
    'CHAR',
    'reserved_word',
    'COMMENT',
    'NEWLINE'
 ] + list(reserved.values())


# Expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_NOT = r'\='
t_INF = r'<'
t_SUP = r'>'
t_INFEQ = r'<='
t_SUPEQ = r'>='
t_EXCLAMATION = r'!'
t_AT = r'@'
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_IF = r'[Ii][Ff]'
t_ELSE = r'[Ee][Ll][Ss][Ee]'
t_THEN = r'[Tt][Hh][Ee][Nn]'
t_DO = r'[Dd][Oo]'
t_LOOP = r'[Ll][Oo][Oo][Pp]'
t_BEGIN = r'[Bb][Ee][Gg][Ii][Nn]'
t_WHILE = r'[Ww][Hh][Ii][Ll][Ee]'
t_REPEAT = r'[Rr][Ee][Pp][Ee][Aa][Tt]'
t_EXIT = r'[Ee][Xx][Ii][Tt]'
t_DROP = r'[Dd][Rr][Oo][Pp]'
t_CONCAT = r'[Cc][Oo][Nn][Cc][Aa][Tt]'
t_SWAP = r'[Ss][Ww][Aa][Pp]'
t_ROT = r'[Rr][Oo][Tt]'
t_OVER = r'[Oo][Vv][Ee][Rr]'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"([^"]|\s)*"'
    t.value = str(t.value)
    return t

def t_STDOUT(t):
    r'\.\s*"([^"]*)"\s*'
    t.value = t.value[3:-1]
    return t

def t_CHAR(t):
    r'CHAR\s+.'
    t.value = str(f'"{t.value[5]}"')
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t\n'

def t_COMMENT(t):
    r'(?:\\.*$|\(.*?\))'
    t.value = str(t.value)
    print(t.value)
    return t

# Contagem de novas linhas
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print("Caractere inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()