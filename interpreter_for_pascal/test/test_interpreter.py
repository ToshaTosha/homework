import pytest

from interpreter.interpreter import NodeVisitor, Interpreter, Parser
from interpreter.ast import BinOp, Number, UnOp, Empty, Variable
from interpreter.token import Token, TokenType

@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


class TestInterpreter:
    interpreter = Interpreter()

    def test_empty_program(self, interpreter):
        assert interpreter.eval("BEGIN END.") == {}

    def test_complex_program(self, interpreter):
        assert interpreter.eval(
            '''
                BEGIN 
                    x := 5 * 3 - (6 + 4);
                    y := 8 / 2 + 5 * ((2 + 3) - (4 - 1)); 
                    z := 7 * 2 / 4 - 5 + ((2 * 3) + (4 / 2)); 
                END.
            ''') == {'x': 5.0, 'y': 14.0, 'z': 6.5}

    def test_invalid_single_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("a")

    def test_invalid_assignment(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x = 5")

    def test_invalid_factor_evaluation(self):
        with pytest.raises(SyntaxError):
            Parser().factor()

    def test_invalid_statement_evaluation(self):
        with pytest.raises(SyntaxError):
            Parser().statement()

    def test_uninitialized_variable_usage(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("BEGIN x := y END.")

    def test_valid_unary_operator_usage(self, interpreter):
        assert interpreter.visit_unop(UnOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, 5)))) == -5

    def test_valid_binary_operator_usage(self, interpreter):
        assert interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, '10')), Token(TokenType.OPERATOR, "+"),
                                             Number(Token(TokenType.NUMBER, '7')))) == 17

    def test_number_string_conversion(self):
        assert Number(Token(TokenType.NUMBER, "8")).__str__() == "Number (Token(TokenType.NUMBER, 8))"

    def test_binop_string_conversion(self):
        assert (BinOp(Number(Token(TokenType.NUMBER, '4')), Token(TokenType.OPERATOR, "-"),
                      Number(Token(TokenType.NUMBER, '3'))).__str__() ==
                "BinOp- (Number (Token(TokenType.NUMBER, 4)), Number (Token(TokenType.NUMBER, 3)))")

    def test_unop_string_conversion(self):
        assert UnOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, '6'))).__str__() == f"UnOp (-Number (Token(TokenType.NUMBER, 6)))"

    def test_variable_string_conversion(self):
        assert Variable(Token(TokenType.ID, "y")).__str__() == "Var (Token(TokenType.ID, y))"

    def test_empty_string_representation(self):
        assert Empty().__str__() == "Empty ()"

    def test_node_visitor_default_visit(self):
        assert NodeVisitor().visit() == None
