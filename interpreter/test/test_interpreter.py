import pytest
from interpreter.ast import Number, BinOp, UnaryOp
from interpreter.token import Token, TokenType
from interpreter.interpreter import NodeVisitor, Interpreter

@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4

    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_mul(self, interpreter):
        assert interpreter.eval("2*5") == 10

    def test_div(self, interpreter):
        assert interpreter.eval("25/5") == 5

    def test_float(self, interpreter):
        assert interpreter.eval("4.2+2.2") == 6.4

    def test_unary_op_plus(self, interpreter):
        assert interpreter.eval("+++2") == 2

    def test_unary_minus(self, interpreter):
        assert interpreter.eval("-2") == -2

    def test_expr(self, interpreter):
        assert interpreter.eval("2-2/2+2*2") == 5

    def test_expr_break(self, interpreter):
        assert interpreter.eval("2+3*2/2") == 8

    def test_unary_expr(self, interpreter):
        assert interpreter.eval("+2-2-2") == -2

    def test_priority(self, interpreter):
        assert interpreter.eval("2+2*4") == 10

    def test_parentheses(self, interpreter):
        assert interpreter.eval("(2+3)*2") == 10

    def test_parentheses_error(self, interpreter):
        with pytest.raises(SyntaxError):
            assert interpreter.eval("(2+2")

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")
        with pytest.raises(SyntaxError):
            interpreter.eval("-a")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2 + 2"),
                              (interpreter, "2 +2 "),
                              (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

    def test_staples(self, interpreter):
        assert interpreter.eval("((9+7)*2-(4+5))/4") == 5.75

    def test_staples_error(self, interpreter):
        with pytest.raises(SyntaxError):
            assert interpreter.eval("5* (2 + 2")

    def test_prioritets(self, interpreter):
        assert interpreter.eval("2+2*2") == 6

    def test_prioritets_error(self, interpreter):
        with pytest.raises(AssertionError):
            assert interpreter.eval("2+2*2") == 8

    def test_unary_plus(self, interpreter):
        assert interpreter.eval("+2") == +2

    def test_unary_minus(self, interpreter):
        assert interpreter.eval("-2") == -2

    def test_wrong_unary_operator(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("*3")
        with pytest.raises(SyntaxError):
            interpreter.eval("S3")

    def test_interpreter_visit_binop_error(self, interpreter):
        with pytest.raises(ValueError):
            assert interpreter.visit(BinOp(Number(1), Token(TokenType.OPERATOR, "y"), Number(2)))

    def test_interpreter_visit_unarop_error(self, interpreter):
        with pytest.raises(ValueError):
            assert interpreter.visit(UnaryOp(Token(TokenType.OPERATOR, "/"), Number(1)))
