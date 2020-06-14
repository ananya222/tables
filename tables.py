def find_table(which_table,how_many,operator):
    table=[]
    result=0

    for i in range(0,how_many+1):
        if(operator=='+'):
            result=which_table+i
            table.append(str(which_table)+'+'+str(i)+'='+str(result))
        if(operator=='-'):
            result=which_table-i
            table.append(str(which_table)+'-'+str(i)+'='+str(result))
        if(operator=='*'):
            result=which_table*i
            table.append(str(which_table)+'*'+str(i)+'='+str(result))
        if(operator=='/' and i>0):
            result=float(which_table)/float(i)
            table.append(str(which_table)+'/'+str(i)+'='+str(result))

    return table

which_table=5
how_many=13
operator='+'
table=find_table(which_table,how_many,operator)
for row in table:
    print(row)
