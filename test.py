import json

def loading():
    try:
        with open('stu.json','r',encoding='utf-8') as f:
            return json.load(f)

    except FileNotFoundError:
        print("파일없어ㅠㅠ")

#p.284
def add(data):
    with open('stu.json','w',encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=2)
            

#print(loading())
datas=[{"name":"Tom","score":100},
 {"name":"Juli","score":80}
]
add(datas)
print('저장')