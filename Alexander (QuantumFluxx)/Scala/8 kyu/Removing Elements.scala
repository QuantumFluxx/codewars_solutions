object Kata {
    def removeEveryOther[T](list: List[T]): List[T] = {
        var n = 0
        list.filter(_ => {
            val should_skip = n % 2 == 0
            n += 1
            should_skip
        })
    }
}
