import ply.yacc as yacc

from lexico import tokens


def p_prog_decl(p):
    'prog : PROGRAM ID PVIG decls cmdComp PONTO'
    p[0] = ('prog-decl', p[1], p[2], p[3], p[4], p[5], p[6])


def p_decls(p):
    '''
    decls : empty
          | VAR listDecl
    '''
    p[0] = ('declaração', p[1], p[2])


def p_listDecl(p):
    '''
     listDecl : declTip
              | declTip listDecl
    '''


def p_declTip(p):
    '''
    declTip : listId DPONTOS tip PVIG
    '''


def p_listId(p):
    '''
    listId : ID
	       | ID VIG listId
    '''


def p_tip(p):
    '''
    tip : INTEGER
        | BOOLEAN
        | CADEIA
    '''


def p_cmdComp(p):
    '''
    cmdComp : BEGIN listCmd END
    '''


def p_listCmd(p):
    '''
    listCmd : cmd
            | cmd PVIG listCmd
    '''


def p_cmd(p):
    '''
    cmd : cmdIf
        | cmdWhile
        | cmdRead
        | cmdWrite
        | cmdAtrib
        | cmdComp
    '''


def p_cmdIf(p):
    '''
    cmdIf : IF expr THEN cmd
         | IF expr THEN cmd ELSE cmd
    '''


def p_cmdWhile(p):
    '''
    cmdWhile : WHILE expr DO cmd
    '''


def p_cmdRead(p):
    '''
    cmdRead : READ ABPAR listId FPAR
    '''


def p_cmdWrite(p):
    '''
    cmdWrite : WRITE ABPAR listW FPAR
    '''


def p_listW(p):
    '''
    listW : elemW
    | elemW VIG listW
    '''


def p_elemW(p):
    '''
    elemW : expr
    | CADEIA
    '''


def p_cmdAtrib(p):
    '''
    cmdAtrib : ID ATRIB expr
    '''


def p_expr(p):
    '''
    expr : OPNEG ABPAR expr FPAR
	| expr OPMULT expr
	| expr OPDIV expr
	| expr OPAD expr
	| expr OPSUB expr
	| expr OPREL expr
	| OPNEG ID
	| OPNEG TRUE
	| OPNEG FALSE
	| OPNEG OPNEG
    '''


# Regra adicionada OPREL erro
def p_opRel(p):
    '''
    OPREL : MENOR
    | MAIOR
    | MAIG
    | MENIG
    | IGUAL
    | DIFER
    '''


# Regra adicionada OPLOG erro porém não é alcançavel
def p_opLog(p):
    '''
    OPLOG : AND
          | OR
    '''


def p_empty(p):
    'empty :'
    pass


erros_sintaticos = []


# Error rule for syntax errors
def p_error(p):
    erros_sintaticos.append(p)
    print(f"Syntax error in input!{p}")


# Build the parser
parser = yacc.yacc(debug=True)
print()
print('Saída sintatico')
while True:
    try:
        s = input('''
PROGRAM example;
VAR x : INTEGER; //rtreyyrty
BEGIN
    x := 5 * 10;
    WRITE(x);
END. "ret345?/:;>,]}[{~´_=+|!@#$%&*()"
        ''')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(input=s, debug=True, tracking=True)
    print(result)
