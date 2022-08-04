object Shortest {
    def findShort(str: String): Int = str.split(" ").map(_.length).min
}
