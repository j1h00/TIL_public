# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            nowLog = log.split(" ")
            if nowLog[1].isalpha():
                letter_logs.append(log)
                continue
            digit_logs.append(log)
        
        return sorted(letter_logs, key = lambda x: (x.split(" ")[1:], x.split(" ")[0])) + digit_logs
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# isdigit 
class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[0]) #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:]) #sort by suffix
        result = letters + digits                                        #put digit logs after letter logs
        return result