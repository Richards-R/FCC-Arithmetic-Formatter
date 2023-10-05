def arithmetic_arranger(problems, resultsDisplay):

    problemLength = len(problems)
    #print(problemLength)

    operandTop = ""
    operandLow = ""
    result = 0
    underRule = ""
    operandTopRow = ""
    operandLowRow = ""
    underRuleRow = ""
    resultRow = ""

    for equation in problems:      

        #print(equation)
       
        operator = "+"
        equationStr = equation
        for character in equationStr:
            if character == "-":
              operator = character
        #print(operator)
               
        operatorPosition = equationStr.find(operator)
        #print(operatorPosition)
    
        operandTop = equationStr[:operatorPosition].strip()
        operandLow = equationStr[operatorPosition +1:].strip()       
        #print(operandTop)
        #print(operandLow)
      
        
        if resultsDisplay == True:
            if operator == "+":
                result = int(operandTop) + int(operandLow)
            elif operator == "-":
                result = int(operandTop) - int(operandLow)
        
        
        if int(result) < 0:
          result = "   " + str(result)
        else:
          result = "    " + str(result)
      
        #compare lengths of operands, and white space to left side of shortest acrdg to diff

        longestOperandLength = 0
        diff = len(operandTop) - len(operandLow)
        #print(diff)
        if diff > 0:
            longestOperandLength = len(operandTop)
            while diff > 0:
                operandLow = " " + operandLow
                diff = diff - 1
    
        elif diff < 0:
            longestOperandLength = len(operandLow)
            while diff*-1 > 0:
                operandTop = " " + operandTop
                diff = diff + 1
        
        operandTop = "    " + operandTop
        operandLow = "  " + operator + " " + operandLow
    
        
        #while longestOperandLength > 0:
            #underRule = underRule + "-"
            #longestOperandLength = longestOperandLength - 1
        
        # print(operandTop)
        #print(operandLow)
        #print(underRule)
        #if resultsDisplay == True:
            #print(resultRow)
    
        #print(problems)
    
        
        operandTopRow = operandTopRow + operandTop
        operandLowRow = operandLowRow + operandLow
                  
        resultRow = resultRow + str(result)

    print(operandTopRow)
    print(operandLowRow)
    underRuleLength = len(operandTopRow)
    while underRuleLength > 0:
        underRuleRow = underRuleRow + "-"
        underRuleLength = underRuleLength - 1
    print(underRuleRow)
    if resultsDisplay == True:
        print(resultRow)
    return