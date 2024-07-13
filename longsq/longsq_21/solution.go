package problem21

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
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var list1 *ListNode
	var list2 *ListNode

	var list1IntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &list1IntArray); err != nil {
		log.Fatal(err)
	}
	list1 = IntArrayToLinkedList(list1IntArray)
	var list2IntArray []int
	if err := json.Unmarshal([]byte(inputValues[1]), &list2IntArray); err != nil {
		log.Fatal(err)
	}
	list2 = IntArrayToLinkedList(list2IntArray)

	return mergeTwoLists(list1, list2).LinkedListToIntArray()
}
