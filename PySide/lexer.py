import ply.lex as lex

tokens = (
    'ID',
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "PPAREN"
)

reverseds = {
    "if" : "IF"
}

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"/"
t_DIVIDE = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"

def t_ID(t):
    r"[a-zA-Z_0-9]*"
    t.type = reverseds.get(t.value, "ID")
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
