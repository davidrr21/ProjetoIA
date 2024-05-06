# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 64:
# 106763 David Rodrigues
# 105882 Duarte Gouveia

import sys
from sys import stdin
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class PipeManiaState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de PipeMania."""

    def __init__(self, dim, content):
        self.dim = dim
        self.content = content

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO
        cell = self.content[row][col]
        return cell

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        # TODO
        up = self.content[row - 1][col] if row - 1 >= 0 else None
        down = self.content[row + 1][col] if row + 1 < self.dim else None
        return up, down

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        left = self.content[row][col - 1] if col - 1 >= 0 else None
        right = self.content[row][col + 1] if col + 1 < self.dim else None
        return left, right
        

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt

            > from sys import stdin
            > line = stdin.readline().split()
        """
        # 
        
        content = []
        dim = 0
        for line in stdin:
            dim += 1
            words = line.split()
            linha = []
            for word in words:
                linha.append(word)
            content.append(linha)

        for linha in content:
            print(linha)
        print(dim)

        return Board(dim, content)

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, initial_state: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        self.board = initial_state
        pass

    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        possible_actions = []
        rows, columns = self.board.dim, self.board.dim
        for i in range(rows):
            for j in range(columns):
                for clockwise in [True, False]:
                    possible_actions.append((i, j, clockwise))

        print(possible_actions)
        return possible_actions

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        r, c, clockwise = action
        piece = state.board.content(r, c)
        print(piece)
        if clockwise:
            if piece == "FC":
                piece = "FD"
            if piece == "FB":
                piece = "FE"
            if piece == "FE":
                piece = "FC"
            if piece == "FD":
                piece = "FB"

            if piece == "BC":
                piece = "BD"   
            if piece == "BB":
                piece = "BE"
            if piece == "BE":
                piece = "BC"
            if piece == "BD":
                piece = "BB"

            if piece == "VC":
                piece = "VD"
            if piece == "VB":
                piece = "VE"
            if piece == "VE":
                piece = "VC"
            if piece == "VD":
                piece = "VB"

            if piece == "LH":
                piece = "LV"
            if piece == "LV":
                piece = "LH"
        else:
            if piece == "FC":
                piece = "FE"
            if piece == "FB":
                piece = "FD"
            if piece == "FE":
                piece = "FB"
            if piece == "FD":
                piece = "FC"

            if piece == "BC":
                piece = "BE"   
            if piece == "BB":
                piece = "BD"
            if piece == "BE":
                piece = "BB"
            if piece == "BD":
                piece = "BC"

            if piece == "VC":
                piece = "VE"
            if piece == "VB":
                piece = "VD"
            if piece == "VE":
                piece = "VB"
            if piece == "VD":
                piece = "VC"

            if piece == "LH":
                piece = "LV"
            if piece == "LV":
                piece = "LH" 
        print("piece:", piece)
        new_board = state.board.content.copy()
        new_board[r][c] = piece
        new_board = Board(state.board.dim, new_board)
        return PipeMania(PipeManiaState.board)

        

    def goal_test(self, state: PipeManiaState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass


board = Board.parse_instance()

problem = PipeMania(board)

initial_state = PipeManiaState(board)

print(initial_state.board.get_value(2,2))

result_state = problem.result(initial_state, (2, 2, True))

print(result_state.board.get_value(2, 2))


