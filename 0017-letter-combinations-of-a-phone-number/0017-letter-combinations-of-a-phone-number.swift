class Solution {
    func letterCombinations(_ digits: String) -> [String] {
        let digitsToChar: [Character: [Character]] = [
            "2": Array("abc"),
            "3": Array("def"),
            "4": Array("ghi"),
            "5": Array("jkl"),
            "6": Array("mno"),
            "7": Array("qprs"),
            "8": Array("tuv"),
            "9": Array("wxyz")
        ]

        var comb: [String] = []
        var currComb: [Character] = []
        let digitsArray = Array(digits)

        func dfs(_ i: Int) {
            if digits.count == currComb.count {
                comb.append(String(currComb))
                return
            }
            if i >= digits.count {
                return
            }

            let digit = digitsArray[i]
            guard let letters = digitsToChar[digit] else { return }
            for c in letters {
                //include i
                currComb.append(c)
                dfs(i + 1)
                currComb.removeLast()

                //don't include i
                dfs(i + 1)
            }
        }

        dfs(0)
        return comb
    }
}