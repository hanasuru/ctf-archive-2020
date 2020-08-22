package main

import (
	"time"
	"math/rand"
	"fmt"
)
func main() {
	// flag,err := os.Open("flag.txt")
	// data := make([]byte, 40)
	// count, err := flag.Read(data)
	// data = data[:count]
	// if err != nil {
	// 	fmt.Println("Cannot readfile")
	// 	os.Exit(1)
	// }
	key := make([]byte, 40)
	x := time.Now().UTC().Unix()
	rand.Seed(x)
	rand.Read(key)
	fmt.Printf("%x",key)
}