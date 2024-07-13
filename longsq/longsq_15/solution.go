package problem15

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	sort.Ints(nums)
	n := len(nums)
	for i := 0; i < n-2; i++ {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}
		left := i + 1
		right := n - 1
		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum == 0 {
				res = append(res, []int{nums[i], nums[left], nums[right]})
				for left = left + 1; left < right && nums[left-1] == nums[left]; left++ {
				}
				for right = right - 1; left < right && nums[right] == nums[right+1]; right-- {
				}
			} else if sum < 0 {
				left++
			} else {
				right--
			}
		}
	}
	return res
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return threeSum(nums)
}
