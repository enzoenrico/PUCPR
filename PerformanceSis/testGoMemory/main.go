package main

import (
	"fmt"
)

func main() {
	x := 2
	y := 3
	fmt.Println(x + y)
	mem := &x
	fmt.Println(mem)
	fmt.Printf("mem variable memory address %v", *mem)

}
