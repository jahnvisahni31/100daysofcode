class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        le = []
        di = []
        for log in logs:
            if log.split()[1].isdigit():   #first it sort based on the digit then if it is digit then put them on digit log and if not then on letter log
                di.append(log)
            else:
                le.append(log)

        le.sort(key= lambda x: (x.split()[1:],x.split()[0]))    #it sort character by character on letter log by the method lexicographically
        return le+di  
