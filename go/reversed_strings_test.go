package kata

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
)

var _ = Describe("Test Example", func() {
   It("should test that the solution returns the correct value", func() {
     Expect(Solution("world")).To(Equal("dlrow"))
   })
})
