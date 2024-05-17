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

locked_pieces = None
profundidade = 0

class PipeManiaState:
    state_id = 0

    def __init__(self, board, prof):
        self.board = board
        self.prof = prof
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe

    def dfs(self):
        visited = [[False for _ in range(self.board.dim)] for _ in range(self.board.dim)]
        stack = [(0, 0)]  # Começa na posição (0, 0)

        Left = ["FD", "BC", "BB", "BD", "VB", "VD", "LH"]
        Right = ["FE", "BC", "BB", "BE", "VC", "VE", "LH"]
        Down = ["FC", "BC", "BE", "BD", "VC", "VD", "LV"]
        Up = ["FB", "BB", "BE", "BD", "VB", "VE", "LV"]

        while stack:
            row, col = stack.pop()
            visited[row][col] = True

            up = down = left = right = (-1, -1)

            if(row - 1 >= 0):
                up = (row - 1, col)
            if(row + 1 < self.board.dim):
                down = (row + 1, col)
            if(col - 1 >= 0):
                left = (row, col - 1)
            if(col + 1 < self.board.dim):
                right = (row, col + 1)

            type = self.board.get_value(row, col)
            #tipos de peças
            if (type == "FC"):
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False
                    
            if (type == "FB"):
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False
                    
            if (type == "FE"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                    
            if (type == "FD"):
                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False
            

            if (type == "BC"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False
                
                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False
                
            if (type == "BB"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False
                
                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False

            if (type == "BE"):
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False

                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False

            if (type == "BD"):
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False

                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False
                
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False


            if (type == "VC"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                    
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False
            
            if (type == "VB"):
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False
                    
                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False

            if (type == "VE"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False
                    
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False

            if (type == "VD"):
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False
                    
                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False


            if (type == "LH"):
                if (left != (-1, -1)):
                    if(not visited[left[0]][left[1]]):
                        left_type = self.board.get_value(left[0], left[1])
                        if left_type in Left:
                            stack.append(left)
                        else:
                            return False
                else:
                    return False

                if (right != (-1, -1)):
                    if(not visited[right[0]][right[1]]):
                        right_type = self.board.get_value(right[0], right[1])
                        if right_type in Right:
                            stack.append(right)
                        else:
                            return False
                else:
                    return False
                    
            if (type == "LV"):
                if (up != (-1, -1)):
                    if(not visited[up[0]][up[1]]):
                        up_type = self.board.get_value(up[0], up[1])
                        if up_type in Up:
                            stack.append(up)
                        else:
                            return False
                else:
                    return False
                
                if (down != (-1, -1)):
                    if(not visited[down[0]][down[1]]):
                        down_type = self.board.get_value(down[0], down[1])
                        if down_type in Down:
                            stack.append(down)
                        else:
                            return False
                else:
                    return False
        
        
        for row in visited:
            for cell in row:
                if not cell:
                    return False

                
        return True


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

        global locked_pieces
        locked_pieces = [["unlock"] * dim for _ in range(dim)]
        return Board(dim, content)

    def print(self):
        result = "\n".join(" ".join(row) for row in self.content)
        return result
    
    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        self.initial = PipeManiaState(board, profundidade)
        

    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        #Listar em tuplos todas as ações possiveis a realizar num tabuleiro de dimensão nxn tendo em conta a posição das peças
        global locked_pieces
        actions = []
        dim = state.board.dim
        flag = False

        if(state.prof < (dim * dim)):
            r = state.prof // dim
            c = state.prof % dim
               
            piece = state.board.get_value(r, c)
            if piece in ["FC", "FD", "FB", "FE"]:
                actions.append((r, c, "init"))
                actions.append((r, c, "CW"))
                actions.append((r, c, "ACW"))
                actions.append((r, c, "HCW"))
            elif piece in ["BC", "BD", "BB", "BE"]:
                actions.append((r, c, "init"))
                actions.append((r, c, "CW"))
                actions.append((r, c, "ACW"))
                actions.append((r, c, "HCW"))
            elif piece in ["VC", "VD", "VB", "VE"]:
                actions.append((r, c, "init"))
                actions.append((r, c, "CW"))
                actions.append((r, c, "ACW"))
                actions.append((r, c, "HCW"))
            elif piece in ["LH", "LV"]:
                actions.append((r, c, "CW"))
                actions.append((r, c, "HCW"))


        return actions


    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO

        rotations = {
            "FC": {"CW": "FD", "ACW": "FE", "HCW": "FB"},
            "FD": {"CW": "FB", "ACW": "FC", "HCW": "FE"},
            "FB": {"CW": "FE", "ACW": "FD", "HCW": "FC"},
            "FE": {"CW": "FC", "ACW": "FB", "HCW": "FD"},
            "BC": {"CW": "BD", "ACW": "BE", "HCW": "BB"},
            "BD": {"CW": "BB", "ACW": "BC", "HCW": "BE"},
            "BB": {"CW": "BE", "ACW": "BD", "HCW": "BC"},
            "BE": {"CW": "BC", "ACW": "BB", "HCW": "BD"},
            "VC": {"CW": "VD", "ACW": "VE", "HCW": "VB"},
            "VD": {"CW": "VB", "ACW": "VC", "HCW": "VE"},
            "VB": {"CW": "VE", "ACW": "VD", "HCW": "VC"},
            "VE": {"CW": "VC", "ACW": "VB", "HCW": "VD"},
            "LH": {"CW": "LV", "ACW": "LH"},
            "LV": {"CW": "LH", "ACW": "LV"}
        }

        r, c, clockwise = action
        
        piece = state.board.get_value(r, c)
        if(clockwise != "init"):
            if (clockwise == "CW"):
                rotation = "CW"
            elif (clockwise == "ACW"):
                rotation = "ACW"
            else:
                rotation = "HCW"
            new_piece = rotations.get(piece, {}).get(rotation, piece)
        else:
            new_piece = piece
        new_board = Board(state.board.dim, [row[:] for row in state.board.content])
        new_board.content[r][c] = new_piece


        return PipeManiaState(new_board, state.prof + 1)
        
        

    def goal_test(self, state: PipeManiaState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO ver se 0,0 liga a 0,1 e a 1,0 e fazer dfs normal metendo numa pilha
        if state.dfs():
           return True
        else:
            return False


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
goal_node = depth_first_tree_search(problem)
#initial_state = PipeManiaState(board)
#print(problem.actions(initial_state))
print("Is goal?", problem.goal_test(goal_node.state))
print("Solution:\n", goal_node.state.board.print(), sep="")



#FB VC VD
#BC BB LV
#FB FB FE


