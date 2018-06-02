package kata

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Basic tests", func() {
	It("should return the correct values", func() {
		Expect(bandNameGenerator(string("knife"))).Should(BeEquivalentTo("The Knife"))
		Expect(bandNameGenerator(string("tart"))).Should(BeEquivalentTo("Tartart"))
		Expect(bandNameGenerator(string("sandles"))).Should(BeEquivalentTo("Sandlesandles"))
		Expect(bandNameGenerator(string("bed"))).Should(BeEquivalentTo("The Bed"))
	})
})