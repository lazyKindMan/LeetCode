package golang

import (
	problem "leetCode/longsq/longsq_15"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "15", "longsq", problem.Solve)
}
