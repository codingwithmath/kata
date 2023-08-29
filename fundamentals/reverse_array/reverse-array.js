module.exports = function reverseArray(array) {
    console.log(`Inputed array ${array} \n`)
    /**
     * aqui é criado um ponteiro que irá percorrer todo o array
     * o .length - 1 é feito pois o javascript retorna a quantidade de
     * itens dentro de um array e nós queremos o número da alocação do array
     */
    var ponteiroMaior = array.length - 1;

    /**
     * aqui é inicializado um ponteiro que será incrementado enquanto
     * percorrermos o array, ele serve para indicar as posicições inicias do array
     */
    var ponteiroMenor = 0

    /**
     * a verificação do loop é a comparação entre os ponteiros, quando eles estão
     * em posição de igualdade significa que chegamos na metade do array, portanto
     * o array já foi revertido
     */
    while(ponteiroMaior > ponteiroMenor) {
        var tmp = array[ponteiroMenor]

        array[ponteiroMenor] = array[ponteiroMaior]
        array[ponteiroMaior] = tmp

        ponteiroMaior--
        ponteiroMenor++
    }

    console.log(`outputed array ${array} \n`)

    return array;
}
