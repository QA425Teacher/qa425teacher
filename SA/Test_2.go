// Спасибо нейронкам, что  научили кодить на голенге!
package main

import "fmt"

type Pair struct {
	a, b int
}

func (p Pair) calcSum() int {
	return p.a + p.b
}

func main() {
	a := 10
	b := 20
	pair := Pair{a, b}
	sum := pair.calcSum()
	fmt.Printf("Сумма %d и %d равна %d\n", pair.a, pair.b, sum)
}
