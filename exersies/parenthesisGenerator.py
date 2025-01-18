def makeParenthesis(open, closed, paraList, resList):
    if open > closed:
        return
    if open == 0 and closed == 0:
        resList.append("".join(paraList))
        return

    if open > 0:
        paraList.append("(")
        makeParenthesis(open-1,closed,paraList, resList)
        paraList.pop()

    if closed > 0:
        paraList.append(")")
        makeParenthesis(open,closed-1, paraList,resList)
        paraList.pop()
def generateParentheses(n):
    resList = []
    makeParenthesis(n, n,[],resList)
    return resList
input1 = input()
print(generateParentheses(input1))
