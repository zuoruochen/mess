import scala.io.Source
import scala.collection.mutable.ListBuffer

val restaurant = ListBuffer[String]()


if (args.length > 0) {
    for (line <- Source.fromFile(args(0)).getLines)
      restaurant.append(line)
}
else{
  Console.err.println("Please enter filename")
}

def whereToEat(target :List[String]):String = { 
    val index = scala.util.Random.nextInt(target.length)
      return target(index)
}

println(whereToEat(restaurant.toList))


