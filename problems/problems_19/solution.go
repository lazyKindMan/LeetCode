package problem19

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode
	var n int

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	 var headPos int
	if err := json.Unmarshal([]byte(inputValues[1]), &headPos); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedListCycle(headIntArray, headPos)
	if err := json.Unmarshal([]byte(inputValues[2]), &n); err != nil {
		log.Fatal(err)
	}

	return LinkedListToIntArray(removeNthFromEnd(head, n))
}
