import multiprocessing;
import requests;

def downloadFile(url,name) :
    print(f"start donwloading {name}")
    respose = requests.get(url)   
    open(f"file/file{name}.jpg", "wb").write(respose.content)
    print(f"finish download {name}")


url = "https://picsum.photos/2000/3000"

for i in range(5):
    p1 = multiprocessing.Process(target=downloadFile, args=[url,i])
    # downloadFile(url,i)
    p1.start()
