import scala.io.Source


def whereToEat(target :List[String]):String = { 
    val index = scala.util.Random.nextInt(target.length)
      return target(index)
}

if (args.length > 0) {
    val restaurant = Source.fromFile(args(0)).getLines.toList
    println(whereToEat(restaurant))
}
else{
  Console.err.println("Please enter filename")
}
