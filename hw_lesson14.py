import csv
class Phone:
    phone_number = ''
    _incomming_calls = 0

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_calls(self):
        self._incomming_calls += 1

    def _get_number_of_calls(self):
        return self._incomming_calls


phone_1 = Phone()
phone_1.set_phone_number('380681217302')
phone_1.get_calls()
phone_1.get_calls()
phone_1.get_calls()

phone_2 = Phone()
phone_2.set_phone_number('380671452154')
phone_2.get_calls()
phone_2.get_calls()

phone_3 = Phone()
phone_3.set_phone_number('380501524152')
phone_3.get_calls()
phone_3.get_calls()

col = [phone_1, phone_2, phone_3]
calls_total_number = 0
for phone in col:
    calls_total_number += phone._get_number_of_calls()


with open('calls_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Total Calls'])
    csvwriter.writerow([calls_total_number])


class Color:
    WHITE = "white"
    BLACK = "black"


class ChessPiece:
    def __init__(self, color, placement):
        if color in (Color.WHITE, Color.BLACK):
            self.color = color
        else:
            raise ValueError('Invalid color value')
        self.placement = placement

    def change_color(self):
        if self.color == Color.WHITE:
            self.color = Color.BLACK
        else: self.color = Color.BLACK

    def get_color(self):
        return self.color
    
    def move_figure(self, coordinate_1, coordinate_2):
        if coordinate_1 in range(7) and coordinate_2 in range(7):
            self.placement = (coordinate_1, coordinate_2)
        else:
            print("Check your move, it is beyond the field")

    def get_current_position(self):
        return self.placement
    
    def is_valid_move(self, new_placement):
        raise NotImplementedError("Subclasses must implement this method")
    



class Pawn(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        # Перевірка ходу для білого пішака (рух вперед)
        if self.color == Color.WHITE:
            if current_file == new_file and new_rank == current_rank + 1 and new_rank <= 7:
                return True
            if current_rank == 1 and new_rank == current_rank + 2 and current_file == new_file and new_rank <= 7:
                return True

        elif self.color == Color.BLACK:
            if current_file == new_file and new_rank == current_rank - 1 and new_rank >= 0:
                return True

            if current_rank == 6 and new_rank == current_rank - 2 and current_file == new_file and new_rank >= 0:
                return True

            if abs(ord(current_file) - ord(new_file)) == 1 and new_rank == current_rank - 1 and new_rank >= 0:
                return True

        return False


class Knight(ChessPiece):
    def is_valid_move(self, new_placement):

        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        file_diff = ord(new_file) - ord(current_file)
        rank_diff = new_rank - current_rank

         # Allowed moves for Knight
        allowed_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
            ]

        if (file_diff, rank_diff) in allowed_moves and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        return False
    
class Bishop(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        file_diff = ord(new_file) - ord(current_file)
        rank_diff = new_rank - current_rank

        if (file_diff == rank_diff or file_diff == -rank_diff) and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        return False


class Rook(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        if (current_file == new_file or current_rank == new_rank) and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        return False


class Queen(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        file_diff = ord(new_file) - ord(current_file)
        rank_diff = new_rank - current_rank

        # horizontal or vertical move check
        if (current_file == new_file or current_rank == new_rank) and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        #  diagonal move check
        if file_diff == rank_diff or file_diff == -rank_diff and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        return False


class King(ChessPiece):
    def is_valid_move(self, new_placement):
        current_file, current_rank = self.placement
        new_file, new_rank = new_placement

        file_diff = ord(new_file) - ord(current_file)
        rank_diff = new_rank - current_rank

        # Дозволені рухи короля (по одній клітині)
        if (file_diff == 1 or file_diff == -1) and (rank_diff == 1 or rank_diff == -1) \
           and new_file in 'abcdefgh' and new_rank in range(1, 8):
            return True

        return False
    

pawn = Pawn('white', (0, 0))
knight = Knight('white', (0, 0))
bishop = Bishop('black', (0, 0))
queen = Queen('white', (0, 0))


print(pawn.is_valid_move((0, 1)))
print(pawn.get_color())
pawn.change_color()
print(pawn.get_color())
pawn.change_color()
print(pawn.get_color())
pawn.change_color()
print(pawn.get_color())

pawn.move_figure(3, 3)
print(pawn.get_current_position())
pawn.move_figure(1, 9)



