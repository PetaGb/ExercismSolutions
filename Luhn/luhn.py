import re
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
    
    def valid(self):
        space_less = re.sub(r'\s+', '', self.card_num)
        if not all([s.isdigit() for s in space_less]) or len(space_less) <= 1:
            return False 
        int_list = [int(s) for s in space_less]
        doubled = [(l*2) if i % 2 != 0  
                   else l for i, l in enumerate(reversed(int_list))]
        final = [(d-9) if d > 9 else d for d in doubled]
        return sum(final) % 10 == 0
      