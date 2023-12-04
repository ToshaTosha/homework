class SpecialHashMap(dict):
    def __init__(self, values=None):
        if values is None:
            values = {}
        super().__init__(values)
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)


class Iloc:
    def __init__(self, special_dict: dict):
        self.special_dict = special_dict

    def __getitem__(self, item_index):
        if not isinstance(item_index, int) or item_index > len(self.special_dict) or item_index < 0:
            raise ValueError("Invalid index")
        sorted_index = sorted(self.special_dict.keys())
        return self.special_dict[sorted_index[item_index]]


class Ploc:
    def __init__(self, special_dict: dict):
        self.special_dict = special_dict

    @staticmethod
    def compare(key, op, value):
        comparison = {
            "<": key < value,
            ">": key > value,
            "=": key == value,
            "<=": key <= value,
            ">=": key >= value,
            "<>": key != value,
        }
        return comparison[op]

    @staticmethod
    def condition(operation, number) -> bool:
        operations = ["<", ">", "=", "<=", ">=", "<>"]
        return operation in operations and number.isdigit()

    @staticmethod
    def parse_condition(_condition):
        cleaned_condition = "".join(_condition.split())
        conditions = []

        for part in cleaned_condition.split(","):
            condition = {"op": "", "num": ""}
            for char in part:
                if char in ["<", ">", "="]:
                    condition["op"] += char
                elif char.isdigit():
                    condition["num"] += char
                elif char == ",":
                    if Ploc.condition(condition["op"], condition["num"]):
                        condition["num"] = float(condition["num"])
                        conditions.append(condition)
                    else:
                        raise SyntaxError("Неправильное условие")
                    condition = {"op": "", "num": ""}
            if Ploc.condition(condition["op"], condition["num"]):
                condition["num"] = float(condition["num"])
                conditions.append(condition)
            else:
                raise SyntaxError("Bad condition")

        return conditions

    @staticmethod
    def parse_key(_key):
        key_values = []
        key = _key[1:-1] if _key[0] == '(' else _key
        key = "".join(key.split()).split(',')

        if len(key) == 1 and key[0].isdigit():
            key_values.append(float(key[0]))
        else:
            key_values = [float(k) for k in key if k.isdigit()]

        return key_values

    def __getitem__(self, condition):
        if not isinstance(condition, str):
            raise SyntaxError("invalid condition")

        parsed_condition = self.parse_condition(condition)

        answer = "{"
        for k, v in self.special_dict.items():
            keys = self.parse_key(k)

            if len(keys) != len(parsed_condition):
                continue

            compared = True
            for index, value in enumerate(keys):
                op = parsed_condition[index]["op"]
                number = parsed_condition[index]["num"]

                if not self.compare(value, op, number):
                    compared = False
                    break

            if compared:
                answer += f", {k} = {v}" if len(answer) > 1 else f"{k} = {v}"

        answer += "}"
        return answer
