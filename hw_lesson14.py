class ChessPiece:
    def __init__(self, color, placement):
        self.color = color
        self.placement = placement
    
    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else: self.color = "white"

    def selected_color(self):
        return self.color
    
    def move_figure(self, coordinate_1, coordinate_2):
        if coordinate_1 in range(7) and coordinate_2 in range(7):
            self.placement = (coordinate_1, coordinate_2)
        else:
            print("Check your move, it is beyond the field")

    def current_position(self):
        return self.placement
    
    def is_valid_move(self, new_placement):
        raise NotImplementedError("Subclasses must implement this method")
    



class Pawn(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        # Перевірка ходу для білого пішака (рух вперед)
        if self.color == 'white':
            if current_file == new_file and new_rank == current_rank + 1 and new_rank <= 7:
                return True

            if current_rank == 1 and new_rank == current_rank + 2 and current_file == new_file and new_rank <= 7:
                return True

        # Перевірка ходу для чорного пішака (рух назад)
        elif self.color == 'black':
            if current_file == new_file and new_rank == current_rank - 1 and new_rank >= 0:
                return True

            if current_rank == 6 and new_rank == current_rank - 2 and current_file == new_file and new_rank >= 0:
                return True

            if abs(ord(current_file) - ord(new_file)) == 1 and new_rank == current_rank - 1 and new_rank >= 0:
                return True

        return False

   

class Knight(ChessPiece):
    def is_valid_move(self, new_placement):
        pass
    
class Bishop(ChessPiece):
    def is_valid_move(self, new_placement):
        # Логіка перевірки можливості ходу офіцера
        pass

class Rook(ChessPiece):
    def is_valid_move(self, new_placement):
        # Логіка перевірки можливості ходу тури
        pass

class Queen(ChessPiece):
    def is_valid_move(self, new_placement):
        # Логіка перевірки можливості ходу ферзя
        pass

class King(ChessPiece):
    def is_valid_move(self, new_placement):
        # Логіка перевірки можливості ходу короля
        pass

    

pawn = ChessPiece('white', (0, 0))

print(pawn.selected_color())
pawn.change_color()
print(pawn.selected_color())
pawn.change_color()
print(pawn.selected_color())
pawn.change_color()
print(pawn.selected_color())

pawn.move_figure(3, 3)
print(pawn.current_position())
pawn.move_figure(1, 9)



