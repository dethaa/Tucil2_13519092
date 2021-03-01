io = __import__('13519092-inoutput')
g = __import__('13519092-graf')

def dnc(arrEdge,arrNode,arrUrut):
    #prosedur rekursif decrease and conquer
    if (len(arrEdge)==0):
        #BASIS: semua simpul yang tersisa memiliki derajat masuk 0
        if (len(arrNode) > 0):
            # apabila sisi habis dan masih ada simpul yang tersisa, simpul tersebut dimasukkan ke arrLast
            arrLast = []  # menyimpan simpul-simpul yang akan dimasukkan sebagai elemen terkakhir arrUrut
            for i in range(len(arrNode)):
                arrLast.append(arrNode[i].name)
            arrUrut.append(arrLast)
    else:
        #REKURSIF: mencari simpul yang berderajat masuk 0 dan menghapusnya kemudian menyesuaikan derajat masuk dari simpul tujuan
        indexTake = []  # menyimpan indeks dari mata kuliah yang dapat diambil pada arrNode
        arrTake = []  # menyimpan simpul-simpul dari mata kuliah yang dapat diambil pada semester tertentu
        for i in range(len(arrNode)):
            # melakukan iterasi pada arrNode menambahkan indeks simpul yang memiliki derajat masuk 0 ke array indexTake
            if (arrNode[i].din == 0):
                indexTake.append(i)
        j = 0
        k = 0
        while j < len(indexTake):
            # memasukkan simpul mata kuliah yang bisa diambil ke dalam array arrTake
            arrTake.append(arrNode[indexTake[j] + k].name)
            # menghapus sisi pada arrEdge dan simpul pada arrNode yang bersesuaian
            g.delEdge(arrEdge, arrNode, arrNode[indexTake[j] + k])
            g.delNode(arrNode[indexTake[j] + k], arrNode)
            k -= 1  # untuk setiap penghapusan, jumlah elemen berkurang sehingga indeks untuk iterasi selanjutnya dikurangi 1
            j += 1
        # arrTake dimasukkan sebagai elemen baru pada array of array arrUrut
        arrUrut.append(arrTake)
        #pemanggilan prosedur rekursif
        dnc(arrEdge,arrNode,arrUrut)

if __name__ == '__main__':
    #menerima input nama file test dari pengguna
    filename = input("Masukkan nama file test: ")
    #memasukkan data seluruh mata kuliah beserta prereq masing-masing ke dalam array of array inArr
    inArr=io.inputfile(filename)
    numCourse = len(inArr)  #menyimpan jumlah mata kuliah
    #menyimpan simpul yang merepresentasikan mata kuliah ke dalam array of Node arrNode
    arrNode = [g.Node for _ in range(numCourse)]
    for i in range(numCourse):
        arrNode[i] = g.Node(inArr[i][0], len(inArr[i]) - 1)
    #menyimpan simsi yang merepresentasikan pasangan mata kuliah dan prereq-nya ke dalam array of Edge arrEdge
    arrEdge = []
    for i in range(numCourse):
        if (len(inArr[i]) != 1):
            for j in range(1, len(inArr[i])):
                arrEdge.append(g.Edge(g.getNode(inArr[i][j], arrNode), g.getNode(inArr[i][0], arrNode)))

    arrUrut=[] #inisialisasi array of array arrUrut yang menyimpan mata kuliah yang diambil per semesternya (dipisahkan oleh indeks)
    dnc(arrEdge, arrNode, arrUrut) #melakukan decrease dan conquer pada arrEdge dan arrNode, hasilnya disimpan pada arrUrut
    io.output(arrUrut)
