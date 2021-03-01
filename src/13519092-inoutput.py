def inputfile(filename):
    #prosedur yang memproses hasil pembacaan filename.txt dan memasukkannya ke dalam array of array of string inArr
    #membaca input file test dan menyimpan hasil bacaan ke atribut file
    f=open("../test/"+filename,"r")
    file = f.read()
    clean = file
    #membersihkan karakter yang tidak diperlukan dan membuat batas "|" untuk memisahkan informasi antar simpul
    #hasil pembersihan dimasukkan ke dalam array tab
    old = [',', '.', '\n']
    new = ['', ' | ', '']
    for i in range(len(old)):
        clean = clean.replace(old[i], new[i])
    tab = clean.split()
    #menghitung jumlah "|" sebagai penanda jumlah mata kuliah dan memasukkannya ke dalam atribut numCourse
    numCourse = 0
    for i in range(len(tab)):
        if (tab[i] == '|'):
            numCourse += 1
    #mengelompokkan tiap elemen yang dibatasi "|" pada array tab dan memasukkannya ke dalam sebuah array
    #array tersebut dimasukkan lagi ke dalam sebuah aray of array inArr
    inArr = [[] for _ in range(numCourse)]
    counter = 0
    for i in range(len(tab)):
        if (tab[i] != "|"):
            inArr[counter].append(tab[i])
        else:
            counter += 1
    return (inArr)

def output(arrUrut):
    #prosedur yang menampilkan output ke layar berupa urutan pengambilan mata kuliah tiap semesternya berdasarkan arrUrut
    print("\nRencana Pengambilan Mata Kuliah")
    print("---------------------------------")
    for i in range(len(arrUrut)):
        print("Semester " + str(i+1) + ": ", end ="")
        for j in range(len(arrUrut[i])):
            if (j == len(arrUrut[i])-1):
                print(arrUrut[i][j])
            else:
                print(str(arrUrut[i][j]) + ", ", end="")












