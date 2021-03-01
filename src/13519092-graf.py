class Node:
    #kelas yang merepresentasikan simpul dari graf
    def __init__(self, name, din):
        #name: nama dari simpul
        #din: derajat masuk dari simpul
        self.name=name
        self.din=din

class Edge:
    #kelas yang merepresentasikan sisi dari graf
    def __init__(self, src, dest):
        #src: simpul asal dari sisi
        #dest: simpul tujuan dari sisi
        self.src = src
        self.dest = dest

def getNode(name, arrNode):
    #fungsi selektor yang mengembalikan simpul yang bernama name dari arrNode
    for i in range(len(arrNode)):
        #melakukan iterasi pada arrNode hingga ditemukan simpul yang bernama name
        if (arrNode[i].name==name):
            return(arrNode[i])

def delNode(node, arrNode):
    #menghapus simpul node pada arrNode apabila ditemukan
    done = False  #atribut bertipe boolean yang bernilai true apabila simpul node telah dihapus
    j = 0
    #melakukan while loop pada arrNode hingga seluruh elemen arrNode selesai dijelajahi atau node telah dihapus
    while j < len(arrNode) and not done:
        if (arrNode[j]==node):
            arrNode.pop(j)
            done=True
        else:
            j+=1

def delEdge(arrEdge,arrNode,src):
    #menghapus sisi yang memiliki simpul asal = src dari arrEdge dan mengurangi derajat dari simpul tujuan pada arrNode
    indexdel=[]  #array yang menyimpan indeks dari elemen arrEdge yang hendak dihapus
    for i in range(len(arrEdge)):
        #melakukan iterasi pada arrEdge dan menambahkan indeks elemen dengan simpul asal = src ke dalam indexdel
        if(arrEdge[i].src==src):
            indexdel.append(i)
            for n in range(len(arrNode)):
                #melakukan iterasi pada arrNode untuk mengurangi derajat dari simpul tujuan
                if(arrNode[n]==arrEdge[i].dest):
                    arrNode[n].din-=1
    j=0
    k=0
    while j<len(indexdel):
        #menghapus edge dari arrEdge pada indeks yang disimpan di array indexdel
        arrEdge.pop(indexdel[j]+k)
        #untuk setiap penghapusan, karena elemen berkurang, sehingga indeks untuk iterasi selanjutnya dikurangi dengan 1
        k-=1
        j+=1

def printNode(node):
    #menampilkan simpul node ke layar dengan format "(name,din)"
    print("(" + str(node.name) + "," + str(node.din) + ")", end="")

def printEdge(edge):
    #menampilkan sisi edge ke layar dengan format "{(name_src,din_src),(name_dest,din_dest)}"
    print("{", end="")
    printNode(edge.src)
    print(",", end="")
    printNode(edge.dest)
    print ("}")
