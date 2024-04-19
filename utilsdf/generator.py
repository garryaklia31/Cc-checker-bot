from random import randint
from re import findall
from datetime import datetime
from typing import List, Tuple


class Generator:
    def __init__(self, bin: str, quantity: int = 10, return_list: bool = False) -> None:
        assert isinstance(bin, str), "The bin must be an instance of str"
        assert isinstance(quantity, int), "The quantity must be an instance of int"
        assert isinstance(
            return_list, bool
        ), "The return_list must be an instance of bool"
        self.data = self.get_info(bin)
        self.quantity = quantity
        self.return_list = return_list

    def generate_ccs(self) -> str | List[str]:
        ccs = []
        cc, mes, year, cvv = self.data
        current_year = datetime.now().year
        for _ in range(self.quantity):
            ccg = self.gen_cc(cc)
            anog = self.gen_year(year)
            current_month = int(anog) == current_year
            mesg = self.gen_mes(mes, current_month=current_month)
            cvvg = self.generate_cvv(cc)
            ccf = f"{ccg}|{mesg}|{anog}|{cvvg}"
            ccs.append(ccf)
        return ccs if self.return_list else "\n".join(ccs)

    @staticmethod
    def gen_cc(cc: str) -> str:
        if not Generator.valid_cc_to_gen(cc):
            raise ValueError("Invalid CC!")
        cc_temp = cc
        
        while True:
            cc_final = ""
            while (cc_temp[0] != "3" and len(cc_temp) != 16) or (
                cc_temp[0] == "3" and len(cc_temp) != 15
            ):
           
                cc_temp += "x"
                
            for d in cc_temp:
                if d.isdigit():
                    cc_final += d
                    continue
                cc_final += str(randint(0, 9))
            if Generator.is_luhn_valid(cc_final):
                return cc_final

    @staticmethod
    def gen_mes(mes: str = "x", current_month: bool = False) -> str:
        assert isinstance(mes, str), "The mes must be an instance of str"
        if mes.isdigit():
            return mes.zfill(2)
        range_month = datetime.now().month if current_month else 1
        return str(randint(range_month, 12)).zfill(2)

    @staticmethod
    def gen_year(year: str = "x") -> str:
        assert isinstance(year, str), "The year must be an instance of str"
        if year.isdigit():
            return year
        current_year = datetime.now().year
        return str(randint(current_year, current_year + 14))

    @staticmethod
    def valid_cc_to_gen(cc_to_validate: str) -> bool:
        assert isinstance(cc_to_validate, str), "The cc must be an instance of str"
        
        if (
            (
                cc_to_validate[0] not in ["3", "4", "5", "6"]
                or len(cc_to_validate) < 6
                or len(cc_to_validate) >= 16 and "x" not in cc_to_validate
            )
            or (cc_to_validate[0] == "3" and len(cc_to_validate) >= 15 and "x" not in cc_to_validate)
            or (len(cc_to_validate[0]) >= 16 and "x" not in cc_to_validate)
        ):
            return False
        return True

    @staticmethod
    def get_info(bin: str) -> Tuple[str, str, str, str]:
        data = findall(r"\d+(?:x\d+)*", bin)
        current_year = datetime.now().year
        short_year = int(str(current_year)[:2])
        
        if len(data) == 1:
            cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen = (
                data[0],
                "rnd",
                "rnd",
                "rnd",
            )
        elif len(data) == 2:
            cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen = (
                data[0],
                data[1],
                "rnd",
                "rnd",
            )
        elif len(data) == 3:
            cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen = (
                data[0],
                data[1],
                data[2],
                "rnd",
            )
        elif len(data) == 4:
            cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen = (
                data[0],
                data[1],
                data[2],
                data[3],
            )
        elif len(data) > 4:
            cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen = ("", "", "", "")
            for num in data:
                if cc_to_gen and mes_to_gen and year_to_gen and cvv_to_gen:
                    break
                if cc_to_gen == "" and Generator.valid_cc_to_gen(num):
                    cc_to_gen = num
                elif mes_to_gen == "" and int(num) in range(1, 13):
                    mes_to_gen = num
                elif year_to_gen == "" and (
                    len(num) == 4
                    and int(num) in range(current_year, current_year + 30)
                    or len(num) == 2
                    and int(num) in range(short_year, short_year + 20)
                ):
                    year_to_gen = num
        else:
            raise ValueError("Invalid BIN!")
        if "x" not in data[0]:
          cc_to_gen = cc_to_gen[:12]
        
        if not Generator.valid_cc_to_gen(cc_to_gen):
          raise ValueError("Invalid CC!")

        if len(year_to_gen) == 2:
            year_to_gen = "20" + year_to_gen
            
        if (
            mes_to_gen != "rnd"
            and int(year_to_gen) == current_year
            and int(mes_to_gen) not in range(datetime.now().month, 13)
            or mes_to_gen.isdigit()
            and int(mes_to_gen) not in range(1, 13)
        ):
            raise ValueError("Invalid month!")

        if year_to_gen != "rnd" and int(year_to_gen) not in range(
            current_year, current_year + 30
        ):
            raise ValueError("Invalid year!")
        
        cvv_to_gen = "rnd"
        
        return cc_to_gen, mes_to_gen, year_to_gen, cvv_to_gen

    @staticmethod
    def generate_cvv(cc):
      if cc.startswith("3"):
        cvv = str(randint(1000, 9999))
      if cc.startswith(("4", "5", "6")):
        cvv = str(randint(100, 999))
      return cvv

    @staticmethod
    def is_luhn_valid(cc: str) -> bool:
        assert isinstance(cc, str), "The cc must be an instance of str"
        num = list(map(int, str(cc)))
        return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0


if __name__ == "__main__":
    generator = Generator("4000228768x3x5x3 10 24")
    print(generator.generate_ccs())
