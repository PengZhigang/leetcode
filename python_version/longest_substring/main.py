class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=""
        m=0
        for i in s:
            if i in x:
                x=x[x.index(i)+1:]
                print(x)
            x+=i
            m=max(m,len(x))
        return m


def main():
    s = "dvdf"
    print(s.index("v"))
    print(Solution.lengthOfLongestSubstring(Solution, s))

if __name__ == "__main__":
    # execute only if run as a script
    main()
