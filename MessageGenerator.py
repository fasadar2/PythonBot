class MessageGenerator:
    @staticmethod
    def GenerateMatrixMessage(matrix) -> str:
        generated_string = ""
        for string in matrix:
            for number in string:
                generated_string += number + " | "
            generated_string += "\n"
        return generated_string
