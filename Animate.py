class Solution:
    
    @staticmethod 
    def animate(speed: int, init: str) -> list[str]:
        n = len(init)

        if n < 1:
            return []
        
        result = []
        t = 0

        while True:
            particle_inside = False
            particle_check = [False] * n

            for i, char in enumerate(init):
                if char == "L":
                    pos = i - t * speed
                elif char == "R":
                    pos = i + t * speed
                else:
                    continue

                if pos > -1 and pos < n:
                    particle_check[pos] = True
                    particle_inside = True

            tmp = "".join("X" if check else "." for check in particle_check)      
            result.append(tmp)      
            
            if not particle_inside:
                break

            t += 1
        
        return result
    
if __name__ == "__main__":
    print(Solution.animate(2, "..R...."))
    print(Solution.animate(3, "RR..LRL"))
    print(Solution.animate(2, "LRLR.LRLR"))
    print(Solution.animate(10, "RLRLRLRLRL"))
    print(Solution.animate(1, "..."))
    print(Solution.animate(1, "LRRL.LR.LRR.R.LRRL."))
            