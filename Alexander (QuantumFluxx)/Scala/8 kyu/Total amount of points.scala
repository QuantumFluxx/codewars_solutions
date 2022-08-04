object Kata {
  def points(games: Vector[String]): Int = games.map(game => {
        val p = game.split(":").map(_.toInt)
        if (p(0) > p(1)) 3 else if (p(0) == p(1)) 1 else 0
    }).sum
}
