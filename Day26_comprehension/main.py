a = [i for i in range(10) if i % 2 == 0]
print(a)
b = [1,2,3,4,5]
c = [n for n in a if n in b]
print(c)
weather = {"Monday":12, "Wednesday": 30}
F = {day:temp*9/5+32 for day, temp in weather.items()}
print(F)
import pandas
dict1 = {"student":["A", "B", "C"], "score":[50, 60, 30]}
pandas_dataframe = pandas.DataFrame(dict1)
for idx, val in pandas_dataframe.iterrows():
    print(val)

my_list = [('a1', 'b1'), ('a2', 'b2'), ('a3', 'b3')]
search_element = 'a4'

# 첫 번째 원소만 고려하여 속하는지 판단
if any(search_element == item[0] for item in my_list):
    print(f"{search_element}은(는) 리스트에 속합니다.")
else:
    print(f"{search_element}은(는) 리스트에 속하지 않습니다.")