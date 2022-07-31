object Order {
    def descendingOrder(num: Int): Int = num.toString.split("").sortWith(_ > _).mkString("").toInt
}
