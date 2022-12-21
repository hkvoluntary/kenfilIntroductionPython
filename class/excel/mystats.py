import openpyxl
import statistics as stats

book = openpyxl.load_workbook('numbers.xlsx', data_only=True)

sheet = book.active

rows = sheet.rows
values = []


for row in rows:
    
    #print(row)
    for cell in row:
    #    print(cell)
        values.append(cell.value)
        pass
    pass

print("Number of values: {0}".format(len(values)))
print("Sum of values: {0}".format(sum(values)))
print("Minimum value: {0}".format(min(values)))
print("Maximum value: {0}".format(max(values)))
print("Mean: {0}".format(stats.mean(values)))
print("Median: {0}".format(stats.median(values)))
print("Standard deviation: {0}".format(stats.stdev))
print("Variance: {0}".format(stats.variance(values)))