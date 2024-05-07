var x1, N=2.3
var x0 = 30
var tol = 0.001

var sx = function(x0){
    return 0*x0**9 + 0*x0**8 - 0*x0**7 + 0.02*x0**6 - 0.36*x0**5 + 3.93*x0**4 - 25.29*x0**3 + 87.78*x0**2 - 124.23*x0
}
var vx = function(x0){
    var h = 0.0000001
    return sx(x0+h)-sx(x0)/h
}
// OBTENDO A FUNÇÃO PARA CALCULAR
var fx = function(x){
    return vx(x) - N
}
var dfx = function(x){
    var h = 0.000001
    return (fx(x+h)-fx(x))/h
}
// NEWTON-RAPHSON
var MNR = function(x){
    return x1 = x - (fx(x)/dfx(x))
}
//APLICAÇÃO

for (var i = 1;i<=200;i++){
    MNR(x0)
    if (Math.abs(x1-x0)<tol){
        x0 = x1
    break;
}
    else {
        x0 = x1
    }
}
console.log('a raiz e '+x0)
