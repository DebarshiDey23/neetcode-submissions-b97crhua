func isAnagram(s string, t string) bool {
	cache := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		ansVal, exists := cache[s[i]];
		if exists {
			cache[s[i]] = ansVal + 1
		} else {
			cache[s[i]] = 1
		}
	}
	for j := 0; j < len(t); j++ {
		amount, exists := cache[t[j]]
		if exists {
			cache[t[j]] = amount - 1
			if cache[t[j]] == 0 {
				delete(cache, t[j])
			}
		} else {
			return false
		}
	}
	return len(cache) == 0
}
