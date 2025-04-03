from pulp import *

def optimize_allocation(data, budget):
    model = LpProblem("Resource_Allocation", LpMaximize)
    items = []
    vars = []

    for item, price, max_qty in data:
        var = LpVariable(item, 0, max_qty, cat='Integer')
        items.append((item, price, var))
        vars.append(var)

    model += lpSum([price * var for item, price, var in items])
    model += lpSum([price * var for item, price, var in items]) <= budget

    # 👇 This forces the use of the built-in CBC solver without requiring system access
    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)

    result = {item: var.varValue for item, price, var in items}
    return result
