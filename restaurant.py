import pandas
try:
    data = pandas.read_csv("log.csv")

    if len(data.drop_duplicates()) != len(data):
        raise Exception("DUPLICATE FOUND")

    lst = list(data['foodmenu_id'])

    lst_1=[(lst.count(x),x) for x in set(lst)]
    lst_1.sort(reverse=True)
    top_3 = [str(i[1]) for i in lst_1[:3]]
    print("These are the top 3 dishes :-", ", ".join(top_3))
except Exception as e:
    print(e)

