func twoSum(nums []int, target int) []int {
    cache := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        complement := target - nums[i];
        ansVal, exists := cache[complement];
        if exists {
            return []int{ansVal, i}
        }
        cache[nums[i]] = i;
    }
    return nil
}
