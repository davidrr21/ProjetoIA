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
        self.initial_state = initial_state
        pass

    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        possible_actions = []
        rows, columns = self.initial_state.dim, self.initial_state.dim
        for i in range(rows):
            for j in range(columns):
                for clockwise in [True, False]:
                    possible_actions.append((i, j, clockwise))

        return possible_actions

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO

        r, c, clockwise = action
        piece = state.board.get_value(r, c)

        if clockwise:
            if piece == "FC":
                piece = "FD"
            elif piece == "FB":
                piece = "FE"
            elif piece == "FE":
                piece = "FC"
            elif piece == "FD":
                piece = "FB"

            elif piece == "BC":
                piece = "BD"   
            elif piece == "BB":
                piece = "BE"
            elif piece == "BE":
                piece = "BC"
            elif piece == "BD":
                piece = "BB"

            elif piece == "VC":
                piece = "VD"
            elif piece == "VB":
                piece = "VE"
            elif piece == "VE":
                piece = "VC"
            elif piece == "VD":
                piece = "VB"

            elif piece == "LH":
                piece = "LV"
            elif piece == "LV":
                piece = "LH"
        else:
            if piece == "FC":
                piece = "FE"
            elif piece == "FB":
                piece = "FD"
            elif piece == "FE":
                piece = "FB"
            elif piece == "FD":
                piece = "FC"

            elif piece == "BC":
                piece = "BE"   
            elif piece == "BB":
                piece = "BD"
            elif piece == "BE":
                piece = "BB"
            elif piece == "BD":
                piece = "BC"

            elif piece == "VC":
                piece = "VE"
            elif piece == "VB":
                piece = "VD"
            elif piece == "VE":
                piece = "VB"
            elif piece == "VD":
                piece = "VC"

            elif piece == "LH":
                piece = "LV"
            elif piece == "LV":
                piece = "LH" 

        new_board = Board(state.board.dim, state.board.content)
        new_board.content[r][c] = piece
        
        return PipeManiaState(new_board)

        

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


