from .token import TokenType
from .lexer import Lexer
from .ast import BinOp, Number, UnOp, Variable, Empty, Assignment, Semicolon


class Parser:
    def __init__(self):
        self._current_token = None
        self._lexer = Lexer()

    def check_token(self, type_: TokenType):
        if self._current_token and self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError("invalid token order")

    def factor(self):
        token = self._current_token

        if not token:
            raise SyntaxError("Invalid factor")

        if token.type_ == TokenType.NUMBER:
            self.check_token(TokenType.NUMBER)
            return Number(token)

        if token.type_ == TokenType.LPAREN:
            self.check_token(TokenType.LPAREN)
            result = self.expr()
            self.check_token(TokenType.RPAREN)
            return result

        if token.type_ == TokenType.OPERATOR:
            self.check_token(TokenType.OPERATOR)
            return UnOp(token, self.factor())

        if token.type_ == TokenType.ID:
            self.check_token(TokenType.ID)
            return Variable(token)

        raise SyntaxError("Invalid factor")

    def term(self):
        result = self.factor()
        while self._current_token and self._current_token.type_ == TokenType.OPERATOR:
            if self._current_token.value in ["*", "/"]:
                token = self._current_token
                self.check_token(TokenType.OPERATOR)
                result = BinOp(result, token, self.factor())
            else:
                break
        return result

    def expr(self):
        result = self.term()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.term())
        return result

    def assignment(self):
        variable = self._current_token
        self.check_token(TokenType.ID)
        self.check_token(TokenType.ASSIGN)
        return Assignment(variable, self.expr())

    def statement(self):
        current_type = self._current_token.type_ if self._current_token else None
        if current_type == TokenType.BEGIN:
            return self.complex_statement()
        elif current_type == TokenType.ID:
            return self.assignment()
        elif current_type == TokenType.END:
            return Empty()
        else:
            raise SyntaxError("Invalid statement")

    def statement_list(self):
        result = self.statement()
        if self._current_token and self._current_token.type_ == TokenType.SEMICOLON:
            self._current_token = self._lexer.next()
            result = Semicolon(result, self.statement_list())
        return result

    def complex_statement(self):
        self.check_token(TokenType.BEGIN)
        result = self.statement_list()
        self.check_token(TokenType.END)
        return result

    def program(self):
        result = self.complex_statement()
        self.check_token(TokenType.DOT)
        return result

    def parse(self, code):
        self._lexer.init(code)
        self._current_token = self._lexer.next()
        return self.program()