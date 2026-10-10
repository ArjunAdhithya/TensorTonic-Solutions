def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    
    def function(inp_a, inp_b, inp_c):
        y =  inp_a * inp_b + inp_c
        return float(y)

    d = function(a,b,c)
    da = (function(a+h, b, c) - d)/h
    db = (function(a, b+h, c) - d)/h
    dc = (function(a, b, c+h) - d)/h

    return (d,da, db, dc)