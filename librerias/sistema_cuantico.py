import cal_complejos as cal

def prob_pos_v(v,x):
    return cal.modulo(v[x][0])**2/cal.normaVectorial(cal.traspuestaVector_v(v))**2

def prob_pos_h(v,x):
    return cal.modulo(v[x])**2/cal.normaVectorial(v)**2

def valor_esperado(sistema,omega):
    primero = cal.multiplicacionMatriz(omega,sistema)
    cal.imprimir_matriz(primero)
    return cal.productoInterno(primero,sistema)

