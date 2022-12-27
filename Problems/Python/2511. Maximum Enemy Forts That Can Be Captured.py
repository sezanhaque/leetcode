from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        count, max_count = 0, 0
        trigger = []

        for idx in range(len(forts)):
            # If triggered, means 1 or -1 and current value is not 0
            # and is not equal to last value of trigger then get max_count
            # and append the current value to trigger, make count 0

            # Why we are doing it? Because it means we have already
            # faced any 1 / -1, and we have counted some enemies
            # So now we have faced again 1 / -1, so we should store
            # total count to max_count.
            # By this way it will help to get max_count again if
            # we have to count from start again.
            if len(trigger) and forts[idx] != 0 and forts[idx] != trigger[-1]:
                max_count = max(max_count, count)
                trigger.append(forts[idx])
                count = 0

            # If we have triggered values and current value is not 0
            # and current value is equal to last value of trigger 1 / -1
            # it means we have faced same 1 / -1 twice.
            # So we should count from start again.
            if len(trigger) and forts[idx] != 0 and forts[idx] == trigger[-1]:
                count = 0

            # If current value is not 0
            # then we append the value to trigger
            # as it will trigger our count.
            if forts[idx] != 0:
                trigger.append(forts[idx])

            # If we have triggered values and current value is 0
            # it means we can count enemies.
            if len(trigger) and forts[idx] == 0:
                count += 1

        return max_count


obj = Solution()
print(obj.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]))  # 4
print(obj.captureForts([-1, -1, 1, -1, -1, 0]))  # 0
print(obj.captureForts([-1, 0, -1, 0, 1, 1, 1, -1, -1, -1]))  # 1
print(obj.captureForts([0, -1, -1, 0, -1]))  # 0
print(obj.captureForts([0, 0, 1, -1]))  # 0
