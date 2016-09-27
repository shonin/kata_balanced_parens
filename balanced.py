class Balanced:

    def answer(self, paren_string):
        input_string = ""
        while input_string != paren_string:
            input_string = paren_string
            paren_string = self.removeBalanced(input_string)
        if paren_string == "":
            return True
        return False

    def removeBalanced(self, paren_string):
        paren_string = paren_string.replace("[]", "")
        paren_string = paren_string.replace("()", "")
        return paren_string
