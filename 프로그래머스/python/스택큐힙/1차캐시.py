def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
 
    
    return answer