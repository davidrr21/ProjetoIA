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

profundidade = 0

class PipeManiaState:
    state_id = 0

    def __init__(self, board, prof, locked_pieces):
        self.board = board
        self.prof = prof
        self.locked_pieces = locked_pieces
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

        return Board(dim, content)

    def print(self):
        result = "\n".join(" ".join(row) for row in self.content)
        return result
    
    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        locked_pieces = [["unlock" for _ in range(board.dim)] for _ in range(board.dim)]
        self.initial = PipeManiaState(board, profundidade, locked_pieces)

        

    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        #Listar em tuplos todas as ações possiveis a realizar num tabuleiro de dimensão nxn tendo em conta a posição das peças
        actions = []        
        dim = state.board.dim
        flag = False

        if(state.prof < (dim * dim)):
            r = state.prof // dim
            c = state.prof % dim
            
            profundidade_lock = state.prof
            while(1):
                if(state.locked_pieces[r][c] == "unlock"):
                    piece = state.board.get_value(r, c)
                    if piece in ["FC", "FD", "FB", "FE"]:
                        if(r == 0 and c == 0):##canto superior esquerdo
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FD"))
                        elif(r == 0 and c == dim - 1): ##canto superior direito
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FE"))
                        elif(r == dim - 1 and c == 0): ##canto inferior esquerdo
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FD"))
                        elif(r == dim - 1 and c == dim - 1): ##canto inferior direito
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FE"))
                        elif(r == 0): ##Primeira linha
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FD"))
                        elif(r == dim - 1): ##Ultima linha
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FD"))
                        elif(c == 0): ##Primeira coluna
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FB"))
                        elif(c == dim - 1): ##Ultima coluna
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FB"))                        
                        else:
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FE"))
                        flag = True
                    elif piece in ["BC", "BD", "BB", "BE"]:
                        if(piece == "BB" and r == 0):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "BC" and r == dim - 1):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "BD" and c == 0):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "BE" and c == dim - 1):
                            state.locked_pieces[r][c] = "lock"
                        else:
                            ##BC
                            if(r == 0): ##Primeira linha
                                actions.append((r, c, "BB"))
                            elif(r == dim - 1): ##Ultima linha
                                actions.append((r, c, "BC"))
                            elif(c == 0): ##Primeira coluna
                                actions.append((r, c, "BD"))
                            elif(c == dim - 1): ##Ultima coluna
                                actions.append((r, c, "BE"))
                            else:
                                actions.append((r, c, "BC"))
                                actions.append((r, c, "BD"))
                                actions.append((r, c, "BB"))
                                actions.append((r, c, "BE"))
                            flag = True
                    elif piece in ["VC", "VD", "VB", "VE"]:
                        if(piece == "VB" and (r == 0 and c == 0)):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "VE" and (r == 0 and c == dim - 1)):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "VD" and (r == dim - 1 and c == 0)):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "VC" and (r == dim - 1 and c == dim - 1)):
                            state.locked_pieces[r][c] = "lock"
                        else:
                            if(r == 0 and c == 0): ##canto superior esquerdo
                                actions.append((r, c, "VB"))
                            elif(r == 0 and c == dim - 1): ##canto superior direito
                                actions.append((r, c, "VE"))
                            elif(r == dim - 1 and c == 0): ##canto inferior esquerdo
                                actions.append((r, c, "VD"))
                            elif(r == dim - 1 and c == dim - 1): ##canto inferior direito
                                actions.append((r, c, "VC"))
                            elif(r == 0): ##Primeira linha
                                actions.append((r, c, "VB"))
                                actions.append((r, c, "VE"))
                            elif(r == dim - 1): ##Ultima linha
                                actions.append((r, c, "VC"))
                                actions.append((r, c, "VD"))
                            elif(c == 0): ##Primeira coluna
                                actions.append((r, c, "VB"))
                                actions.append((r, c, "VD"))
                            elif(c == dim - 1): ##Ultima coluna
                                actions.append((r, c, "VC"))
                                actions.append((r, c, "VE"))
                            else:
                                actions.append((r, c, "VC"))
                                actions.append((r, c, "VD"))
                                actions.append((r, c, "VB"))
                                actions.append((r, c, "VE"))
                            flag = True
                    elif piece in ["LH", "LV"]:
                        if(piece == "LH" and (r == 0 or r == dim - 1)):
                            state.locked_pieces[r][c] = "lock"
                        elif(piece == "LV" and (c == 0 or c == dim -1)):
                            state.locked_pieces[r][c] = "lock"
                        else:
                            if(r == 0): ##Primeira linha
                                actions.append((r, c, "LH"))
                            elif(r == dim - 1): ##Ultima linha
                                actions.append((r, c, "LH"))
                            elif(c == 0): ##Primeira coluna
                                actions.append((r, c, "LV"))
                            elif(c == dim - 1): ##Ultima coluna
                                actions.append((r, c, "LV"))
                            else:
                                actions.append((r, c, "LH"))
                                actions.append((r, c, "LV"))
                            flag = True
                    
                    if(flag):
                        break
                
                profundidade_lock += 1
                if(profundidade_lock < (dim * dim)):
                    r = (profundidade_lock) // dim
                    c = (profundidade_lock) % dim
                else:
                    break
        print("ações: ", actions)
        return actions


    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO

        r, c, position = action
        
        new_piece = position
        
        #novo board
        new_board = Board(state.board.dim, [row[:] for row in state.board.content])
        new_board.content[r][c] = new_piece
        new_locked_pieces = [row[:] for row in state.locked_pieces]

        it = 1
        dim_total = state.board.dim * state.board.dim
        if((state.prof + 1) < dim_total):#caso seja a última peça do tabuleiro não pode estar trancada e vir parar aqui porque já não lhe deia mais ações no actions
            r = (state.prof + 1) // state.board.dim
            c = (state.prof + 1) % state.board.dim
            while(1):
                if(state.locked_pieces[r][c] == "unlock"):
                    break
                it += 1

        return PipeManiaState(new_board, state.prof + it, new_locked_pieces)
        
        

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
#goal_node.state.board.print()
print("Is goal?", problem.goal_test(goal_node.state))
print("Solution:\n", goal_node.state.board.print(), sep="")