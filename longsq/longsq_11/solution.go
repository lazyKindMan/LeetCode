package problem11

import (
	"encoding/json"
	"log"
	"strings"
)

func maxArea(height []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var height []int

	if err := json.Unmarshal([]byte(inputValues[0]), &height); err != nil {
		log.Fatal(err)
	}

	return maxArea(height)
}
