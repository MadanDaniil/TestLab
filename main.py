# Необходимо написать программу, которая будет считывать последовательности измерений.
# В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести отсортированный по убыванию список
# этих макс значений, разделенных символом “;”.
# Во входных данных в первой строке будет задано целое положительное число –
# сколько записей нужно обработать, причем самих записей может быть больше чем это число, это нужно учесть.
# Значения в рамках одной записи разделены пробелом, минимальное число значений в записи – 1.
# Записи разделены переводом строки.

cnt = input()
lst = []
i = 0
while data := input():
    i+=1
    if(i <= int(cnt)):
        lst.append(max(data))
lst.sort(reverse=1)
joined = ";".join(lst)
print(joined)