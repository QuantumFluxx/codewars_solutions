object CenturyYear {
    def centuryFromYear(year: Int): Int = math.ceil(year / 100.0).toInt
}
