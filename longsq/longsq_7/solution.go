package problem7

import (
	"encoding/json"
	"log"
	"strings"
)

func reverse(x int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}

	return reverse(x)
}
