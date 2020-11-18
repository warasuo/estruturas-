class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        # current = atual
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return

    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next
        return total

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def R_to_list(self, l):
        node_data = l
        current_node = self.head
        i = 0
        while current_node:
            current_node.data = l[i]
            i += 1
            current_node = current_node.next
        return

    def get(self, index):
        if index >= self.length() or index < 0:
            print("erro")
            return -1
        current_idx = 0
        current_node = self.head
        while current_node != None:
            if current_idx == index:
                v = current_node.data
                del current_node
                return v
            current_node = current_node.next
            current_idx += 1

    #Remoção por índice lab 1
    def remove_element(self, data, index):
        elemente = Node(data)
        p = index
        t = 0
        if self.get(index) == -1:
            print("erro")
            return
        else:
            t = self.get(index)

        current_node = self.head.next
        prev = self.head

        if index >= self.length() or index < 0:
            print("index nao esta na lista")
        elif index == 0:
            if t == elemente.data:
                self.head = self.head.next
            else:
                print("elemento nao coresponde ao indice")
            return

        while current_node.next:
            if current_node.data == elemente.data:
                break
            prev = prev.next
            current_node = current_node.next
        if t == prev.next.data:
            prev.next = current_node.next
        else:
            print(f"elemento :{prev.next.data} nao bate com  index {t - 1}")
        return
    def display(self):
        contents = self.head

        if contents is None:
            print("nao à elementos")

        while contents:
            print(contents.data)
            contents = contents.next
        print("---------------")

    #Ordenação simples lab1
    def sort(self):
        l = self.to_list()
        l = sorted(l)
        self.R_to_list(l)

    #ordenaçao
    def insertion_sort(lista, chave2=0):

        for i in range(1, len(lista)):

            chave = lista[i]

            k = i
            while k > 0 and chave < lista[k - 1]:
                lista[k] = lista[k - 1]

                k -= 1
            lista[k] = chave

#Selection Sort
def ordena_selecao(a):
    for index in range(0, len(a)):
        min = index

        for temp in range(index + 1, len(a)):
            if a[temp] < a[min]:
                min = temp
        a[index], a[min] = a[min], a[index]

#Bubble Sort
def ordena_bolha(lista):
    for final in range(len(lista), 0, -1):
        ordenador = False
        for atual in range(0,final - 1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]
                ordenador = True
            if not ordenador:
                break

#Merge Sort
def ordena_merge(lista):
    aux = lista[:]
    sort_m(lista, aux, 0, len(lista) - 1)

def sort_m(lista, aux, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) //2

    sort_m(lista, aux, inicio, meio)
    sort_m(lista, aux, meio + 1, fim)

    merge(lista, aux, inicio, fim)

def merge(lista, aux, inicio, fim):
    esqueda = inicio
    esqueda_fim = (inicio + fim) // 2
    direita = esqueda_fim + 1
    direita_fim = fim
    posicao = inicio

    while esqueda <= esqueda_fim or direita <= direita_fim:
        if esqueda > esqueda_fim:
            aux[posicao] = lista[direita]
            direita += 1
            posicao += 1
        elif direita > direita_fim:
            aux[posicao] = lista[esqueda]
            esqueda += 1
            posicao += 1
        elif lista[esqueda] < lista[direita]:
            aux[posicao] = lista[esqueda]
            esqueda += 1
            posicao += 1
        else:
            aux[posicao] = lista[direita]
            direita += 1
            posicao += 1
    for k in range(inicio, fim + 1):
        lista[k] = aux[k]

def quickSort(list):
   quickSortHelper(list, 0, len(list)-1)

def quickSortHelper(list,inicio,fim):
   if inicio < fim:

       meio = part(list, inicio, fim)

       quickSortHelper(list, inicio, meio - 1)
       quickSortHelper(list, meio + 1, fim)


def part(list, inicio, fim):
   pivotvalue = list[inicio]

   esquerda = inicio + 1
   direita = fim

   done = False
   while not done:

       while esquerda <= direita and list[esquerda] <= pivotvalue:
           esquerda = esquerda + 1

       while list[direita] >= pivotvalue and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           done = True
       else:
           temp = list[esquerda]
           list[esquerda] = list[direita]
           list[direita] = temp

   temp = list[inicio]
   list[inicio] = list[direita]
   list[direita] = temp


   return direita

list = LinkedList()

list.display()

list.append(6)
list.append(5)
list.append(4)
list.append(3)
list.append(2)
list.append(1)
list.display()
"""
print(f"o numero total de elementos na lista e: {list.length()}")
print(list.to_list())
print("----------")

print(list.get(2))
print("----------")
list.display()
list.sort()
list.remove_element(6, 5)

list.display()

print(list.get(0))
list.display()
"""
l = list.to_list()
list.display()
print(l)
#ordena_selecao(l)
#ordena_bolha(l)
#ordena_merge(l)
#quickSort(l)
print(l)
#list.display()