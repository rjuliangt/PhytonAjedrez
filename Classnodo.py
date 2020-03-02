# crearemos el nodo
class Node:
    def __init__(self,val_node):
        self.status = val_node
        self.top = None
        self.left = None
        self.right = None
        self.down = None

#para obtener los valores
    def get_status(self):
       # print (self.status)
       return f"{self.status}" 

    def get_node_top(self):
        return self.top
    
    def get_node_rigth(self):
        return self.right
    
    def get_node_down(self):
        return self.down
    
    def get_node_left(self):
        return self.left

#para modificar los valores
    def set_status(self,status):
        self.status = status

    def insert_top(self,top_nodo):
        self.top = Node(top_nodo)
              
    def insert_right(self,right_node):
        self.right = Node(right_node)
     
    def insert_down(self,down_node):
        self.down = Node(down_node)
    
    def insert_left(self,left_node):
        self.left = Node(left_node)
