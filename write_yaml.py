import ruamel.yaml as yl

with open('./.github/workflows/main.yml','r',encoding='utf-8') as f:
    content=yl.load(f.read(),Loader=yl.RoundTripLoader)
    print(content['jobs']['build']['steps'][4]['with']['body'])
    for i in range(1,13):
        content['jobs']['build']['steps'][3]['env']['FILE_NAME'] = i
        content['name']='spider'+str(i)
        content['jobs']['build']['steps'][4]['with']['body'] = 'file://site'+str(i)+'.txt'
        with open('.github/workflows/spider'+str(i)+'.yml', 'w', encoding='utf-8') as t:
            yl.dump(content, t, Dumper=yl.RoundTripDumper)