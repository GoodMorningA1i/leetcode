class RandomizedSet {

    private var set: Set<Int>

    init() {
        self.set = Set()
    }

    func insert(_ val: Int) -> Bool {
        if self.set.contains(val) {
            return false
        }
        self.set.insert(val)
        return true
    }

    func remove(_ val: Int) -> Bool {
        if !self.set.contains(val) {
            return false
        }

        self.set.remove(val)
        return true
    }

    func getRandom() -> Int {
        let setArray = Array(self.set)
        let index = Int.random(in: 0..<setArray.count)
        return setArray[index]
    }
}