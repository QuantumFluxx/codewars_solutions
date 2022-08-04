object Kata {
    def expressionMatter(a: Int, b: Int, c: Int): Int = List(
        a + b + c,
        a * b * c,
        a + b * c,
        a * b + c,
        a * (b + c),
        (a + b) * c
    ).max
}
