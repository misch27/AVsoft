import json
from Main.ThreadWork import ThreadWork




if __name__ == '__main__':
    # read json file
    with open('document.json', 'r',encoding='utf-8') as doc:
        data = json.load(doc)
        ThreadWork.globArr = data.get("array")
        ThreadWork.maxGlobCount = len(data.get("array"))
        # start 3 Threads
        for x in range(0, 3):
            threadNew = ThreadWork()
            threadNew.setProp(str(data.get("url")), str(data.get("log")), str(data.get("pas")))
            threadNew.start()

