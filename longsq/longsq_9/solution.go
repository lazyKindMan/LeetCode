package problem9

import (
	"encoding/json"
	"log"
	"strings"
)

func isPalindrome(x int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}

	return isPalindrome(x)
}
