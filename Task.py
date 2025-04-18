from collections import deque

class Solution:
    
    @staticmethod
    def initialize_task(task_num: int, prereq: list[list[int]]) -> tuple[list[list[int]], 
                                                                         list[int]]:
        prereq_num = [0] * task_num
        next_task = [[] for _ in range(task_num)]

        for ele in prereq:
            current = ele[0]
            pre = ele[1]
            next_task[pre].append(current)
            prereq_num[current] += 1

        return next_task, prereq_num 
    
    @staticmethod
    def organize_order(task_num: int, prereq: list[list[int]]) -> list[int]:
        if task_num == 0:
            return []

        next_task, prereq_num = Solution.initialize_task(task_num, prereq)
        queue = deque()
        for i, ele in enumerate(prereq_num):
            if ele == 0:
                queue.append(i)

        ans = []
        while queue:
            pre_task = queue.popleft()
            ans.append(pre_task)

            for next in next_task[pre_task]:
                prereq_num[next] -= 1

                if prereq_num[next] == 0:
                    queue.append(next)

        if len(ans) == task_num:
            return ans
        else:
            return []


if __name__ == "__main__":
    n = 4
    l = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution.organize_order(4, l))
    l = [[1, 0], [2, 0], [2, 1], [3, 2], [1, 3]]
    print(Solution.organize_order(4, l))