func hasDuplicate(nums []int) bool {
	cache := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		_, exists := cache[nums[i]]
		if exists {
			return true
		}
		cache[nums[i]] = true
	}
	return false
}
