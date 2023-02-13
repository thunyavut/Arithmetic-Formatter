def arithmetic_arranger(problems, Bool=False):
    firstList = []
    secList = []
    dash = []
    result = []

    # Problem limit is 4
    if len(problems) > 5: 
        return 'Error: Too many problems.'

    # Check Error each given problems
    for i in problems:
        sp = i.split()
        
        if len(sp) != 3:
            return 'Error: Enter only 2 operand and 1 operator in between.'
 
        elif len(sp[0]) > 4 or len(sp[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
           
        elif '+' not in sp[1] and '-' not in sp[1]:
            #print(sp[1])
            return 'Error: Operator must be \'+\' or \'-\'.'
           
        try: 
            type(int(sp[0])) == int
            type(int(sp[2])) == int
        except:
            return 'Error: Numbers must only contain digits.'
           
        
        # When every item is valid
        if len(sp[0]) > len(sp[2]):
            maxLen = (len(sp[0])) + 1 
        else:
            maxLen = (len(sp[2])) + 1
        
        firstList.append(' ' + ' ' * (maxLen - (len(sp[0]))) + sp[0])
        secList.append(sp[1] + ' ' * (maxLen - (len(sp[2]))) + sp[2])
        dash.append('-' + '-' * (maxLen))

        if Bool == True:
            if sp[1] == '+':
                result.append(' ' + ' ' * (maxLen - (len(str(int(sp[0]) + int(sp[2]))))) + str((int(sp[0]) + int(sp[2]))))
            else:
                if int(sp[0]) - int(sp[2]) < 0:
                    result.append(' ' + ' ' * (maxLen - (len(str(int(sp[0]) - int(sp[2]))))) + str(int(sp[0]) - int(sp[2])))
                else:
                    result.append(' ' + ' ' * (maxLen - (len(str(int(sp[0]) - int(sp[2]))))) + str((int(sp[0]) - int(sp[2]))))

    if Bool == True:
        arranged_problems = '    '.join(firstList) + '\n' + '    '.join(secList) + '\n' + '    '.join(dash) + '\n' + '    '.join(result)
    else:
        arranged_problems = '    '.join(firstList) + '\n' + '    '.join(secList) + '\n' + '    '.join(dash)
    return arranged_problems
            

