def arithmetic_arranger(problems, resultsDisplay=''):

    problemLength = len(problems)
    if problemLength > 5:
        return "Error: Too many problems."

    operandTop = ""
    operandLow = ""
    result = 0
    underRule = ""
    
    operandTopRow = ""
    operandLowRow = ""
    underRuleRow = ""
    resultRow = ""

    for equation in problems:      
        operator = "+"
        equationStr = equation
        for character in equationStr:
            if character == "-":
              operator = character
            elif character == "+":
              operator = character
            elif character == "/":
              return "Error: Operator must be '+' or '-'."
            elif character == "*":
              return "Error: Operator must be '+' or '-'."
                       
        operatorPosition = equationStr.find(operator)
        operandTop = equationStr[:operatorPosition].strip()
        operandLow = equationStr[operatorPosition +1:].strip()       
            
        if operandTop.isnumeric() == False:
          return "Error: Numbers must only contain digits."
        if operandLow.isnumeric() == False:
          return "Error: Numbers must only contain digits."
              
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
    
        if diff >= 0:
            longestOperandLength = len(operandTop)
            while diff > 0:
                operandLow = " " + operandLow
                diff = diff - 1
    
        elif diff < 0:
            longestOperandLength = len(operandLow)
            while diff*-1 > 0:
                operandTop = " " + operandTop
                diff = diff + 1

        if longestOperandLength > 4:
            return "Error: Numbers cannot be more than four digits."        
        
        underRuleLength = 0
        underRuleLength = longestOperandLength + 2
        while underRuleLength > 0:
            underRule = underRule + "-"
            underRuleLength = underRuleLength - 1 
        
        underRule = underRule + "    "
        
        operandTop = "      " + operandTop
        operandLow = "    " + operator + " " + operandLow
        
        operandTopRow = operandTopRow + operandTop
        operandLowRow = operandLowRow + operandLow

        if len(result.strip()) > longestOperandLength:
            if int(result) < 0:
              resultRow = resultRow + "  " + str(result)
            else:
              resultRow = resultRow + " " + str(result)             
        elif len(result.strip()) <= longestOperandLength: 
            resultRow = resultRow + "  " + str(result)
              
    underRuleRow =  underRuleRow + underRule       
    
    if resultsDisplay == "":
      output = operandTopRow[4:] + "\n" + operandLowRow[4:] + "\n" + underRuleRow.rstrip()
    elif resultsDisplay == True:
      output = operandTopRow[4:] + "\n" + operandLowRow[4:] + "\n" + underRuleRow.rstrip() + "\n" + resultRow[4:]
    return output 