from .token import Token, TokenType


class Lexer():

    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]

    def forward(self):
        if self._pos < len(self._text) - 1:
            self._pos += 1
            self._current_char = self._text[self._pos]
        else:
            self._current_char = None

    def skip(self):
        while (self._current_char is not None and self._current_char.isspace()):
            self.forward()

    def number(self):
        result = []
        while (self._current_char is not None and
               (self._current_char.isdigit() or
                self._current_char == ".")):
            result.append(self._current_char)
            self.forward()
        return "".join(result)

    def is_assignment(self):
        self.forward()
        while self._current_char is not None and self._current_char.isspace():
            self.forward()
        if self._current_char == '=':
            self.forward()
            return True
        return False

    def variable(self):
        result = []
        correct_var = False
        while self._current_char is not None and (self._current_char.isalnum() or self._current_char == "_"):
            if self._current_char.isalpha() and not correct_var:
                correct_var = True
            result.append(self._current_char)
            self.forward()
        return "".join(result), correct_var

    def next(self):
        while self._current_char:
            if self._current_char.isspace():
                self.skip()
                continue
            elif self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            elif self._current_char in ["+", "-", "/", "*"]:
                op = self._current_char
                self.forward()
                return Token(TokenType.OPERATOR, op)
            elif self._current_char in {"(", ")", ".", ";"}:
                token_type = {
                    "(": TokenType.LPAREN,
                    ")": TokenType.RPAREN,
                    ".": TokenType.DOT,
                    ";": TokenType.SEMICOLON
                }[self._current_char]
                self.forward()
                return Token(token_type, self._current_char)
            elif self._current_char == ":":
                if self.is_assignment():
                    return Token(TokenType.ASSIGN, ":=")
            elif self._current_char == "B":  # BEGIN
                begin = ['B', 'E', 'G', 'I', 'N']
                while self._current_char and self._current_char in begin:
                    self.forward()
                return Token(TokenType.BEGIN, "BEGIN")
            elif self._current_char == "E":  # END
                begin = ['E', 'N', 'D']
                while self._current_char and self._current_char in begin:
                    self.forward()
                return Token(TokenType.END, "END")
            elif self._current_char.isalpha() or self._current_char == '_':
                var, correct_var = self.variable()
                if correct_var:
                    return Token(TokenType.ID, var)

            raise SyntaxError("bad token")
