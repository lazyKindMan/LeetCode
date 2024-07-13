package problem12

import (
	"encoding/json"
	"log"
	"strings"
)

func intToRoman(num int) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return intToRoman(num)
}
