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
Left = ["FD", "BC", "BB", "BD", "VB", "VD", "LH"]
Right = ["FE", "BC", "BB", "BE", "VC", "VE", "LH"]
Down = ["FC", "BC", "BE", "BD", "VC", "VD", "LV"]
Up = ["FB", "BB", "BE", "BD", "VB", "VE", "LV"]

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

    def __init__(self, dim, content, locked_pieces):
        self.dim = dim
        self.content = content
        self.locked_pieces = locked_pieces


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


        locked_pieces = [["unlock" for _ in range(dim)] for _ in range(dim)]
        
        #completar caso possível
        while(1):#flag começa a true e cada vez que rodo uma peça torno-a a false logo vou ter que percorrer o tabuleiro todo outra vez pois podem surgir novas inferências
            flag = True
            it = 0
            done = 0
            while(it != (dim*dim)):
                r = it // dim
                c = it % dim

                if(locked_pieces[r][c] == "unlock"):
                    piece = content[r][c]
                    if piece in ["FC", "FD", "FB", "FE"]:
                        if(r == 0 and c == 0):##canto superior esquerdo
                            #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or(locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == 0 and c == dim - 1): ##canto superior direito
                            #left
                            if((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == dim - 1 and c == 0): ##canto inferior esquerdo
                            #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #up
                            elif((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == dim - 1 and c == dim - 1): ##canto inferior direito
                            #left
                            if((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #up
                            elif((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == 0): ##Primeira linha
                            #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and( locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #left
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and( locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #primeira linha
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and( locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == dim - 1):#Última linha
                             #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and( locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #left
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and( locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #última linha
                            elif((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and( locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(c == 0): ##Primeira coluna
                            #up
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)) and( locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and( locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False 
                            #primeira coluna
                            elif((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and( locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(c == dim - 1):#última coluna
                            #up
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)) and( locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and( locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #última coluna
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and( locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        else:#caso em que a peça está no meio
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)))):
                                content[r][c] = "FB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "FE"
                                locked_pieces[r][c] = "lock"
                                flag = False               
                    elif piece in ["VC", "VD", "VB", "VE"]:
                        if(r == 0 and c == 0):
                            content[r][c] = "VB"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(r == 0 and c == dim - 1):
                            content[r][c] = "VE"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(r == dim - 1 and c == 0):
                            content[r][c] = "VD"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(r == dim - 1 and c == dim - 1):
                            content[r][c] = "VC"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(r == 0): ##Primeira linha
                            #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))):
                                content[r][c] = "VB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #left
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))):
                                content[r][c] = "VE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(r == dim - 1): ##Ultima linha
                            #right
                            if((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) or (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))):
                                content[r][c] = "VD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #left
                            elif((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))):
                                content[r][c] = "VC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        elif(c == 0): ##Primeira coluna
                            #up
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))):
                                content[r][c] = "VD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))):
                                content[r][c] = "VB"
                                locked_pieces[r][c] = "lock"
                                flag = False 
                        elif(c == dim - 1): ##Ultima coluna
                            #up
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))):
                                content[r][c] = "VC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            #down
                            elif((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))):
                                content[r][c] = "VE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                        else:#caso em que a peça está no meio
                            if(((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))) or
                                ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))) or 
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "VC"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up))) or
                                ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)))):
                                content[r][c] = "VD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)))):
                                content[r][c] = "VB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)))):
                                content[r][c] = "VE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                    #quando tenho outro tipo de peças B's ou L's mas que estão no meio
                    elif piece in ["LH", "LV"]:
                        if(r == 0 or r == dim - 1):
                            content[r][c] = "LH"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(c == 0 or c == dim -1):
                            content[r][c] = "LV"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        else:#meio
                            if((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) or 
                                (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) or
                                (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)) or 
                                (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))):
                                content[r][c] = "LV"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif((locked_pieces[r][c+1] == "lock" and (content[r][c+1]  in Right)) or
                                (locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) or
                                (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)) or
                                (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))):
                                content[r][c] = "LH"
                                locked_pieces[r][c] = "lock"
                                flag = False
                    elif piece in ["BC", "BB", "BE", "BD"]:
                        if(r == 0):
                            content[r][c] = "BB"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(r == dim - 1):
                            content[r][c] = "BC"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(c == 0):
                            content[r][c] = "BD"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        elif(c == dim - 1):
                            content[r][c] = "BE"
                            locked_pieces[r][c] = "lock"
                            flag = False
                        else:#meio
                            if(((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))) or
                                ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right))) or
                                ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] not in Right)))):
                                content[r][c] = "BE"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or                        
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up))) or
                                ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right))) or
                                ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] not in Up)))):
                                content[r][c] = "BB"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))) or
                                ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left))) or
                                ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] in Down)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right))) or
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] not in Left)))):
                                content[r][c] = "BD"
                                locked_pieces[r][c] = "lock"
                                flag = False
                            elif(((locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)) and (locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up))) or
                                ((locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))) or                        
                                ((locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down))) or
                                ((locked_pieces[r-1][c] == "lock" and (content[r-1][c] in Up)) and (locked_pieces[r][c-1] == "lock" and (content[r][c-1] in Left)) and (locked_pieces[r][c+1] == "lock" and (content[r][c+1] in Right))) or 
                                ((locked_pieces[r+1][c] == "lock" and (content[r+1][c] not in Down)))):
                                content[r][c] = "BC"
                                locked_pieces[r][c] = "lock"
                                flag = False        
                else:
                    done +=1   
                it += 1
            if(done == (dim*dim)):
                flag = True
            if(flag):
                break

        return Board(dim, content, locked_pieces)

    def print(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if j != self.dim - 1:
                    print(self.content[i][j], end="\t")
                else:
                    print(self.content[i][j])
    
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
        actions = []        
        dim = state.board.dim

        if(state.prof < (dim * dim)):
            r = state.prof // dim
            c = state.prof % dim
            if(state.board.locked_pieces[r][c] == "unlock"):#vou explorar peças ainda não bloqueadas
                piece = state.board.get_value(r, c)
                if piece in ["FC", "FD", "FB", "FE"]:
                    if(r == 0 and c == 0):##canto superior esquerdo
                        #if(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):#tem direita
                        #    actions.append((r, c, "FD"))
                        #elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):#tem baixo
                        #    actions.append((r, c, "FB"))
                        #else:    
                        actions.append((r, c, "FB"))
                        actions.append((r, c, "FD"))
                    elif(r == 0 and c == dim - 1): ##canto superior direito
                        if(state.board.get_value(r, c-1) in Left and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))):
                            #não é possível ter esquerda e baixo simultaneamente
                            pass   
                        #elif(state.board.locked_pieces[r+1][c] == "lock" and state.board.get_value(r+1, c) in Down):#tem baixo
                        #    actions.append((r, c, "FB"))                     
                        elif(state.board.get_value(r, c-1) in Left):#tem esquerda
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r, c-1) not in Left):#não tem esquerda logo tem que ser baixo
                            actions.append((r, c, "FB"))
                        #else:
                        #    actions.append((r, c, "FB"))
                        #    actions.append((r, c, "FE"))
                    elif(r == dim - 1 and c == 0): ##canto inferior esquerdo
                        if(state.board.get_value(r-1, c) in Up and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):
                            #não é possível ter cima e direita simultaneamente
                            pass
                        #elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):
                        #    actions.append((r, c, "FD"))
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "FC"))
                        elif(state.board.get_value(r-1, c) not in Up):
                            actions.append((r, c, "FD"))
                        #else:
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FD"))
                    elif(r == dim - 1 and c == dim - 1): ##canto inferior direito
                        if((state.board.get_value(r-1, c) in Up )and (state.board.get_value(r, c-1) in Left)):
                            #não é possível ter cima e esquerda simultaneamente
                            pass
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.get_value(r, c-1) not in Left)):
                            #não é possível ligar
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r, c-1) not in Left):
                            actions.append((r, c, "FC"))
                        #else:
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FE"))
                    elif(r == 0): ##Primeira linha
                        if(((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                           ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)))):
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FB"))
                        elif(state.board.get_value(r, c-1) not in Left):
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FD"))
                        #else:
                        #    actions.append((r, c, "FE"))
                        #    actions.append((r, c, "FB"))
                        #    actions.append((r, c, "FD"))
                    elif(r == dim - 1): ##Ultima linha
                        if(((state.board.get_value(r, c-1) in Left) and (state.board.get_value(r-1, c) in Up)) or
                           ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))) or
                           ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)))):
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "FC"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.get_value(r-1, c) not in Up)):
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FC"))
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r, c-1) not in Left):
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FC"))
                        elif(state.board.get_value(r-1, c) not in Up):
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FE"))
                        elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FC"))
                        #else:
                        #    actions.append((r, c, "FE"))
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FD"))
                    elif(c == 0): ##Primeira coluna
                        if(((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                           ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)))):
                            pass
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "FC"))
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FB"))
                        elif(state.board.get_value(r-1, c) not in Up):
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FD"))
                        #else:
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FD"))
                        #    actions.append((r, c, "FB"))
                    elif(c == dim - 1): ##Ultima coluna
                        if(((state.board.get_value(r, c-1) in Left) and (state.board.get_value(r-1, c) in Up)) or
                           ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                           ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)))):
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "FC"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FC"))
                        elif((state.board.get_value(r, c-1) not in Left) and (state.board.get_value(r-1, c) not in Up)):
                            actions.append((r, c, "FB"))
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FE"))
                        elif(state.board.get_value(r, c-1) not in Left):
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FC"))
                        elif(state.board.get_value(r-1, c) not in Up):
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FE"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down)):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FB"))
                        #else:
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FE"))
                        #    actions.append((r, c, "FB"))                        
                    else:#interior
                        if(((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left)) or
                           ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))) or
                           ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                           ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))) or
                           ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)))):
                            #não é possível por isso cortar este ramo
                            pass
                        elif(state.board.get_value(r-1, c) in Up):#só de cima
                            actions.append((r, c, "FC"))
                        elif(state.board.get_value(r, c-1) in Left):#só da esquerda
                            actions.append((r, c, "FE"))
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            pass
                        elif((state.board.get_value(r, c-1) not in Left) and 
                             (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            pass
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.get_value(r, c-1) not in Left) and 
                             (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FB"))
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.get_value(r, c-1) not in Left) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.get_value(r, c-1) not in Left)):
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FB"))
                        elif((state.board.get_value(r, c-1) not in Left) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FD"))
                        elif((state.board.get_value(r, c-1) not in Left) and 
                             (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FB"))
                        elif((state.board.get_value(r-1, c) not in Up) and 
                             (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FB"))
                        elif((state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)) and 
                             (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            actions.append((r, c, "FC"))
                            actions.append((r, c, "FE"))
                        elif((state.board.get_value(r-1, c) not in Up)):
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FE"))
                        elif((state.board.get_value(r, c-1) not in Left)):
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FC"))
                        elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FB"))
                            actions.append((r, c, "FC"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down)):
                            actions.append((r, c, "FE"))
                            actions.append((r, c, "FD"))
                            actions.append((r, c, "FC"))
                        #else:
                        #    actions.append((r, c, "FC"))
                        #    actions.append((r, c, "FD"))
                        #    actions.append((r, c, "FB"))
                        #    actions.append((r, c, "FE"))
                elif piece in ["VC", "VD", "VB", "VE"]:
                    if(r == 0): ##Primeira linha
                        if((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)) or
                           (state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "VE"))
                        elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):
                            actions.append((r, c, "VB"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VE"))
                        else:
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VE"))
                    elif(r == dim - 1): ##Ultima linha
                        if((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)) or
                           (state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right))):
                            pass
                        elif(state.board.get_value(r, c-1) in Left):
                            actions.append((r, c, "VC"))
                        elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):
                            actions.append((r, c, "VD"))
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VD"))
                        else:
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VD"))
                    elif(c == 0): ##Primeira coluna
                        if((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)) or
                           (state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            pass
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "VD"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):
                            actions.append((r, c, "VB"))
                        else:
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VD"))
                    elif(c == dim - 1): ##Ultima coluna
                        if((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)) or
                           (state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))):
                            pass
                        elif(state.board.get_value(r-1, c) in Up):
                            actions.append((r, c, "VC"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):
                            actions.append((r, c, "VE"))
                        else:
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VE"))
                    else:#interior
                        if(((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                            ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))) or
                            ((state.board.get_value(r-1, c) not in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down))) or
                            ((state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)))):
                            pass
                        elif((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left)):#de cima e da esquerda
                            actions.append((r, c, "VC"))
                        elif((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):#de cima e da direita
                            actions.append((r, c, "VD"))
                        elif((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))):#de esuqerda e baixo
                            actions.append((r, c, "VE"))
                        elif(state.board.get_value(r-1, c) in Up):#só de cima
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VD"))
                        elif(state.board.get_value(r, c-1) in Left):#só da esquerda
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VE"))
                        elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VE"))
                        elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VD"))
                        #rever estes 3 elif's em baixo disto
                        elif((state.board.get_value(r-1, c) not in Up) and (state.board.get_value(r, c-1) in Left)):#nem da esquerda nem de cima
                            actions.append((r, c, "VB"))
                        else:
                            actions.append((r, c, "VC"))
                            actions.append((r, c, "VD"))
                            actions.append((r, c, "VB"))
                            actions.append((r, c, "VE"))
                #considerar inferências para caso a peça esteja no meio
                elif piece in ["BC", "BD", "BB", "BE"]:
                    if(((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))) or
                    ((state.board.get_value(r-1, c) not in Up) and (state.board.get_value(r, c-1) not in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) not in Right)) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) not in Down)))):
                        pass
                    elif((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):#tem pela esquerda, por cima e pela direita
                        actions.append((r, c, "BC"))
                    elif((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))):#tem por cima, pela esquerda e por baixo
                        actions.append((r, c, "BE"))
                    elif((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):#tem pela esquerda, por baixo e pela direita
                        actions.append((r, c, "BB"))
                    elif((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):#tem por cima, pela direita e por baixo
                        actions.append((r, c, "BD"))
                    elif((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left)):#tem pela esquerda e por cima 
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BE"))
                    elif((state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)) and (state.board.get_value(r-1, c) in Up)):#tem pela direita e por cima
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BD"))
                    elif((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right))):#tem pela esquerda e pela direita
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BB"))
                    elif((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down))):#tem por cima e por baixo
                        actions.append((r, c, "BE"))
                        actions.append((r, c, "BD"))
                    elif(state.board.get_value(r-1, c) in Up):#tem por cima
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BD"))
                        actions.append((r, c, "BE"))
                    elif(state.board.get_value(r-1, c) in Up):#tem pela esquerda
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BB"))
                        actions.append((r, c, "BE"))
                    elif(state.board.locked_pieces[r][c+1] == "lock" and (state.board.get_value(r, c+1) in Right)):#tem pela direita
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BD"))
                        actions.append((r, c, "BB"))
                    elif(state.board.locked_pieces[r+1][c] == "lock" and (state.board.get_value(r+1, c) in Down)):#tem por baixo
                        actions.append((r, c, "BB"))
                        actions.append((r, c, "BD"))
                        actions.append((r, c, "BE"))
                    else:
                        actions.append((r, c, "BC"))
                        actions.append((r, c, "BD"))
                        actions.append((r, c, "BB"))
                        actions.append((r, c, "BE"))
                elif piece in ["LH", "LV"]:
                    if(((state.board.get_value(r-1, c) in Up) and (state.board.get_value(r, c-1) in Left)) or
                       ((state.board.get_value(r-1, c) in Up) and (state.board.locked_pieces[r][c+1] == "lock" and state.board.get_value(r, c+1) in Right)) or
                       ((state.board.get_value(r, c-1) in Left) and (state.board.locked_pieces[r+1][c] == "lock" and state.board.get_value(r+1, c) in Down))):
                            #não é possível por isso cortar este ramo
                            pass
                    elif(state.board.get_value(r-1, c) in Up):
                        actions.append((r, c, "LV"))
                    elif(state.board.get_value(r, c-1) in Left):
                        actions.append((r, c, "LH"))
                    elif(state.board.locked_pieces[r][c+1] == "lock" and state.board.get_value(r, c+1) in Right):
                        actions.append((r, c, "LH"))
                    elif(state.board.locked_pieces[r+1][c] == "lock" and state.board.get_value(r+1, c) in Down):
                        actions.append((r, c, "LV"))

                    #else:
                    #    actions.append((r, c, "LH"))
                    #    actions.append((r, c, "LV"))                
            else:#devolve a única ação da peça bloqueada que é ela mesma
                actions.append((r, c, state.board.get_value(r, c)))
        return actions


    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO

        r, c, position = action
                
        #novo board
        new_board = Board(state.board.dim, [row[:] for row in state.board.content], [row[:] for row in state.board.locked_pieces])
        new_board.content[r][c] = position

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
<<<<<<< HEAD
#print(goal_node.state.board.print())
=======
goal_node.state.board.print()
>>>>>>> 7edb0de (changes)
#print("Is goal?", problem.goal_test(goal_node.state))
#print("Solution:\n", goal_node.state.board.print(), sep="")

#FB VC VD
#BC BB LV
#FB FB FE