package main

import (
	"os"
	"time"
	"math/rand"
	"fmt"
	"encoding/hex"
)

func _enc(input, key []byte) (output []byte){
	var length int
	if len(key) < len(input){
		length = len(key)
	} else {
		length = len(input)
	}
	output = make([]byte,length)

	for i:=0; i < length; i++ {
		output[i] += input[i % length] ^ key[i % length]
	}
	return output
}

func main() {
	flag,err := os.Open("flag.txt")
	data := make([]byte, 40)
	count, err := flag.Read(data)
	data = data[:count]
	if err != nil {
		fmt.Println("Cannot readfile")
		os.Exit(1)
	}
	key := make([]byte, count)
	x := time.Now().UTC().Unix()
	rand.Seed(x)
	rand.Read(key)
	enc := _enc(data,key)
	fmt.Printf("I encoded the flag for you, now give me the key\n")
	var new_key string
	fmt.Scanln(&new_key)
	decoded, err := hex.DecodeString(new_key)
	if err != nil{
		fmt.Println("I need hex")
		os.Exit(1)
	}
	fmt.Printf("decoded flag : %s\n",_enc(enc, decoded))
}
