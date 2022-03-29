import ruamel.yaml as yl

with open('./.github/workflows/main.yml','r',encoding='utf-8') as f:
    print(yl.safe_load(f.read()))