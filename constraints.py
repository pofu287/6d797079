class Constraints:
    """all methods for checking overlap, working hours and other constraints that will be listed here
    """
    @staticmethod
    def dt_overlap(times):
       # returns true if period s1 and s2 overlap.  s1 s2 e1 e2 in times list
        s1 = times[0][0]
        e1 = times[0][1]
        s2 = times[1][0]
        e2 = times[1][1]       
        if is_between(s1,s2,e2) or is_between(e1, s2, e2) or is_between(s2, s1, e1) or is_between(e2, s1,e1):
            return true
        return false
        
    @staticmethod   
    def is_between(t, t1, t2):
        # datetime input. true if t is between t1 and t2. false otherwise
        if t1<= t <= t2:
            return True
        return False
