import pandas as pd
from pandas import ExcelFile
Color_Path = '/Users/suhong/Downloads/基于多种复杂约束条件下的智能排产附件/订单表.xlsx'
df = pd.read_excel (Color_Path)
print(df)
print


#define a function to convert a 颜色 (string) to the color shade
#color shade has five levels (from light to dark): 0,1,2,3,4
def get_shade_level(color):
    if color in ['PC透明色','本色']:
        return 0
    elif color in ['白色','金属色']:
        return 1
    elif color in ['浅灰色','浅蓝色','黄色']:
        return 2
    elif color == '其他':
        return 3
    elif color == '黑色':
        return 4


